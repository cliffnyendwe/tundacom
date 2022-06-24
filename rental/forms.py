from django import forms
from django.forms import ModelForm
from . models import *

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('user', 'name', 'phone_number', 'address', 'city', 'country')

        widgets = {
        	'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'country': forms.TextInput(attrs={'class': 'form-control'}),
        }


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ('owner', 'phone_number', 'property_name', 'posted_by','location', 'town', 'rent', 'bedrooms', 'description', 'image_1','image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8', 'image_9', 'image_10')

        widgets = {
        	'owner': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'owner', 'type': 'hidden'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
			'location': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
			'rent': forms.NumberInput(attrs={'class': 'form-control'}),
			'bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			#'photo': forms.PhotoInput(attrs={'class': 'form-control'}),
        }

class SwapHouseForm(forms.ModelForm):
    class Meta:
        model = SwapHouse
        fields = ('owner', 'phone_number', 'property_name', 'location', 'town', 'rent', 'bedrooms', 'description', 'swap_house_option', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8', 'image_9', 'image_10')

        widgets = {
        	'owner': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'owner', 'type': 'hidden'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
			'location': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
			'rent': forms.NumberInput(attrs={'class': 'form-control'}),
			'bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			#'photo': forms.PhotoInput(attrs={'class': 'form-control'}),
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('owner', 'phone_number', 'property_name', 'location', 'town', 'price', 'description', 'property_type','image_1','image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8', 'image_9', 'image_10')

        widgets = {
        	'owner': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'owner', 'type': 'hidden'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
			'location': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.NumberInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			#'photo': forms.PhotoInput(attrs={'class': 'form-control'}),
        }



class AdvertisementForm(ModelForm):
	class Meta:
		model = Advertisement
		fields = "__all__"

class MessageForm(ModelForm):
	class Meta:
		model = Message
		fields = "__all__"
