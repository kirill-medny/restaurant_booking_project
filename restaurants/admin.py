from django.contrib import admin

from .models import Restaurant, Table


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "owner")


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        "table_number",
        "restaurant",
        "capacity",
        "x_coordinate",
        "y_coordinate",
    )
