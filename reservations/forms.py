from datetime import date
from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """Datefield widget in form"""

    input_type = "date"


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date", "start_time", "num_people"]
        widgets = {
            "date": DateInput(),
            "num_people": forms.NumberInput(
                attrs={"max": 10, "min": 1}
            ),  # Set max and min attributes
        }

    # Code got from: https://docs.djangoproject.com/en/5.0/ref/forms/widgets/
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].widget.attrs.update({"min": date.today()})