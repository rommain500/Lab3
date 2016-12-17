from django.conf.urls import url

from hotel.views import hotel_list_view
from hotel.views import reserve_list_view
from hotel.views import reserve_hotel
from hotel.views import hotel_info


urlpatterns = [
    url('^reserve/list/$', reserve_list_view, name='reserve_list'),
    url('^reserve/$', reserve_hotel, name='reserve'),
    url('^hotel/(?P<pk>\d+)/$', hotel_info, name='hotel_info'),
    url('^', hotel_list_view, name='main'),
]
