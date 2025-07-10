from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_detail, name='restaurant_detail'),
]