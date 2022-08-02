
from django.db import models


from authnapp.models import CustomUser


class ClippedLinks(models.Model):
    creator_link = models.ManyToManyField(CustomUser, through='ThroughModel', verbose_name='создатель ссылки')
    original_link = models.URLField(blank=True, null=True, verbose_name='первоначальная ссылка')
    shortened_link = models.URLField(blank=True, null=True, verbose_name='сокращенная ссылка')

    def __str__(self):
        return f'{self.original_link } - {self.shortened_link}'



class ThroughModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default='deleted user')
    link = models.ForeignKey(ClippedLinks, on_delete=models.PROTECT)