from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingsAdmin(admin.ModelAdmin):
    search_fields = ["user_name"]
    list_display = ("user", "date", "start_time", "email")
    list_filter = ["date"]
