from django.contrib import admin
from .models import Product, Enterprise


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'quantity', 'enterprise')
    search_fields = ('title', 'description')
    list_filter = ('enterprise',)


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'work_hours')
    search_fields = ('name', 'description')
