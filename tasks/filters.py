from django.utils.translation import gettext_lazy as _
from django.forms import CheckboxInput

import django_filters
from .models import Task, Label


class TaskFilter(django_filters.FilterSet):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)


    tags = django_filters.ModelChoiceFilter(label=_('Метка'), queryset=Label.objects.all())
    self_tasks = django_filters.BooleanFilter(
        label=_('Только свои задачи'),
        field_name='author',
        widget=CheckboxInput,
        method='filter_self_tasks'
        )

    class Meta:
        model = Task
        fields = [
            'status',
            'executor',
        ]
    
    def filter_self_tasks(self, queryset, name, value):
        if value is True:
            user = self.user.pk
            qs = queryset.filter(author=user)
            return qs
        return queryset
