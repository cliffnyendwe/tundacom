from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('', views.home, name='home'),
	path('houses/', views.houses, name='houses'),
	path('vacant-houses/', views.vacant_houses, name='vacant-houses'),
	path('sale-houses/', views.sale_houses, name='sale-houses'),
	path('swap-houses/', views.swap_houses, name='swap-houses'),

	path("messages/", views.messages, name="messages"),
	path("customers/", views.members, name="customers"),
	path("advertisements/", views.advertisements, name="advertisements"),
	path("dashboard/", views.dashboard, name="dashboard"),
  	path("property/", views.property, name="property"),
  	path("swap-list/", views.swap_list, name="swap-list"),
  	path("houses-list/", views.vacants_list, name="houses-list"),

	#properties
	path("property/<int:pk>/details/", views.property_details, name="property-details"),
	path("swap-house/<int:pk>/details/", views.swap_house_details, name="swap-house-details"),
	path("vacant-house/<int:pk>/details/", views.house_details, name="vacant-house-details"),
	path("delete/<int:pk>/rental/", views.delete_rental, name="delete-rental"),
	path("update/<int:pk>/rental/", UpdateRental.as_view(), name="update-rental"),

	#create views
	path("new-member/", NewMember.as_view(), name="new-member"),
	path("new-property/", NewProperty.as_view(), name="new-property"),
	path("new-vacant-house/", NewHouse.as_view(), name="new-vacant-house"),
	path("new-swap-house/", NewSwapHouse.as_view(), name="new-swap-house"),

	path("main_search/",views.main_search, name="main_search"), 
]
