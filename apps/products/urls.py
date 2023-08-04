from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from products.views import IndexView, CheckoutView, StoreView, ProductDetailView, CustomLoginView

urlpatterns = [
    path('', IndexView.as_view()),
    path('store', StoreView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('checkout', CheckoutView.as_view()),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(template_name='electro/logout.html'), name='logout'),
]
