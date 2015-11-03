# coding: utf-8

from django.shortcuts import render_to_response
from practice_keyfire_ru.settings import page_title

title = page_title


def special_case_2003(request):
    return render_to_response('index.html', {'title': title})


def year_archive(request):
    return render_to_response('index.html', {'title': title})


def month_archive(request):
    return render_to_response('index.html', {'title': title})


def article_detail(request):
    return render_to_response('index.html', {'title': title})