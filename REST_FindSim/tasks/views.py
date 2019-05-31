from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer
from .runFindSim import runTask

import os
import json


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #parse the path to .tsv file and model file
        tsv_path = 'files/tsv/'+ serializer.validated_data['tsv_file'].name.split('/').pop()
        model_path = 'files/model/'+ serializer.validated_data['model_file'].name.split('/').pop()
        res = runTask(tsv_path,model_path)
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


# Create your views here.
