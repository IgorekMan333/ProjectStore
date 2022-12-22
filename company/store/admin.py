from django.contrib.admin import *
from .models import Image, Product, Customer, Order


class ProductAdmin(ModelAdmin):

    list_display = ['name', 'category', 'price', 'image']


class CustomerAdmin(ModelAdmin):

    list_display = ['first_name', 'last_name', 'city', 'phone']


class OrderAdmin(ModelAdmin):
    
    list_display = ['customer', 'product', 'date_created', 'status']


site.register(Product, ProductAdmin)
site.register(Image)
site.register(Customer, CustomerAdmin)
site.register(Order, OrderAdmin)
