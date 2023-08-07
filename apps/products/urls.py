from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import IndexView, CheckoutView, StoreView, ProductDetailView, CustomLoginView

urlpatterns = [
    # path('', cache_page(60 * 5, key_prefix='page')(IndexView.as_view())),
    path('', IndexView.as_view()),
    path('store', StoreView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('checkout', CheckoutView.as_view()),
]
