from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'auth_user'


class Status(models.Model):
    name = models.CharField(_('Имя'), max_length=100, unique=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(_('Имя'), max_length=100, unique=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(_('Имя'), max_length=150, unique=True)
    description = models.TextField(_('Описание'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name=_('Статус'), related_name='statuses')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('Автор'), related_name='authors')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('Исполнитель'), related_name='executors')
    labels = models.ManyToManyField(Label, through='LabelTask', through_fields=('task', 'label'), verbose_name=_('Метки'), blank=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.name


class LabelTask(models.Model):
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
