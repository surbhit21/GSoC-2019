from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('tsv_file','model_file','score','time','figure','error')
