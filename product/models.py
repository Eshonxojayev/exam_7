from django.db import models

# from api.models import Product
# from customers.models import Customers
from .helps import SaveMediaFile, PriceType, WeightType
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    text = models.TextField()
    # customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    search = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    top_comment = models.TextField()

    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['-created_date']),
        ]

    def __str__(self):
        return self.text[:10]


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMediaFile.category_image_path)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    search = models.TextField(max_length=100)

    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['-created_date']),
        ]

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    manufacturer_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=SaveMediaFile.product_image_path)
    price = models.FloatField()
    price_type = models.CharField(max_length=10, choices=PriceType.choices, default=PriceType.usd)
    rating = models.FloatField(default=0)
    max_weight = models.FloatField(default=0)
    max_weight_type = models.CharField(max_length=10, choices=WeightType.choices, default=WeightType.kg)
    min_weight = models.FloatField(default=0)
    min_weight_type = models.CharField(max_length=10, choices=WeightType.choices, default=WeightType.kg)
    comments = models.ManyToManyField(Comment, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    search = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    # top_products = models.ManyToManyField(null=True, blank=True)



    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['-created_date']),
        ]

    def __str__(self):
        return self.title


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_number = models.IntegerField(default=1)
    shipping_price = models.FloatField(default=3)
    total_price = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    search = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)




    class Meta:
        ordering = ['-product_number']
        indexes = [
            models.Index(fields=['-product_number']),
        ]
