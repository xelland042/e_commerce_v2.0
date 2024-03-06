from django.urls import path

from products.views import index, product, store

urlpatterns = [
    path('', index),
    path('product/<int:product_id>/', product),
    path('store/', store),
]
