from rest_framework import serializers
from .models import Calculation, Optimization

class CalculationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calculation
        fields = ('username','tsv_file','model_file','score','time','figure','error')

class OptimizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Optimization
        fields = ('username', 'tsv_files', 'model_file', 'parameters', 'score','time','optimized_model','error')
