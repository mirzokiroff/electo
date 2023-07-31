from django.contrib import admin
from django.urls import path

from products.views import IndexView, CheckoutView, StoreView, ProductDetailView

urlpatterns = [
    path('', IndexView.as_view()),
    path('store', StoreView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('checkout', CheckoutView.as_view()),
]
