from django.urls import path
from .views import *


urlpatterns = [
    path('', log, name='log'),
    path('register/', register, name='register'),
    path('create_customer/', create_customer, name='create_customer'),
    path('create_order/<str:pk>', create_order, name='create_order'),
    path('buyProduct/<str:pk>', buyProduct, name='buyProduct'),
    path('update_order/<str:pk>', update_order, name='update_order'),
    path('delete_order/<str:pk>', delete_order, name='delete_order'),
    path('products/', products, name='products'),
    path('customer/<str:pk>', customer, name='customer'),
    path('home/', home, name='home'),
    path('navbar/', navbar, name='navbar'),
    path('logout/', logoutUser, name='logoutUser'),
    path('base/', base, name='base'),
    path('user/', userPage, name='user')
]