# coding: utf-8

from django.http import HttpResponse
from django.template import Context, Template, loader

"""
def details(request):
    return HttpResponse('Заработало, Ура!')


def details(request):
    my_dict = {'fav_color': 'blue'}
    my_template = 'Мой любимый цвет {{ fav_color }}'
    c = Context(my_dict)
    t = Template(my_template)
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)

"""


def details(request):
    c = Context({'fav_color': ['green', 'red', 'blue']})
    t = loader.get_template('inner\example.html')
    return HttpResponse(t.render(c))


