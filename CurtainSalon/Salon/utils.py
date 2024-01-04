from .models import *


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Услуги', 'url_name': 'service'},
        {'title': 'Отзывы', 'url_name': 'comment'},
        {'title': 'Регистрация', 'url_name': 'register'}
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        type = ProductType.objects.all()
        context['menu'] = menu
        context['type'] = type
        if 'type_selected' not in context:
            context['type_selected'] = 0
        return context
