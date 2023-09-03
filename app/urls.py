from django.urls import path

from . import views


urlpatterns = [
    path('customers', views.customers, name='customers'),
    path('customer/<slug:slug>', views.customer, name='customer'),
    
    path('managers', views.managers, name='managers'),
    path('manager/<slug:slug>', views.manager, name='manager'),
    
    path('products', views.products, name='products'),
    path('product/<slug:slug>', views.product, name='product'),
    
    path('delivery_crews', views.delivery_crews, name='delivery_crews'),
    path('delivery_crew/<slug:slug>', views.delivery_crew, name='delivery_crew'),
    
    path('cart/<int:arg>', views.cart, name='cart'),
    
]
