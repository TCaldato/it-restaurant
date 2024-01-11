from datetime import date
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """Datefield widget in form
    """
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'date', 'start_time', 'email']
        widgets = {
            'date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'min': date.today()
        })