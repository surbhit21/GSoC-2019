from django.contrib import admin

# Register your models here.
from .models import Experiment, Optimization

#  FindSim Experiment tasks
admin.site.register(Experiment)
# FindSim Optimizations tasks
admin.site.register(Optimization)
