from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Calculation, Optimization
from .serializers import CalculationSerializer, OptimizationSerializer
from .run_findSim import run_findSim
from .run_fptimization import run_optimization

import os
import json
import thread
import zipfile
import time


# Create your views here.
class CalculationViewSet(viewsets.ModelViewSet):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #parse the path to .tsv file and model file
        tsv_path = 'files/tsv/'+ serializer.validated_data['tsv_file'].name.split('/').pop()
        model_path = 'files/model/'+ serializer.validated_data['model_file'].name.split('/').pop()
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

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #parse the path to .tsv file and model file
        tsv_path = 'files/tsv/'+ serializer.validated_data['tsv_file'].name.split('/').pop()
        model_path = 'files/model/'+ serializer.validated_data['model_file'].name.split('/').pop()
        file_label = serializer.validated_data['username'] + str(time.time())
        tsv_path_new = 'files/tsv/'+ file_label + serializer.validated_data['tsv_file'].name.split('/').pop()
        model_path_new = 'files/model/'+ file_label + serializer.validated_data['model_file'].name.split('/').pop()

        # Rename the files to avoid collision
        if os.path.exists(tsv_path):
            os.rename(tsv_path, tsv_path_new)
            tsv_path = tsv_path_new
        else:
            serializer.validated_data['error'] = '.tsv files not found'

        if os.path.exists(model_path):
            os.rename(model_path, model_path_new)
            model_path = model_path_new
        else:
            serializer.validated_data['error'] = 'model file not found'

        res = run_optimization(tsv_path, model_path, file_label)
        os.remove(tsv_path)
        os.remove(model_path)

        serializer.validated_data['score'] = res.score
        serializer.validated_data['time'] = res.time
        serializer.validated_data['optimized_model'] = res.model
        serializer.validated_data['error'] = res.error

        serializer.save()
        headers = self.get_success_headers(serializer.data)
        os.remove(tsv_path)
        os.remove(model_path)


        return Response(serializer.data)
