# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

"""
def fav(request):
    c = Context({

    })
    t = loader.get_template('types.html')
    return HttpResponse(t.render(c))
"""

"""
def fav(request):

    a = 5
    b = 3
    m = a + b
    hh = ('hh1', 89,)
    hhh = ('hhh', 89,)
    h2 = hh + hhh


    c = Context({'m': m, 'h2':h2})
    t = loader.get_template('types.html')
    return HttpResponse(t.render(c))

"""


def fav(request):
    rem = {}
    rem['cat'] = 'Геральд'

    class fav():
        pass
    fav1 = fav()
    fav1.dog = 'Собака Рем'

    c = Context({'rem': rem,  # вставляем словарь
                 'fav1': fav1  # вставляем класс

    })
    t = loader.get_template('types.html')
    return HttpResponse(t.render(c))