from django.contrib import admin
from . models import Hotel, Booking, Rating
admin.site.register(Hotel)
admin.site.register(Rating)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["user", "hotel", "booking_option", "rooms_booked"]