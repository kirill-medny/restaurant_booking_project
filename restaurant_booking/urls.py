from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bookings/", include("bookings.urls", namespace="bookings")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("", include("restaurants.urls", namespace="restaurants")),  # Главный URL ведет к ресторанам
]

