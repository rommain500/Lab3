import datetime
import logging

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from hotel.models import Hotel
from hotel.models import Reserve
from hotel.forms import ReserveCreateForm


logger = logging.getLogger(__name__)


def hotel_list_view(request):
    """ Список всех отелей
        Доступна пагинация
    """
    hotels = Hotel.objects.all()[:10]
    # TODO: join list of reserves
    # TODO: pagination
    kw = {
        'object_list': hotels,
        'reserve_form': ReserveCreateForm,
    }
    return render(request, "hotel/object_list.html", kw)


def hotel_info(request, pk):
    """Получение информации об отеле"""
    try:
        obj = Hotel.objects.get(pk=pk)
    except Hotel.DoesNotExist as e:
        logger.info("Hotel not found: {}".format(e))
        obj = None
    kw = {
        'object': obj,
    }
    return render(request, "hotel/hotel_info.html", kw)


def reserve_hotel(request):
    """Резервирование отеля"""
    form = ReserveCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return JsonResponse({
            "success": True,
        })
    else:
        logger.debug('\n'.join(['"{}"={}'.format(k, v) for k, v in request.POST.items()]))
        logger.debug(form.errors)
        return JsonResponse({
            "success": False,
        })

# TODO: форма удаления резерва


@login_required
def reserve_list_view(request):
    """ Список резеров данного юзера
        Доступна пагинация
    """
    today = datetime.datetime.today()
    reserves = Reserve.objects.select_related('hotel').filter(client=request.user, date_end__gte=today)
    kw = {
        'object_list': reserves,
    }
    return render(request, "hotel/reserve_list.html", kw)
