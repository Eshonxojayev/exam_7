from django.db import models
# from .help import SaveMediaFile

class Chef(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    search = models.CharField(max_length=100)
    birth_date = models.DateField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        ordering = ['-birth_date']
        indexes = [
            models.Index(fields=['-birth_date']),
        ]

    def __str__(self):
        return self.name

class Cooker(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    search = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        ordering = ['-birth_date']
        indexes = [
            models.Index(fields=['-birth_date']),
        ]

    def __str__(self):
        return self.name

class Assistantcook(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    search = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(max_length=100)
    status = models.CharField(max_length=100)

    class Meta:
        ordering = ['-birth_date']
        indexes = [
            models.Index(fields=['-birth_date']),
        ]

    def __str__(self):
        return self.name

