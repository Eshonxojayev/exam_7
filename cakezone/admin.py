from django.contrib import admin
from .models import Category, Product, Rate

admin.site.register(Category)
admin.site.register(Rate)



# from django.contrib import admin
# from .models import Category, Product, Rate, Profile
#
# admin.site.register(Category)
# admin.site.register(Rate)
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'price', 'rating']
#     raw_id_fields = ['category']
#
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'gender', 'age', 'address']
#     raw_id_fields = ['user']
#     search_fields = ['user']
#     list_filter = ['gender', 'age', 'address']
# #
# # @admin.register(Rate)
# # class RateAdmin(admin.ModelAdmin):
# #     list_display = ['user', 'rate']
# #     raw_id_fields = ['user']
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     raw_id_fields = ['name']
