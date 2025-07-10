from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('restaurants.urls')), # Главный URL ведет к ресторанам
]