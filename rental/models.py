from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	country = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def member_address(self):
		return self.address + " , "+self.city+"-"+self.country

	def get_absolute_url(self):
    		return reverse("home")



HOUSE_ACTIONS = (
	("Agent", "Agent"),
	("Land lord", "Land lord"),
	("Tenant", "tenant"),
)

class House(models.Model):
	owner = models.ForeignKey(Member, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=30, default='0')
	property_name = models.CharField(max_length=200, null=True)
	posted_by = models.CharField(max_length=100, choices=HOUSE_ACTIONS, default='Landlord')
	location = models.CharField(max_length=500)
	town = models.CharField(max_length=200, default='town')
	rent = models.FloatField()
	bedrooms = models.IntegerField()
	description = models.TextField()
	image_2 = models.ImageField(upload_to="houses", default='houses')
	image_3 = models.ImageField(upload_to="houses", default='houses')
	image_1 = models.ImageField(upload_to="houses", default='houses')
	image_4 = models.ImageField(upload_to="houses", default='houses')
	image_5 = models.ImageField(upload_to="houses", default='houses')
	image_6 = models.ImageField(upload_to="houses", default='houses')
	image_7 = models.ImageField(upload_to="houses", default='houses')
	image_8 = models.ImageField(upload_to="houses", default='houses')
	image_9 = models.ImageField(upload_to="houses", default='houses')
	image_10 = models.ImageField(upload_to="houses", default='houses')
	approved = models.BooleanField(default=False)


	def __str__(self):
		return self.owner.name

	def get_absolute_url(self):
    		return reverse("vacant-house-details", kwargs={"pk": self.pk})

PROPERTY_TYPE_CHOICES = (
	("House", "House"),
	("land", "land"),
)

class Property(models.Model):
	owner = models.ForeignKey(Member, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=30, default='0')
	property_name = models.CharField(max_length=200)
	property_type = models.CharField(max_length=200, choices=PROPERTY_TYPE_CHOICES, default='property type')
	location = models.CharField(max_length=500)
	town = models.CharField(max_length=200, default='town')
	price = models.FloatField(default=0)
	description = models.TextField()
	image_2 = models.ImageField(upload_to="property", default='property')
	image_3 = models.ImageField(upload_to="property", default='property')
	image_1 = models.ImageField(upload_to="property", default='property')
	image_4 = models.ImageField(upload_to="property", default='property')
	image_5 = models.ImageField(upload_to="property", default='property')
	image_6 = models.ImageField(upload_to="property", default='property')
	image_7 = models.ImageField(upload_to="property", default='property')
	image_8 = models.ImageField(upload_to="property", default='property')
	image_9 = models.ImageField(upload_to="property", default='property')
	image_10 = models.ImageField(upload_to="property", default='property')
	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.owner.name

	def get_absolute_url(self):
    		return reverse("property-details", kwargs={"pk": self.pk})

SWAP_HOUSE_CHOICES = (
	("Swapwith another house", "Swap with another house"),
	("Swap for with Discounted Deposit", "Swap for with Discounted Deposit"),
	("Swap for another house/Discounted Deposit", "Swap for another house/Discounted Deposit"),
)

class SwapHouse(models.Model):
	owner = models.ForeignKey(Member, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=30, default='0')
	property_name = models.CharField(max_length=200)
	swap_house_option = models.CharField(max_length=200, choices=SWAP_HOUSE_CHOICES, default="swap house")
	location = models.CharField(max_length=500)
	town = models.CharField(max_length=200, default='town')
	rent = models.FloatField()
	bedrooms = models.IntegerField()
	description = models.TextField()
	image_1 = models.ImageField(upload_to="swap-houses", default='image')
	image_2 = models.ImageField(upload_to="swap-houses", default='image')
	image_3 = models.ImageField(upload_to="swap-houses", default='image')
	image_4 = models.ImageField(upload_to="swap-houses", default='image')
	image_5 = models.ImageField(upload_to="swap-houses", default='image')
	image_6 = models.ImageField(upload_to="swap-houses", default='image')
	image_7 = models.ImageField(upload_to="swap-houses", default='image')
	image_8 = models.ImageField(upload_to="swap-houses", default='image')
	image_9 = models.ImageField(upload_to="swap-houses", default='image')
	image_10 = models.ImageField(upload_to="swap-houses", default='image')
	approved = models.BooleanField(default=False)


	def __str__(self):
		return self.owner.name

	def get_absolute_url(self):
    		return reverse("swap-house-details", kwargs={"pk": self.pk})



class HouseImage(models.Model):
	house = models.ForeignKey(House, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="houses")

	def __str__(self):
		return self.house.owner.name


class Advertisement(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title =models.CharField(max_length=500)
	message = models.TextField(blank=True, null=True)
	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	sender = models.CharField(max_length=200, blank=True, null=True)
	body = models.TextField()
	date_send = models.DateField(auto_now_add=True)
	reply = models.TextField(blank=True, null=True)
	date_replied = models.DateField(auto_now=True)

	def __str__(self):
		return self.body[:50]
