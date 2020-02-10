import django_filters
from .models import Client


class ClientsFilter(django_filters.FilterSet):

    CHOISES = (
        ('first, desc', 'First name, desc'),
        ('first, asc', 'First name, asc'),
        ('last, desc', 'Last name, desc'),
        ('last, asc', 'Last name, asc'),
        ('age, desc', 'Age, desc'),
        ('age, asc', 'Age, asc'),

    )
    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOISES, method='filter_by_order')

    def filter_by_order(self, queryset, name, value):
        expression = 'last'
        if value == 'first, desc':
            expression = '-first'
        elif value == 'first, asc':
            expression = 'first'
        elif value == 'last, desc':
            expression = '-last'
        elif value == 'last, asc':
            expression = 'last'
        elif value == 'age, desc':
            expression = '-birth'
        elif value == 'age, asc':
            expression = 'birth'

        return queryset.order_by(expression)

    class Meta:
        model = Client
        fields = ()


