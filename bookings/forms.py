from django import forms
from django.core.exceptions import ValidationError

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date", "time", "number_of_guests", "comments"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")
        number_of_guests = cleaned_data.get("number_of_guests")
        table = self.instance.table  # Получаем столик из инстанса формы

        if date and time and table:
            # Проверяем, есть ли уже бронирования на это время для этого столика
            existing_bookings = Booking.objects.filter(
                table=table, date=date, time=time
            )
            if self.instance.pk:
                existing_bookings = existing_bookings.exclude(
                    pk=self.instance.pk
                )  # Исключаем текущую бронь при редактировании

            if existing_bookings.exists():
                raise ValidationError(
                    "This table is already booked for this date and time."
                )

        return cleaned_data
