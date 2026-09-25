from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    



