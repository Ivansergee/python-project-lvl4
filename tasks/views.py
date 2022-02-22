from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from .models import User
from .forms import UserRegisterForm


class IndexView(TemplateView):
    template_name = 'tasks/index.html'


class CreateUserView(SuccessMessageMixin, CreateView):
    success_url = reverse_lazy('login')
    template_name = 'tasks/register.html'
    form_class = UserRegisterForm
    success_message = _('Пользователь успешно зарегистрирован')


class UpdateUserView(SuccessMessageMixin, UpdateView):
    success_url = reverse_lazy('login')
    template_name = 'tasks/register.html'
    form_class = UserRegisterForm
    success_message = _('Пользователь успешно изменен')


class DeleteUserView(SuccessMessageMixin, DeleteView):
    success_url = reverse_lazy('login')
    template_name = 'tasks/register.html'
    form_class = UserRegisterForm
    success_message = _('Пользователь успешно зарегистрирован')


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name='tasks/login.html'
    success_message = _('Вы залогинены')


class LogoutUserView(LogoutView):
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, _('Вы разлогинены'))
        return response


class UsersListView(ListView):
    template_name = 'tasks/users.html'
    model = User
    context_object_name = 'users'