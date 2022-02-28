from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    class Meta:
        db_table = 'auth_user'


class Status(models.Model):
    name = models.CharField(_('Имя'), max_length=100, unique=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)


class Label(models.Model):
    name = models.CharField(_('Имя'), max_length=100, unique=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)


class Task(models.Model):
    name = models.CharField(_('Имя'), max_length=150, unique=True)
    description = models.TextField(_('Описание'))
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Label)