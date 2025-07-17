from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from bookings.forms import BookingForm
from bookings.models import Booking

from .forms import ContactForm
from .models import AboutRestaurant, Restaurant


def about_restaurant_view(request):
    restaurant = Restaurant.objects.first()
    about_info = None
    if restaurant:
        about_info = AboutRestaurant.objects.filter(restaurant=restaurant).first()
    return render(
        request,
        "restaurants/about_restaurant.html",
        {"restaurant": restaurant, "about_info": about_info},
    )


def restaurant_detail(request):
    restaurant = Restaurant.objects.first()
    contact_form = ContactForm()  # Создайте экземпляр формы
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Обработка формы обратной связи (например, отправка email)
            print("Contact form submitted:", contact_form.cleaned_data)
            # Можно добавить перенаправление или сообщение об успехе
            return redirect(
                "restaurants:restaurant_detail"
            )  # Перенаправляем на ту же страницу после отправки

    return render(
        request,
        "restaurants/restaurant_detail.html",
        {
            "restaurant": restaurant,
            "contact_form": contact_form,  # Передайте форму в контекст
        },
    )


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
