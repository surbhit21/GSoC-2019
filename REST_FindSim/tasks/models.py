from django.db import models
from REST_FindSim.settings import BASE_DIR

# Create your models here.
class Task(models.Model):
    tsv_file    = models.FileField(blank = False, upload_to = "files/tsv/")
    model_file  = models.FileField(blank = False, upload_to = "files/model/")
    score       = models.DecimalField(blank = True, null = True, editable = False, max_digits=20, decimal_places=10)
    time        = models.DecimalField(blank = True, null = True, editable = False, max_digits=20, decimal_places=10)
    figure      = models.TextField(blank = True, null = True, editable = False)
    error       = models.TextField(blank = True, null = True, editable = False)
