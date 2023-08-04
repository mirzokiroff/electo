from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView, DetailView

from products.models import Product


class IndexView(ListView):
    template_name = 'electro/index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     data = super().get_context_data(object_list=object_list, **kwargs)
    #     data['hhhhh'] = Product.objects.all()
    #     return data


class ProductDetailView(DetailView):
    template_name = 'electro/product.html'
    queryset = Product.objects.all()
    context_object_name = 'product'


class StoreView(TemplateView):
    template_name = 'electro/store.html'


class CheckoutView(TemplateView):
    template_name = 'electro/checkout.html'


class CustomLoginView(LoginView):
    template_name = 'electro/login.html'
