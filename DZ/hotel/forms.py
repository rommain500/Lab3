from django import forms
from django.forms import widgets

from hotel.models import Reserve


class ReserveCreateForm(forms.ModelForm):

    class Meta:
        model = Reserve
        fields = (
            'date_start',
            'date_end',
            'person_amount',
            'hotel',
            'client',
        )
        widgets = {
            'person_amount': widgets.NumberInput,
            'hotel': widgets.HiddenInput,
            'client': widgets.HiddenInput,
        }
