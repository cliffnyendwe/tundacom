from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from hotel.forms import HotelForm, BookingForm, RatingForm, UpdateHotelForm
from . models import *
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.db.models import Q
# Create your views here.
def hotel_list(request):
	q = request.GET.get('q') if request.GET.get('q') != None else ''
	hotels = Hotel.objects.filter(Q(name__icontains=q) | Q(location__icontains=q) | Q(price__icontains=q))
	context = {
		"hotels": hotels
	}
	return render(request, "hotel/hotel-list.html", context)

def rooms_test(request):
	hotels = Hotel.objects.all()
	context = {
		"hotels": hotels
	}

	return render(request, "hotel/rooms-test.html", context)

def booking_test(request):
	form = BookingForm()

	context = {
		"form": form
	}


	if request.method == "POST":
		hotel = request.POST.get("hotel")
		booking_option = request.POST.get("booking_option")
		rooms_booked = request.POST.get("rooms_booked")

		booking = Booking()
		booking.hotel = hotel
		booking.booking_option = booking_option
		booking.rooms_booked = rooms_booked
		booking.user = request.user

		print(f'Name: ${hotel} Rooms Booked: ${rooms_booked} Booking Option: ${booking_option}')

		booking.save()
		return redirect("customer-bookings")

	return render(request, "hotel/booking-test.html", context)

def hotels(request):
	hotels = Hotel.objects.all()
	context = {
		"hotels": hotels
	}
	return render(request, "hotel/hotels.html")

def bookings(request):
	bookings = Booking.objects.all()
	return render(request, "hotel/bookings.html", {"bookings": bookings})

def hotel_details(request, pk):
	hotel = Hotel.objects.get(id=pk)
	ratings = Rating.objects.filter(hotel=hotel)
	new_rating = None
	if request.method == 'POST':
		rating_form = RatingForm(data=request.POST)
		if rating_form.is_valid():

            # Create Comment object but don't save to database yet
			new_rating = rating_form.save(commit=False)
            # Assign the current post to the comment
			new_rating.hotel = hotel
            # Save the comment to the database
			new_rating.save()
	else:
		rating_form = RatingForm()

	context = {
		"hotel": hotel,
		"ratings": ratings,
		"new_rating": new_rating,
		"rating_form": rating_form
	}
	return render(request, "hotel/hotel-details.html", context)

def customer_bookings(request):
	bookings = Booking.objects.filter(user=request.user)
	return render(request, "customer-bookings.html", {"bookings": bookings})

class NewHotel(CreateView):
  model = Hotel
  #fields = "__all__"
  form_class = HotelForm
  template_name = "hotel/new-hotel.html"
  success_url = reverse_lazy("hotels")

def new_booking(request):
	pass

class BookRoom(CreateView):
  model = Booking
  form_class = BookingForm
  template_name = "hotel/book-room.html"

  success_url = reverse_lazy("home")
  
def delete_hotel(request, pk=None):
    hotel = get_object_or_404(Hotel, pk=pk)
    hotel.delete()
    return redirect("hotel-list")


class UpdateHotel(UpdateView):
	model = Hotel
	fields = "__all__"
	template_name = "hotel/update-hotel.html"
 
#  def delete_hotel(request, pk=None):
#         hotel = get_object_or_404(Hotel, pk=pk)
# 	hotel.delete()
# 	return redirect("hotel-list")
  