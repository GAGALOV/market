from django.contrib import admin
from .models import Product, Basket

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('product','quantity')