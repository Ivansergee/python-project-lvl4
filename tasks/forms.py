from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = _('<ul><li>Ваш пароль должен содержать как минимум 3 символа.</li></ul>')

    first_name = forms.CharField(label=_('Имя'))
    last_name = forms.CharField(label=_('Фамилия'))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
        )
