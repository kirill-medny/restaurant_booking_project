from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from restaurants.models import Table

from .forms import BookingForm
from .models import Booking


@login_required
def booking_create(request, table_id):
    table = get_object_or_404(Table, pk=table_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=Booking(table=table))
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.table = table
            booking.save()
            return redirect(
                "bookings:user_bookings"
            )  # Перенаправление в личный кабинет
    else:
        form = BookingForm(initial={"table": table})
    return render(request, "bookings/booking_form.html", {"form": form, "table": table})


@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "bookings/user_bookings.html", {"bookings": bookings})


@login_required
def booking_cancel(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    booking.delete()
    return redirect("bookings:user_bookings")
