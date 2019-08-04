# GSoC-2019
Google Summer of Code 2019 project

This will be a working implementation of a RESTful API to run FindSim experiment on NSG (https://www.nsgportal.org/) server.


## Contents:

* [1.Implementing](#1)
* [2.RESTful APIs](#2)
* [3.Testing](#3)


<h2 id="1">1. Implementing FindSim & Setting up environment</h2>

#### Pre-requisites:

- Moose (https://github.com/BhallaLab/moose)
- FindSim (https://github.com/BhallaLab/FindSim)
- Mpld3 (http://mpld3.github.io/)
- Python3 virtualenv
- Django, djangorestframework

#### Turorial
- Install Python3
- Set up Python3 venv(optional)
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

- install moose
```
    > pip install pymoose --user --pre --upgrade
```
- Clone FindSim from repostory and link FindSim to REST_FindSim/third_party
```
    > git clone https://github.com/BhallaLab/FindSim.git

    > ln -s path/to/your/FindSim REST_FindSim/third_party/FindSim
```

<h2 id="2">2. RESTful APIs</h2>


 #### By now, there are following APIs:  

|  url   | POST | GET |
|  ----  | ----  | ---- |
| /tasks/Calculation/ | Give username, upload .tsv file and model(.g or .xml) file.<br>Response score, running time and experiemnt result figure |  response all calculation tasks|
| /tasks/Optimization/ | Give username, upload .tsv files(in a .zip file) and model(.g or .xml) file and other arguments.<br>Response a parameters list, score, running time and url of optimized model file |  response all Optimization tasks|
| /media/files/model/<unique_url_for_a_optimization_task> | - | Download optimized model file |


1. url: /tasks/Calculation/

    POST:  
    {  
    'username': provided by front-end  
    'tsv_file': .tsv file  
    'model_file': model file(.g or .xml)  
    }  


    Response:  
    A task info:  
    {  
    'score': score of experiment  
    'time': cost time  
    'figure': html string of the figure  
    'error': infomations when error happens  
    }  

    GET:  
    Response:  
    A list of calculation tasks.  

2. url: /tasks/Optimization/

    POST:  
    {  
    'username': provided by front-end  
    'tsv_files': a .zip file contains only .tsv files  
    'model_file': model file(.g or .xml)  
    'num_processes': parameters for running optimization(integer)  
    'tolerance': parameters for running optimization(float point number under 1.0)  
    }  

    Response:  
    A task info:  
    {  
    'parameters': parameter list according to .tsv files  
    'score': score of experiment  
    'time': cost time  
    'optimized_model': url for downloading model file  
    'error': infomations when error happens  
    }  

    GET:  
    Response:  
    A list of optimization tasks.  

3. url: In the response of API-2

    GET:
    response: downloading modle file.

    

<h2 id="3">3.Testing</h2>

#### Running TestCase to test models:

> cd REST_FindSim
> ./manage.py test tasks.tests
