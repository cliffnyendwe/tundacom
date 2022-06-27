from django.shortcuts import render

from rental.forms import MemberForm, HouseForm, SwapHouseForm, PropertyForm
from . models import *
from hotel.models import Hotel
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Create your views here.
def main_search(request):
	q = request.GET.get('q') if request.GET.get('q') != None else ''
	hotels = Hotel.objects.filter(Q(name__icontains=q) | Q(location__icontains=q) | Q(town__icontains=q))
	properties = Property.objects.filter(Q(property_name__icontains=q) | Q(location__icontains=q) | Q(town__icontains=q))
	houses = House.objects.filter(Q(property_name__icontains=q) | Q(location__icontains=q) | Q(town__icontains=q))
	swap_houses = SwapHouse.objects.filter(Q(property_name__icontains=q) | Q(location__icontains=q) | Q(town__icontains=q))

	context = {
		"hotels": hotels,
		"properties": properties,
		"houses": houses,
		"swap_houses": swap_houses		
	}	
	print(context)
	return render(request, "index.html", context)

def home(request):
	hotels = Hotel.objects.all()[:4]
	properties = Property.objects.all()[:4]
	houses = House.objects.all()[:4]
	swap_houses = SwapHouse.objects.all()[:4]
	context = {
		"hotels": hotels,
		"properties": properties,
		"houses": houses,
		"swap_houses": swap_houses
	}
	return render(request, "index.html", context)

def dashboard(request):
	return render(request, "home.html")

def property(request):
	q = request.GET.get('q') if request.GET.get('q') != None else ''
	properties = Property.objects.filter(Q(property_name__icontains=q) | Q(location__icontains=q) | Q(price__icontains=q)|Q(town__icontains=q))
	#properties = Property.objects.all()
	context = {
		"properties": properties
	}
	return render(request, "rental/property-list.html", context)

class NewProperty(CreateView):
	model = Property
	form_class = PropertyForm
	template_name = "rental/new-property.html"

class NewSwapHouse(CreateView):
	model = SwapHouse
	form_class = SwapHouseForm
	template_name = "rental/new-swap-house.html"

class NewHouse(CreateView):
	model = House
	form_class = HouseForm
	template_name = "rental/new-house.html"

def property_details(request, pk):
	property = Property.objects.get(id=pk)
	context = {
		"property": property
	}
	return render(request, "rental/property-details.html", context)

def house_details(request, pk):
	house = House.objects.get(id=pk)
	context = {
		"house": house
	}
	return render(request, "rental/house-details.html", context)

def swap_house_details(request, pk):
	swap_house = SwapHouse.objects.get(id=pk)
	context = {
		"swap_house": swap_house
	}
	return render(request, "rental/swap-house-details.html", context)

def swap_list(request):
	q = request.GET.get('q') if request.GET.get('q') != None else ''
	swap_houses = SwapHouse.objects.filter(Q(property_name__icontains=q) | Q(location__icontains=q) | Q(rent__icontains=q))
	context = {
    "swap_houses": swap_houses
  	}
	return render(request, "rental/swap-list.html", context)

def vacants_list(request):
	q = request.GET.get('q') if request.GET.get('q') != None else ''
	houses = House.objects.filter(Q(property_name__icontains=q) | Q(location__icontains=q) | Q(rent__icontains=q))
	context = {
    "houses": houses
  	}
	return render(request, "rental/houses-list.html", context)

def houses(request):
	houses = House.objects.all()
	title = "Posted Houses"
	context = {
		"houses": houses,
		"title": title
	}
	return render(request, "rental/houses.html", context)

def vacant_houses(request):
	houses = House.objects.filter(house_type="Vacant")
	title = "Vacant Houses"

	context = {
		"houses": houses,
		"title": title
	}
	return render(request, "rental/houses.html", context)

def sale_houses(request):
	houses = House.objects.filter(house_type="Sale")
	title = "Sale Houses"

	context = {
		"houses": houses,
		"title": title
	}
	return render(request, "rental/houses.html", context)

def swap_houses(request):
	houses = House.objects.filter(house_type="Swapping")
	title = "Swap Houses"

	context = {
		"houses": houses,
		"title": title
	}
	return render(request, "rental/houses.html", context)


def new_house(request):
	pass

def messages(request):
	messages = Message.objects.all()
	context = {
		"messages": messages
	}
	return render(request, "rental/messages.html", context)

def new_message(request):
	pass

def members(request):
	members = Member.objects.all()
	context = {
		"members": members
	}
	return render(request, "rental/members.html", context)

class NewMember(CreateView):
	model = Member
	#fields = "__all__"
	form_class = MemberForm
	template_name = "rental/new-member.html"

def advertisements(request):
	advertisements = Advertisement.objects.all()
	context = {
		"advertisements": advertisements
	}
	return render(request, "rental/advertisements.html", context)

def new_advertisement(request):
	pass



def delete_rental(request, pk=None):
	rental = get_object_or_404(House, pk=pk)
	rental.delete()
	#return redirect("houses-list")


class UpdateRental(UpdateView):
	model = House
	fields = "__all__"
	template_name = "rental/update-rental.html"