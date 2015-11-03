# coding: utf-8
from django.db import models


class Saas(models.Model):
    class Meta:
        db_table = 'app_saas_saas'

    date = models.DateTimeField(verbose_name="Дата", blank=True, null=True)
    title = models.CharField(verbose_name="Заголовок", max_length=128, blank=True, unique=True)
    text = models.TextField(verbose_name="Текст", blank=True, null=True)
    tip = models.TextField()