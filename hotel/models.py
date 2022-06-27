from random import choices
from django.db import models
from django.contrib.auth.models import User
from rental.models import Member
from django.urls import reverse, reverse_lazy
from django.utils import timezone
# Create your models here.
from django.db.models import Q

HOTEL_CATEGORY = (
	("5_star", "5_star"),
	("4_star", "4_star"),
	("3_star", "3_star"),
	("Regular", "Regular"),
)
CANCELLATION = (
	("cancellation_charged", "cancellation_charged"),
	("Free_cancellation", "Free_cancellation"),
)
BED_CAPACITY = (
	("Double_bed", "Double_bed"),
	("Single_bed", "Single_bed"),
)
TV = (
	("Avalable", "Available"),
	("Not_available", "Not_available"),
)
HOT_SHOWER = (
	("Avalable", "Available"),
	("Not_available", "Not_available"),
)

BATHROOM_CHOICES = (
	("Outdoor", "Outdoor"),
	("Indoor", "Indoor"),
)
ROOM_CHOICES = (
	("hotel", "hotel"),
	("apartment", "apartment"),
	("Guest house", "Guest house"),
)

BOOKING_CHOICES = (
	("Half Day", "Half Day"),
	("Full Day", "Full Day"),
)

SWIMMING_POOL_CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available"),
)
WIFI_CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available"),
)
GYM_CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available"),
)
RESTAURANT_CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available"),
)
BAR_CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available"),
)
LIFT_OR_RAMP_CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available"),
)
BALCONY_CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available"),
)
KITCHEN_CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available"),
)
HOUSE_KEEPER_CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available"),
)
NETFLIX_CHOICES = (
	("Available", "Available"),
	("Not Available", "Not Available"),
)
class Hotel(models.Model):
	owner = models.ForeignKey(Member, on_delete=models.CASCADE)
	name = models.CharField(max_length=400)
	booking_option = models.CharField(max_length=200, choices=BOOKING_CHOICES, default="Half Day")
	bathroom = models.CharField(max_length=200, choices=BATHROOM_CHOICES, default="Indoor")
	rooms_count = models.IntegerField()
	room_type = models.CharField(max_length=200, choices=ROOM_CHOICES, default='Hotel')
	available_rooms = models.IntegerField(default=0)
	location = models.CharField(max_length=200)
	town = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	beds_count = models.IntegerField(default=0)
	bathroom = models.CharField(max_length=200, choices=BATHROOM_CHOICES, default="Indoor")
	swimming_pool = models.CharField(max_length=200, choices=SWIMMING_POOL_CHOICES, default="Available")
	wifi = models.CharField(max_length=200, choices=WIFI_CHOICES, default="Available")
	gym = models.CharField(max_length=200, choices=GYM_CHOICES, default="Available")
	restaurant = models.CharField(max_length=200, choices=RESTAURANT_CHOICES, default="Available")
	balcony = models.CharField(max_length=200, choices=BALCONY_CHOICES, default="Available")
	bar = models.CharField(max_length=200, choices=BAR_CHOICES, default="Available")
	lift_or_ramp = models.CharField(max_length=200, choices=LIFT_OR_RAMP_CHOICES, default="Available")
	kitchen = models.CharField(max_length=200, choices=KITCHEN_CHOICES, default="Available")
	netflix = models.CharField(max_length=200, choices=NETFLIX_CHOICES, default="Available")
	house_keeper = models.CharField(max_length=200, choices=HOUSE_KEEPER_CHOICES, default="Available")
	
	image_1 = models.ImageField(upload_to="hotel", default='image', blank=True, null=True)
	image_2 = models.ImageField(upload_to="hotel", default='image', blank=True, null=True)
	image_3 = models.ImageField(upload_to="hotel", default='image', blank=True, null=True)
	image_4 = models.ImageField(upload_to="hotel", default='image', blank=True, null=True)
	image_5 = models.ImageField(upload_to="hotel", default='image', blank=True, null=True)
	image_6 = models.ImageField(upload_to="hotel", default='image', blank=True, null=True)
	image_7 = models.ImageField(upload_to="hotel", default='image', blank=True, null=True)
	image_8 = models.ImageField(upload_to="hotel", default='image', blank=True, null=True)
	image_9 = models.ImageField(upload_to="hotel", default='image', blank=True, null=True)
	image_10 = models.ImageField(upload_to="hotel", default='image', blank=True, null=True)
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("hotel-details", kwargs={"pk": self.pk})

RATING_CHOICES = (
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5)
)

class Rating(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	rating = models.IntegerField(choices=RATING_CHOICES, default=1)
	review = models.TextField(null=True, blank=True)
	date_rated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.hotel)


BOOKING_CHOICES = (
	("Half Day", "Half Day"),
	("Full Day", "Full Day"),
)

class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	#hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
	hotel = models.CharField(max_length=200, null=True)
	booking_option = models.CharField(max_length=200, choices=BOOKING_CHOICES, default="Half Day")
	rooms_booked = models.IntegerField()
	date_booked = models.DateField(auto_now=True)
	checkin_date = models.DateField(null=True)
	checkout_date = models.DateField(null=True)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse("home")
