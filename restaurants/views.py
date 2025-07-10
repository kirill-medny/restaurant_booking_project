from django.shortcuts import render, get_object_or_404
from .models import Restaurant

def restaurant_detail(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant})