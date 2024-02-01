from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_per_one', 'category')
    list_filter = ('category',)  # Добавляем фильтр по категории
    search_fields = ('name', 'description')  # Добавляем поля для поиска
