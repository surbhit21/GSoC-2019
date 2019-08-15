from django.contrib import admin

# Register your models here.
from .models import Experiment, Optimization

admin.site.register(Experiment)
admin.site.register(Optimization)
