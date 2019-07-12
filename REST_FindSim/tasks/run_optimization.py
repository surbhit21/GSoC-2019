import subprocess
import re
import zipfile
import os

from .utility import OptimizationResult, parse_output, decode_bytes
from .run_findSim import run_findSim


def run_optimization( tsv_zip, model_file , file_label, optimized_model, num_processes, tolerance):
    t_result = OptimizationResult()

    # Validation of .tsv file and modle file
    fs = tsv_zip.split('.')
    if len(fs) < 2 or fs[-1] != 'zip' or len(tsv_zip) < 5:
        t_result.set_error('Invalid .tsv zip file type.')
    fs = []
    fs = model_file.split('.')
    if len(fs) < 2 or (fs[-1] != 'g' and fs[-1] != 'xml'):
        t_result.set_error('Invalid model file type.')

    if t_result.error:
        return t_result

    # Unzip .tsv files and save them into a directory
    f = zipfile.ZipFile(tsv_zip, 'r')
    for file in f.namelist():
        f.extract(file,'media/files/tsv/'+file_label)
    f.close()

    # Firstly, run findSim to generate parameters list for each .tsv file
    # tsv_file_path = tsv_zip[0:len(tsv_zip)-4]
    tsv_file_path = 'media/files/tsv/'+file_label
    tsv_file_path_new = os.path.join(tsv_file_path, 'tsv_files')
    os.mkdir(tsv_file_path_new)

    # Record parameters in a dictionary
    param_list_d = {}
    # Record num of tsv files
    tsv_cnt = 0
    # output file of findSim: param list
    tmp_param_list_path = os.path.join('media/files/tsv/'+file_label,"tmp_param_list.txt")
    # Traverse through directory
    for root, dirs, files in os.walk(tsv_file_path, topdown=False):
        # For each .tsv file in the directory
        for file in files:
            # Check if this is a .tsv file:
            if file.split('.')[-1] != 'tsv':
                continue
            else:
                tsv_cnt += 1
            # Run findSim to generate param list, use '-p'
            # Set param file : tmp_param_list_path
            # and set hp : True
            # Check if there exists wrong file type
            tmp_file_path = os.path.join(root,file)
            run_findSim( tmp_file_path, model_file , "", tmp_param_list_path, True)
            # Fetch params and add them into dictionary
            try:
                tmp_param_list = open(tmp_param_list_path, 'r+')
                param = tmp_param_list.readline().strip()
                # For each param
                while param:
                    tmp_contents = param.split('   ')
                    assert(len(tmp_contents) == 2)
                    param = tmp_contents[0]+'.'+tmp_contents[1]
                    if param not in param_list_d:
                        param_list_d[param] = True
                    param = tmp_param_list.readline().strip()
            except OSError:
                t_result.set_error('Error when open param list(while running FindSim)')
                return t_result
            else:
                tmp_param_list.close()
            os.rename(tmp_file_path, os.path.join(tsv_file_path_new,file))
    # Check if there exists files
    if tsv_cnt == 0:
        t_result.set_error("No .tsv file in directory")
        return t_result
    print("Collected %d .tsv files." % tsv_cnt)

    # Secondly, run optimization according to parameter list
    # Generate param list:
    param_list_commandline = ""
    for param in param_list_d.keys():
        param_list_commandline += param + ' '
    # Generate command line:
    command_Optimization = 'python third_party/FindSim/multi_param_minimization.py '\
                           + tsv_file_path_new\
                           + ' -n ' + str(num_processes)\
                           + ' -m ' + model_file\
                           + ' -f ' + optimized_model\
                           + ' -p ' + param_list_commandline\
                           + ' -t ' + str(tolerance)

    # Run Optimization via subprocess
    print(command_Optimization)
    p = subprocess.Popen(command_Optimization,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output_info, error_info = p.communicate()
    p.wait()
    # Parse output
    t_result = parse_output(decode_bytes(output_info),decode_bytes(error_info),"Optimization")
    t_result.set_model(optimized_model)
    if not t_result.parameters:
        for param in param_list_commandline.split(' '):
            t_result.add_parameter(param)

    return t_result
