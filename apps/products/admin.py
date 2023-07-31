from django.contrib import admin
from django.contrib.admin import TabularInline

from products.models import Product, ProductImages, Category


class ProductImagesInline(TabularInline):
    model = ProductImages
    fields = 'image',
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'title',
    inlines = [ProductImagesInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'title',
