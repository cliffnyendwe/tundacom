from django.forms import ModelForm
from django import forms
from . models import *

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('owner', 'name', 'booking_option','room_type', 'rooms_count', 'available_rooms', 'location', 'town', 'price', 'beds_count', 'bathroom', 'swimming_pool', 'bar', 'wifi', 'netflix', 'gym'
        ,'restaurant', 'balcony', 'kitchen', 'house_keeper', 'lift_or_ramp','image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8', 'image_9', 'image_10')

        widgets = {
        	'owner': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'owner', 'type': 'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
			'rooms_count': forms.NumberInput(attrs={'class': 'form-control'}),
			'available_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
			'location': forms.TextInput(attrs={'class': 'form-control'}),
			'town': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.NumberInput(attrs={'class': 'form-control'}),
			'beds_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'file_field': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':
True}))
            #'kids_allowed': forms.NumberInput(attrs={'class': 'form-control'}),
			#'photo': forms.PhotoInput(attrs={'class': 'form-control'}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ("review", "rating")


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'hotel', 'booking_option', 'rooms_booked', 'checkin_date', 'checkout_date')

        widgets = {
        	'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'hotel': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'hotel', 'type': 'hidden'}),
            'booking_option': forms.Select(attrs={'class': 'form-control'}),
			'rooms_booked': forms.NumberInput(attrs={'class': 'form-control'}),
            'checkin_date': forms.DateInput(attrs={'class': 'form-control'}),
            'checkout_date': forms.DateInput(attrs={'class': 'form-control'}),
        }

class UpdateHotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('owner', 'name', 'booking_option','room_type', 'rooms_count', 'available_rooms', 'location', 'town', 'price', 'beds_count', 'bathroom', 'swimming_pool', 'bar', 'wifi', 'netflix', 'gym'
        ,'restaurant', 'balcony', 'kitchen', 'house_keeper', 'lift_or_ramp','image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8', 'image_9', 'image_10')

        widgets = {
        	'owner': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'owner', 'type': 'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
			'rooms_count': forms.NumberInput(attrs={'class': 'form-control'}),
			'available_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
			'location': forms.TextInput(attrs={'class': 'form-control'}),
			'town': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.NumberInput(attrs={'class': 'form-control'}),
			'beds_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'file_field': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':
True}))
            #'kids_allowed': forms.NumberInput(attrs={'class': 'form-control'}),
			#'photo': forms.PhotoInput(attrs={'class': 'form-control'}),
        }