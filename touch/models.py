from django.db import models

class Touch(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    massage=models.TextField()

# Create your models here.
