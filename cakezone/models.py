from django.db import models
from django.contrib.auth.models import User


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


class Profile(models.Model):
    photo = models.ImageField(upload_to='profile/%Y/%m/%d/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)



# from django.db import models
# from django.contrib.auth.models import User
#
# class Profile(models.Model):
#     class Meta:
#         verbose_name = 'Profile'
#
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     date_of_birth = models.DateField(null=True, blank=True)
#
# class Location(models.Model):
#     location = models.CharField(max_length=50)
#     def save_location(self):
#         self.save()
#         return self.location
#
# class Category(models.Model):
#     category = models.CharField(max_length=50)
#     title = models.CharField(max_length=50, blank=False)
#
#     def __str__(self):
#         return self.title
#
#
# class Product(models.Model):
#     image = models.ImageField(default='default.jpg', upload_to='products')
#     name = models.CharField(max_length=50, blank=False)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.name
#
# class Rate(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     rate = models.DecimalField(max_digits=5, decimal_places=2)
#
#     def __str__(self):
#         return self.product
