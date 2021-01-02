from django.db import models

# Create your models here.
class Guncelkonular(models.Model):
    resimadi=models.CharField(max_length=100)
    