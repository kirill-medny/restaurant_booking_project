from django.urls import path

from . import views

app_name = "bookings"

urlpatterns = [
    path("table/<int:table_id>/book/", views.booking_create, name="booking_create"),
    path("my_bookings/", views.user_bookings, name="user_bookings"),
    path(
        "booking/cancel/<int:booking_id>/", views.booking_cancel, name="booking_cancel"
    ),
]
