# GSoC-2019
Google Summer of Code 2019 project

This will be a working implementation of a RESTful API to run FindSim experiment on NSG (https://www.nsgportal.org/) server.


## Contents:

* [1.Introduction](#1)
* [2.Registration to Findsim Interface](#2)
* [3.APIs' User Guide](#3)
* [4.Testing](#4)

<h2 id="1">1.Introduction</h2>

#### About FindSim


Framework for Integrating Neuronal Data and Signaling Models (FindSim) is a tool that enable systematic validation and optimization of a neuronal signaling model by anchoring a model to actual experiment dataset. It is a framework for integrating many individual electrophysiological and biochemical experiments with large, multiscale models so as to systematically refine and validate the model. We use a structured format for encoding the conditions of many standard physiological and pharmacological experiments, specifying which parts of the model are involved, and comparing experiment outcomes  with model output. A database of such experiments is run against successive generations of composite cellular models to iteratively improve the model against each experiment, while retaining global model validity. This toolchain provides a principled and scalable way to tackle model complexity and diversity of data sources.



#### Using REST APIs to Access FindSim on High-Performance Server

Running a FindSim can be a computing extensive processes depending on the size of the model and various parameters involved. With FindSim running on a high-performance machine, we can handle models and data with larger scale in less time. Meanwhile, we want more flexible access to FindSim, for example doing experiments by FindSim on a web borwser.
To combine the flexibility of users' machines and the the computation power of high-performance machine, we developed FindSim REST APIs. Based on HTTP protocol, you can access well implemented FindSim running  on a high-performance machine with your network terminal anywhere.
We also have web-based tool named FindSim-drupal(See https://github.com/BhallaLab/Findsim-drupal) which allow users to use the FindSim pipeline in a user-friendly way. This REST APIs for FindSim can be a strong support for the web tool.



<h2 id="2">2.Registration to Findsim Interface</h2>


<h2 id="3">3.APIs' User Guide</h2>

#### Implementing REST APIs on Server

##### Installing Pre-requisites:

###### Pre-requisites List:

- Moose (https://github.com/BhallaLab/moose)
- FindSim (https://github.com/BhallaLab/FindSim)
- Mpld3 (http://mpld3.github.io/)
- Python3 virtualenv
- Django
- djangorestframework

##### Tutorial

- Install Python3
- Set up Python3 venv(optional but recommended)
- Install following packages via apt:
    + python-dev
    + libgsl0-dev
    + libhdf5-dev
    + python3-tk
- Install following packages via pip:  
    + numpy
    + wheel
    + python-libsbml
    + matplotlib
    + pyneuroml
    + Jinja2
    + mpld3
    + Django
    + djangorestframework
    + scipy

- Install moose

    > pip install pymoose --user --pre --upgrade

- Clone FindSim from repostory and link FindSim to REST_FindSim/third_party

    > git clone https://github.com/BhallaLab/FindSim.git

    > ln -s path/to/your/FindSim REST_FindSim/third_party/FindSim

#### APIs' User Guide

The examples in this guide use the unix curl command and assume you have set the following environment variables(replace the 'your_base_url' and 'your_user_name' according to your situation):
> export URL=your_base_url
> export UNAME=your_user_name

##### Submit Experiment Tasks

One of the most important and basic API is to run experiments on FindSim. You need to POST your username and two files(a .tsv file and a model file) as input of FindSim.
Using following command:
> curl \$URL/tasks/Calculation/ \\
> -F "username=$UNAME" \\
> -F "tsv_file=@tsv_file_path" \\
> -F "model_file=@model_file_path"

Here 'tsv_file_path' and 'model_file_path' represents the .tsv file and model file you would like to upload.
Once you've sent a POST request with correct format, it will be reguarded as a 'task'. After running in FindSim, the input and output will also be stored in the database. You will get a json as response which contains the information of your task and looks like:
>{  
    "username":"your_username"
    "tsv_file": URL/media/files/tsv/your_tsv_file
    "model_file": URL/media/files/model/your_model_file
    'score': "0.01000000"
    'time': "5.00000000"  
    'figure': "\n\n<style>\n\n</style>\n\n</div>\n<script>\nfunction mpld3_load_lib(url, callback){Result mpld3 data here.}\n</script>\n"  
    'error': ""
    }  

The 'figure' field contains html string of matplotlib plot, visualizing the result of the experiment.
If experiment ran normally, the 'error' should be an empty string, or it will contain some error info so that you can figure out what happened and how to make it right.


##### Submit Optimization Tasks

Another basic API is to submit optimization tasks. It's quite like the submitting of experiment tasks.
By sending POST requests like this:
> curl \$URL/tasks/Optimization/ \\
> -F "username=\$UNAME" \\
> -F "num_processes=" \\
> -F "torlance=" \\
> -F "tsv_files=@tsv_zip_file_path" \\
> -F "model_file=@model_file_path" \\

you can submit and run an optimization task on the server. Notice that 'num_porcesses' and 'torlance' here are arguments for running optimizatin, and the tsv_file must be a .zip file contains at least one .tsv file.
The responding json looks like:
> {
        "username": "your_username",
        "tsv_files": URL/media/files/tsv/your_tsv_zip_file
        "model_file": URL/media/files/model/your_model_file
        "num_processes": "1",
        "tolerance": "0.500000000",
        "parameters": "[\"ATP.concInit\", \"R2C2.concInit\", \"PKA_Inhibitor.concInit\", \"Reac_R2C2.Kd\", \"Reac_R2C2.tau\", \"Reac_cAMP_R2C2.Kd\", \"Reac_cAMP_R2C2.tau\", \"Reac_cAMP2_R2C2.Kd\", \"Reac_cAMP2_R2C2.tau\", \"Reac_cAMP3_R2C2.Kd\", \"Reac_cAMP3_R2C2.tau\", \"Reac_cAMP4_R2C2.Kd\", \"Reac_cAMP4_R2C2.tau\", \"Reac_cAMP4_R2C.Kd\", \"Reac_cAMP4_R2C.tau\", \"Reac_PKA_Inhibitor.Kd\", \"Reac_PKA_Inhibitor.tau\"]",
        "score": "Init score = 0.6310, final = 0.63095591",
        "time": "6.5020000000",
        "optimized_model": URL/downloadUri,
        "error": ""
    }

The "parameters" field is a list of moose name. The list is the input of optimization generated from all the .tsv files and it may be helpful if the users can acquire the full list.
The "optimized_model" provides a "downloadUri" to users by which they can download the model file generated by optimization process.

##### List Tasks

Send GET request and you can acquire all the submitted tasks.
> curl $URL/tasks/Calculation/
> curl $URL/tasks/Optimization/

Notice that any user can acquire all the tasks record or even download the output file generated by tasks that other users submitted. This may need improvements in the future.


##### Download Results

As mentioned above, optimizaiton tasks will generated new model file. You can download the model files using the downloadUri in the task infomation. Make sure you have the right downloadUri and send GET request like this:
> curl -O $URL/downloadUri

and the model file will be downloaded into yout current directory.

##### Delete and cancel(Unfinished)

In the future we may provide API that allow users to delete their submissions.


##### Summary

|  url   | POST | GET |
|  ----  | ----  | ---- |
| $URL/tasks/Calculation/ | Give username, upload .tsv file and model(.g or .xml) file.<br>Response score, running time and experiemnt result figure |  response all calculation tasks|
| $URL/tasks/Optimization/ | Give username, upload .tsv files(in a .zip file) and model(.g or .xml) file and other arguments.<br>Response a parameters list, score, running time and url of optimized model file |  response all Optimization tasks|
| $URL/downloadUri | - | Download optimized model file |

<h2 id="4">4.Testing</h2>

#### Running TestCase to test models:

 Go to this directory and run the following command to test APIs:
> cd REST_FindSim  
> ./manage.py test tasks.tests  

#### Select part of the testcases:

if you want to test part of the testcases. Use --tag arguments:
> ./manage.py test tasks.tests --tag=calculation  

if you get 'OK' on your command line ouput, then you have passed the test on your machine.

The command above will test only FindSim API.

- The tags we provided are:

|  Tags  | Testcases |
|  ----  | ----  |
| calculation | All .tsv test files for calculation(FindSim) API |
| BC | BarChart .tsv test files for calculation(FindSim) API |
| DP | DirectParameter .tsv test files for calculation(FindSim) API |
| DR | DoseResponse .tsv test files for calculation(FindSim) API |
| TS | TimeSeries .tsv test files for calculation(FindSim) API |
| optimization | All testcases for optimization API |
