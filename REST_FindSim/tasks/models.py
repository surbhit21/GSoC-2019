from django.db import models
from REST_FindSim.settings import BASE_DIR

# Create your models here.
class Calculation(models.Model):
    username    = models.TextField(blank = False, default = 'admin_HC')
    tsv_file    = models.FileField(blank = False, upload_to = "files/tsv/")
    model_file  = models.FileField(blank = False, upload_to = "files/model/")
    score       = models.DecimalField(blank = True, null = True, editable = False, max_digits=20, decimal_places=10)
    time        = models.DecimalField(blank = True, null = True, editable = False, max_digits=20, decimal_places=10)
    figure      = models.TextField(blank = True, null = True, editable = False)
    error       = models.TextField(blank = True, null = True, editable = False)

class Optimization(models.Model):
    username        = models.TextField(blank = False, default = 'admin_HC')
    tsv_files       = models.FileField(blank = False, upload_to = "files/tsv/")
    model_file      = models.FileField(blank = False, upload_to = "files/model/")
    parameters      = models.TextField(blank = False, null = False)

    score           = models.TextField(blank = True, null = True, editable = False)
    time            = models.DecimalField(blank = True, null = True, editable = False, max_digits=20, decimal_places=10)
    optimized_model = models.FileField(blank = True, null = True,editable = False)

    finished        = models.BooleanField(blank = True, null = True, default = False, editable = False)
    error           = models.TextField(blank = True, null = True, editable = False)
