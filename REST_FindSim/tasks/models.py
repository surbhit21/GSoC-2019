from django.db import models
from REST_FindSim.settings import BASE_DIR

# Create your models here.
class Task(models.Model):
    tsv_file    = models.FileField(blank = False, upload_to = "files/tsv/")
    model_file  = models.FileField(blank = False, upload_to = "files/model/")
    score       = models.TextField(blank = True, null = True, editable = False)
    time       = models.TextField(blank = True, null = True, editable = False)
    figure      = models.TextField(blank = True, null = True, editable = False)
