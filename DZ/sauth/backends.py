""" Кастомные бэкенды для авторизации
"""
from uuid import uuid4

from sauth.models import Client


class SMSBackendAbstract(object):

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None

    def authenticate(self, uid=None):
        # username = uuid4()[:30]
        # TODO: проверять что такой код был отправлен
        # TODO: отдельная страница создания кодов
        if uid:
            try:
                return Client.objects.get(pk=uid)
            except Client.DoesNotExist:
                pass
        return None
