from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from bookings.forms import BookingForm
from bookings.models import Booking

from .models import Restaurant


def restaurant_detail(request):
    restaurant = Restaurant.objects.first()
    if not restaurant:
        return render(request, "restaurants/no_restaurant.html")
    return render(
        request, "restaurants/restaurant_detail.html", {"restaurant": restaurant}
    )  # Убедитесь, что restaurant передается


@login_required
def booking_create(request, table_id):  # Добавьте аргумент table_id
    from bookings.models import Table

    table = get_object_or_404(Table, pk=table_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=Booking(table=table))
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.table = table
            booking.save()
            return redirect("user_bookings")  # Перенаправление в личный кабинет
    else:
        form = BookingForm(initial={"table": table})
    return render(request, "bookings/booking_form.html", {"form": form, "table": table})
