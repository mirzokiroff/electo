from django.core.cache import cache
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from root import settings
from users.forms import UserRegisterForm
from users.tasks import send_to_gmail


class RegisterView(CreateView):
    template_name = 'electro/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('activate')

    def form_valid(self, form):
        user = form.save(commit=False)
        send_to_gmail.apply_async(args=[user.email], countdown=5)
        self.object = user
        cache.set(f'user:{user.email}', user, timeout=settings.CACHE_TTL)
        # {
        #     'user:ganiyevuz@mail.ru': user
        # }
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return super().form_invalid(form)


class ActivateUserView(TemplateView):
    template_name = 'electro/activate_user.html'

    def post(self, request, *args, **kwargs):
        code = request.POST.get('code')
        if code and (email := cache.get(f'{settings.CACHE_KEY_PREFIX}:{code}')):
            if user := cache.get(f'user:{email}'):
                # cache.delete(f'{settings.CACHE_KEY_PREFIX}:{code}')
                # cache.delete(f'user:{email}')
                user.save()
                return HttpResponse('User is successfully activated')
        return HttpResponse('Code is expired or invalid')
