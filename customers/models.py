from django.db import models
from .help import SaveMediaFile


class Country(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    search = models.CharField(max_length=50)

    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['-created_date']),
        ]

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    search = models.CharField(max_length=50)

    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['-created_date']),
        ]

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['-created_date']),
        ]

    def __str__(self):
        return self.name


class Customers(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to=SaveMediaFile.customer_image_path)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    user_id = models.CharField(max_length=20, blank=True)
    search = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        ordering = ['-user_id']
        indexes = [
            models.Index(fields=['-user_id']),
        ]

    def __str__(self):
        return self.username

    def full_name(self):
        return f"{self.first_name} {self.last_name}"



