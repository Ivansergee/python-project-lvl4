from re import T
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from .models import User, Status, Label, Task
from .forms import UserRegisterForm, StatusCreationForm, LabelCreationForm, TaskCreationForm
from .filters import TaskFilter


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
    success_message = _('Пользователь успешно изменён')
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
    success_message = _('Пользователь успешно удалён')
    login_url = reverse_lazy('login')
    redirect_field_name = None

    def test_func(self):
        return self.request.user.pk == self.get_object().pk
    
    def handle_no_permission(self):
        messages.error(self.request, _('У вас нет прав для изменения другого пользователя.'))
        return redirect('users_list')
    
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, _('Невозможно удалить пользователя, связанного с существующими задачами.'))
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
    success_message = _('Статус успешно изменён')
    
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


class LabelsListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/labels/labels.html'
    model = Label
    context_object_name = 'labels'

    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')


class CreateLabelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    success_url = reverse_lazy('labels_list')
    template_name = 'tasks/labels/create_label.html'
    form_class = LabelCreationForm
    success_message = _('Метка успешно создана')

    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')


class UpdateLabelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    success_url = reverse_lazy('labels_list')
    template_name = 'tasks/labels/update_label.html'
    form_class = LabelCreationForm
    success_message = _('Метка успешно изменена')
    
    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')


class DeleteLabelView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    success_url = reverse_lazy('labels_list')
    template_name = 'tasks/labels/delete_label.html'
    success_message = _('Метка успешно удалена')
    
    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')
    
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, _('Метка используется в задаче, удаление невозможно.'))
            return redirect('labels_list')


class TasksListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/tasks/tasks.html'
    model = Task
    context_object_name = 'tasks'

    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TaskFilter(self.request.GET, user=self.request.user, queryset=self.get_queryset())
        return context


class CreateTaskView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    success_url = reverse_lazy('tasks_list')
    template_name = 'tasks/tasks/create_task.html'
    form_class = TaskCreationForm
    success_message = _('Задание успешно создано')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')


class UpdateTaskView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('tasks_list')
    template_name = 'tasks/tasks/update_task.html'
    form_class = TaskCreationForm
    success_message = _('Задание успешно изменено')
    
    def handle_no_permission(self):
        messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
        return redirect('login')


class DeleteTaskView(AccessMixin, SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks_list')
    template_name = 'tasks/tasks/delete_task.html'
    success_message = _('Задание успешно удалено')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('Выполните вход для просмотра данной страницы'))
            return redirect('login')
        if not request.user.pk == self.get_object().author.pk:
            messages.error(self.request, _('Удалить задачу может только её автор.'))
            return redirect('tasks_list')
        return super().dispatch(request, *args, **kwargs)


class TaskView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/tasks/task.html'
    context_object_name = 'task'
