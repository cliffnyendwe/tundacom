from django.urls import path
from . import views
from . views import *

urlpatterns = [
  path("bookings/", views.bookings, name="bookings"),
  path("customer-bookings/", views.customer_bookings, name="customer-bookings"),
  path("new-hotel/", NewHotel.as_view(), name="new-hotel"),
  path("hotel-list/", views.hotel_list, name="hotel-list"),
  path("hotel/<int:pk>/details/", views.hotel_details, name="hotel-details"),
  path("hotels/", views.hotels, name="hotels"),
  path("book-room/", BookRoom.as_view(), name="book-room"),
  path("rooms-test/", views.rooms_test, name="rooms-test"),
  path("booking-test/", views.booking_test, name="booking-test"),
  path("update/<int:pk>/hotel/", UpdateHotel.as_view(), name="update-hotel"),
  path("delete/<int:pk>/hotel/", views.delete_hotel, name="delete-hotel"),
  
]
