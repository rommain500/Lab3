from logging import getLogger

from django.shortcuts import render
from django.shortcuts import HttpResponsePermanentRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.decorators.http import require_POST

from sauth.forms import RegisterClient


logger = getLogger(__name__)


def register(request):
    """ Регистрация пользователя или отображение формы регистрации
        * Регистрация работает только для неавторизованных пользователей
        * Если пользователь успешно зарегистрирован, он будет авторизован и редиректен на урл /
    """
    form = RegisterClient(request.POST or None)
    if request.method == "POST" and not request.user.is_authenticated():
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password1'])
            login(request, user)
            return HttpResponsePermanentRedirect('/')
    kw = {
        "form": form,
    }
    return render(request, "sauth/register.html", kw)


@require_POST
def logout_handler(request):
    """ Логаут пользователя

        :form redirect_to: урл на который сделать редирект после логаута, по умолчанию - текущая страница
    """
    if request.user.is_authenticated():
        logout(request)
    redirect_to = request.POST.get('redirect_to', '/')
    return HttpResponsePermanentRedirect(redirect_to)
