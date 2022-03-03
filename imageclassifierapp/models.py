from django.db import models

# Create your models here.

class ImgClass(models.Model):
    img_path = models.CharField(max_length=100)
    img_classifier = models.CharField(max_length=100)