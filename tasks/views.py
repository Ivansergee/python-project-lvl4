from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from .models import User, Status
from .forms import UserRegisterForm, StatusCreationForm


class IndexView(TemplateView):
    template_name = 'tasks/index.html'


class CreateUserView(SuccessMessageMixin, CreateView):
    success_url = reverse_lazy('login')
    template_name = 'tasks/users/register.html'
    form_class = UserRegisterForm
    success_message = _('Пользователь успешно зарегистрирован')


class UpdateUserView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users_list')
    template_name = 'tasks/users/update.html'
    form_class = UserRegisterForm
    success_message = _('Пользователь успешно изменен')
    login_url = reverse_lazy('login')
    redirect_field_name = None

    def test_func(self):
        return self.request.user.pk == self.get_object().pk
    
    def handle_no_permission(self):
        messages.error(self.request, _('У вас нет прав для изменения другого пользователя.'))
        return redirect('users_list')


class DeleteUserView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users_list')
    template_name = 'tasks/users/delete.html'
    success_message = _('Пользователь успешно удален')
    login_url = reverse_lazy('login')
    redirect_field_name = None

    def test_func(self):
        return self.request.user.pk == self.get_object().pk
    
    def handle_no_permission(self):
        messages.error(self.request, _('У вас нет прав для изменения другого пользователя.'))
        return redirect('users_list')


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name='tasks/users/login.html'
    success_message = _('Вы залогинены')


class LogoutUserView(LogoutView):
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, _('Вы разлогинены'))
        return response


class UsersListView(ListView):
    template_name = 'tasks/users/users.html'
    model = User
    context_object_name = 'users'


class StatusesListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/statuses/statuses.html'
    model = Status
    context_object_name = 'statuses'

    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')


class CreateStatusView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    success_url = reverse_lazy('statuses_list')
    template_name = 'tasks/statuses/create_status.html'
    form_class = StatusCreationForm
    success_message = _('Статус успешно создан')

    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')


class UpdateStatusView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    success_url = reverse_lazy('statuses_list')
    template_name = 'tasks/statuses/update_status.html'
    form_class = StatusCreationForm
    success_message = _('Статус успешно изменен')
    
    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')


class DeleteStatusView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('statuses_list')
    template_name = 'tasks/statuses/delete_status.html'
    success_message = _('Статус успешно удален')
    
    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')
