from django.contrib.auth.models import User
from django.db.models import *


class Image(Model):

    image = ImageField(null=True, blank=True)
    name = CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(Model):

    CATEGORY = (
        ('Fruit', 'Fruit'),
        ('Vegetables', 'Vegetables')

    )

    name = CharField(max_length=50, null=True)
    category = CharField(max_length=100, null=True, choices=CATEGORY)
    price = FloatField(null=True)
    image = ForeignKey(Image, null=True, on_delete=SET_NULL)

    def __str__(self):
        return self.name


class Customer(Model):

    first_name = CharField(max_length=100, null=True)
    last_name = CharField(max_length=100, null=True)
    email = EmailField(null=True)
    phone = CharField(max_length=50, null=True)
    address = CharField(max_length=100, null=True)
    city = CharField(max_length=50, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Order(Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    
    status = CharField(max_length=100, null=True, choices=STATUS)
    date_created = DateTimeField(auto_now_add=True, null=True)
    customer = ForeignKey(Customer, null=True, on_delete=SET_NULL)
    product = ForeignKey(Product, null=True, on_delete=SET_NULL)

    def __str__(self):
        return self.status
