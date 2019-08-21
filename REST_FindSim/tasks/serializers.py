from rest_framework import serializers
from .models import Experiment, Optimization

# FindSim experiments:
class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experiment
        fields = ('username','tsv_file','model_file','score','time','figure','error')

# FindSim optimization tasks:
class OptimizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Optimization
        fields = ('username', 'tsv_files', 'model_file', 'num_processes', 'tolerance', 'parameters', 'score','time','optimized_model','error')
