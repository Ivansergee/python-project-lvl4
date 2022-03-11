from dataclasses import fields
from django.utils.translation import gettext_lazy as _
from django import forms

import django_filters
from django_filters import widgets
from .models import Task


class TaskFilter(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(label=_('Только свои задачи'), widget=forms.BooleanField())

    class Meta:
        model = Task
        fields = [
            'status',
            'executor',
            'tags'
        ]
