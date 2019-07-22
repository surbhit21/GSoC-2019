from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Calculation, Optimization
from .serializers import CalculationSerializer, OptimizationSerializer
from .run_findSim import run_findSim
from .run_optimization import run_optimization

import os
import json
import zipfile
import time
import shutil

BASE_FILE_PATH = 'media/files/'

# Create your views here.
class CalculationViewSet(viewsets.ModelViewSet):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer

    def create(self, request, *args, **kwargs):

        global BASE_FILE_PATH
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #parse the path to .tsv file and model file

        tsv_path = os.path.join(BASE_FILE_PATH, 'tsv/') + serializer.validated_data['tsv_file'].name
        model_path = os.path.join(BASE_FILE_PATH, 'model/') + serializer.validated_data['model_file'].name

        res = run_findSim(tsv_path,model_path)
        os.remove(tsv_path)
        os.remove(model_path)

        serializer.validated_data['score'] = res.score
        serializer.validated_data['time'] = res.time
        serializer.validated_data['figure'] = res.figure
        serializer.validated_data['error'] = res.error

        serializer.save()
        headers = self.get_success_headers(serializer.data)
        os.remove(tsv_path)
        os.remove(model_path)
        return Response(serializer.data)


class OptimizationViewSet(viewsets.ModelViewSet):
    queryset = Optimization.objects.all()
    serializer_class = OptimizationSerializer


    def create(self, request, *args, **kwargs):

        global BASE_FILE_PATH
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #parse the path to .tsv file and model file
        tsv_path = os.path.join(BASE_FILE_PATH, 'tsv/') + serializer.validated_data['tsv_files'].name.split('/').pop()
        model_path = os.path.join(BASE_FILE_PATH, 'model/') + serializer.validated_data['model_file'].name.split('/').pop()
        file_label = serializer.validated_data['username'] + str(time.time())
        os.mkdir(os.path.join(BASE_FILE_PATH, 'tsv/')+file_label)
        os.mkdir(os.path.join(BASE_FILE_PATH, 'model/')+file_label)
        os.mkdir(os.path.join(BASE_FILE_PATH, 'model/')+file_label+'/optimized')
        tsv_path_new = os.path.join(BASE_FILE_PATH, 'tsv/'+file_label+'/') + serializer.validated_data['tsv_files'].name
        model_path_new = os.path.join(BASE_FILE_PATH, 'model/' + file_label+'/') + serializer.validated_data['model_file'].name
        print(tsv_path_new)
        # Rename the files to avoid collision
        if os.path.exists(tsv_path):
            os.rename(tsv_path, tsv_path_new)
        else:
            serializer.validated_data['error'] = '.tsv files not found'

        if os.path.exists(model_path):
            os.rename(model_path, model_path_new)
        else:
            serializer.validated_data['error'] = 'model file not found'

        # define optimized model name
        optimized_model = os.path.join(BASE_FILE_PATH, 'model/') + file_label + '/optimized/' + model_path_new.split('/').pop()
        optimized_model_url = os.path.join(BASE_FILE_PATH, 'model/') + file_label + '/optimized/'
        optimized_model_url = optimized_model_url + serializer.validated_data['model_file'].name.split('.')[0] \
                              + '_tweaked.' + serializer.validated_data['model_file'].name.split('.')[1]
        optimized_model_url = optimized_model_url[6:]
        # Get num_processes & tolerance
        tolerance = serializer.validated_data['tolerance']
        num_processes = serializer.validated_data['num_processes']
        # Run optimization via subprocess
        res = run_optimization(tsv_path_new, model_path_new, file_label, optimized_model, num_processes, tolerance)
        # os.remove(model_path_new)
        # shutil.rmtree(os.path.join(BASE_FILE_PATH, 'tsv/')+file_label)

        serializer.validated_data['score'] = res.score
        serializer.validated_data['time'] = res.time
        serializer.validated_data['parameters'] = json.dumps(res.parameters)

        if not res.has_error():
            res_model_file = open(res.model)
            serializer.validated_data['optimized_model'] = optimized_model_url
            res_model_file.close()

        serializer.validated_data['error'] = res.error
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        os.remove(tsv_path)
        os.remove(model_path)

        return Response(serializer.data)
