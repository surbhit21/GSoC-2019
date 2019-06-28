import subprocess
import re
import zipfile
import os

from .utility import *


def run_optimization( tsv_zip, model_file , file_label, optimized_model, num_processes = 2, tolerance = 1e-4):
    t_result = FindSimResult()

    # Validation of .tsv file and modle file
    fs = tsv_zip.split('.')
    if len(fs) < 2 or fs[-1] != 'zip':
        t_result.set_error('Invalid .tsv zip file type.')
    fs = []
    fs = model_file.split('.')
    if len(fs) < 2 or (fs[-1] != 'g' and fs[-1] != 'xml'):
        t_result.set_error('Invalid model file type.')

    if t_result.error:
        return t_result

    # Unzip .tsv files and save them into a directory
    f = zipfile.ZipFile(tsv_zip, 'r')
    for file in f.nameliset():
        f.extract(file,'files/tsv')
    f.close()

    # Generate command line
    # This .py code print all we need into stdout
    command_Optimization = 'python third_party/interface_FindSim.py '+script+' -m '+modelFile
    # TODO(Chen): add other arguments into command line
    '''
    if dumpFname:
    if paramFname:
    if not optimizeElec:
    if silent:
    if scaleParam:
    if settleTime:
    if settleDict:
    '''

    # Run FindSim via subprocess
    # output = subprocess.getoutput(command_FindSim)
    p = subprocess.Popen(command_FindSim,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output_info, error_info = p.communicate()

    #print(type(output_info))
    #print(type(error_info))
    p.wait()

    # Parse output
    t_result = parse_output(decodeBytes(output_info),decodeBytes(error_info))

    return t_result
