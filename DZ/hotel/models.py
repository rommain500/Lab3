from django.db import models
from django.utils import timezone

from sauth.models import Client


class Picture(models.Model):
    path = models.FileField(
        verbose_name=u"Фотография",
    )

    class Meta:
        db_table = 'picture'


class Hotel(models.Model):
    name = models.CharField(
        verbose_name=u"Название отеля",
        max_length=255,
    )
    pictures = models.ManyToManyField(
        Picture,
        verbose_name=u"Фотографии отеля",
        db_table='hotel_pictures',
    )
    description = models.TextField(
        verbose_name=u"Описание"
    )

    def __unicode__(self):
        return "<Hotel: {}>".format(self.name)

    class Meta:
        db_table = 'hotel'


class Reserve(models.Model):
    hotel = models.ForeignKey(Hotel)
    client = models.ForeignKey(Client)
    date_start = models.DateTimeField(
        verbose_name=u"Дата начала бронирования",
        default=timezone.now,
    )
    date_end = models.DateTimeField(
        verbose_name=u"Дата окончания бронирования",
        default=timezone.now,
    )
    person_amount = models.PositiveIntegerField(
        verbose_name=u"Кол-во персон",
        default=1,
    )

    class Meta:
        db_table = 'reserve'
