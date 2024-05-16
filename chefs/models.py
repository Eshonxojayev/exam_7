from django.db import models
# from .help import SaveMediaFile

class Chef(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    search = models.CharField(max_length=100)
    birth_date = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cooker(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    search = models.CharField(max_length=100)
    birth_date = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Assistantcook(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    search = models.CharField(max_length=100)
    birth_date = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

