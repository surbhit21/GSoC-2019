# GSoC-2019
Google Summer of Code 2019 project

This will be a working implementation of a RESTful API to run FindSim experiment on NSG (https://www.nsgportal.org/) server.

Pre-requisites:

- Moose (https://github.com/BhallaLab/moose)
- FindSim (https://github.com/BhallaLab/FindSim)
- Mpld3 (http://mpld3.github.io/)
- Python3 virtualenv
- Django, djangorestframework

1. Install Python3

2. Set up Python3 venv(optional)

3. Install following packages via apt:
python-dev
libgsl0-dev
libhdf5-dev
python3-tk

4. Install following packages via pip:
numpy
wheel
python-libsbml
matplotlib
pyneuroml
Jinja2
mpld3
Django
djangorestframework

5. install moose

> pip install pymoose --user --pre --upgrade

6. Clone FindSim from repostory and link FindSim to REST_FindSim/third_party

> git clone https://github.com/BhallaLab/FindSim.git

> ln -s path/to/your/FindSim REST_FindSim/third_party/FindSim


APIs:

/tasks/

POST:  
{  
'tsv_file': .tsv file  
'model_file': model file(.g or .xml)  
}  


Response:  
{  
'score': score of experiment  
'time': cost time  
'figure': html string of the figure  
'error': infomations when error happens  
}  
