from django.contrib import admin
from .models import Category, Product, Rate

# admin.site.register(Category)
# admin.site.register(Rate)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    raw_id_fields = ('category',)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('product', 'rate')
    search_fields = ('product', 'rate')
    raw_id_fields = ('product',)