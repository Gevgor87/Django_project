from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product-details/<int:id>', views.product_details, name = 'product_details'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('basket/', views.basket, name="basket"),
    path('delete_product/', views.delete_product, name="delete_product")

]