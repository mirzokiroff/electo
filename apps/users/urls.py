from django.contrib.auth.views import LogoutView
from django.urls import path

from products.views import CustomLoginView
from users.views import RegisterView, ActivateUserView

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(template_name='electro/logout.html'), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('activate', ActivateUserView.as_view(), name='activate')
]
