from django.db import models
from REST_FindSim.settings import BASE_DIR

# Create your models here.
class Calculation(models.Model):
    # Input
    username    = models.TextField(blank = False, default = 'admin_HC')
    tsv_file    = models.FileField(blank = False, upload_to = "files/tsv/")
    model_file  = models.FileField(blank = False, upload_to = "files/model/")
    # Output
    score       = models.DecimalField(blank = True, null = True, editable = False, max_digits=20, decimal_places=10)
    time        = models.DecimalField(blank = True, null = True, editable = False, max_digits=20, decimal_places=10)
    figure      = models.TextField(blank = True, null = True, editable = False)
    error       = models.TextField(blank = True, null = True, editable = False)

class Optimization(models.Model):
    # Input
    username        = models.TextField(blank = False, default = 'admin_HC')
    tsv_files       = models.FileField(blank = False, upload_to = "files/tsv/")
    model_file      = models.FileField(blank = False, upload_to = "files/model/")
    num_processes   = models.DecimalField(blank = True, default = 2, max_digits=3, decimal_places=0)
    tolerance       = models.DecimalField(blank = True, default = 1e-4, max_digits=10, decimal_places=9)
    # Output
    parameters      = models.TextField(blank = False, null = False, editable = False)
    score           = models.TextField(blank = True, null = True, editable = False)
    time            = models.DecimalField(blank = True, null = True, editable = False, max_digits=20, decimal_places=10)
    optimized_model = models.FileField(blank = True, null = True,editable = False)
    error           = models.TextField(blank = True, null = True, editable = False)
