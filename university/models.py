from django.db import models


# Create your models here.
class UniversityModel(models.Model):
    university_name = models.CharField(max_length=100)
    university_link = models.TextField()
