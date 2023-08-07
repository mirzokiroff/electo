from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField

from users.models import User


class UserRegisterForm(ModelForm):
    confirm_password = CharField(max_length=255)

    class Meta:
        model = User
        fields = 'email', 'password', 'confirm_password'

    def clean_password(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirm_password")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "The two password fields didn’t match.",
                code="password_mismatch",
            )
        return make_password(password1)
