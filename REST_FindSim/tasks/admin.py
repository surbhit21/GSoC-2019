from django.contrib import admin

# Register your models here.
from .models import Calculation, Optimization

admin.site.register(Calculation)
admin.site.register(Optimization)
