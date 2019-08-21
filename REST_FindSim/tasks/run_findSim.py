import subprocess
import re

from .utility import FindSimResult, parse_output, decode_bytes

def run_findSim( script, modelFile , dumpFname = "", paramFname = "", hidePlot = False, hideSubplots = False, optimizeElec=True,  silent = False, scaleParam=[], settleTime = 0, settleDict = {} ):
    t_result = FindSimResult()

    # Validation of .tsv file and modle file
    fs = script.split('.')
    if len(fs) < 2 or fs[-1] != 'tsv':
        t_result.set_error('Invalid script file type.')
    fs = []
    fs = modelFile.split('.')
    if len(fs) < 2 or (fs[-1] != 'g' and fs[-1] != 'xml' and fs[-1] != 'py'):
        t_result.set_error('Invalid model file type.')

    if t_result.error:
        return t_result

    # Generate command line
    # This .py code print all we need into stdout
    command_FindSim = 'python third_party/interface_FindSim.py '+script+' -m '+modelFile
    if paramFname != "":
        command_FindSim += ' -p ' + paramFname
    if hidePlot:
        command_FindSim += ' -hp'

    # TODO(Chen, 1103324644@qq.com): add other arguments into command line
    '''
    if dumpFname:
    if not optimizeElec:
    if silent:
    if scaleParam:
    if settleTime:
    if settleDict:
    '''
    
    # Run FindSim via subprocess
    # output = subprocess.getoutput(command_FindSim)
    print(command_FindSim)
    p = subprocess.Popen(command_FindSim,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output_info, error_info = p.communicate()
    p.wait()

    # Parse output
    t_result = parse_output(decode_bytes(output_info),decode_bytes(error_info),"Experiment")

    return t_result
