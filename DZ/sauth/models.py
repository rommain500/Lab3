
from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    RU_LANG = 'RU'
    EN_LANG = 'EN'
    LANG_CHOICES = (
        (RU_LANG, 'Русский'),
        (EN_LANG, 'English'),
    )
    language = models.CharField(
        verbose_name=u'Язык',
        max_length=16,
        choices=LANG_CHOICES,
        default=RU_LANG,
    )
