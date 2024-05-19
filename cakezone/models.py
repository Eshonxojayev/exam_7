from django.db import models
from django.contrib.auth.models import User


from django.db import models

class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Category(models.Model):
    title = models.CharField(max_length=250, blank=False)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    photo = models.ImageField(upload_to='products/', unique=True)
    name = models.CharField(max_length=250, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    rating = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rate')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rate = models.IntegerField()

    def __str__(self) -> str:
        return self.product



