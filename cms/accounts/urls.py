from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('home/', views.home),
	path('product/', views.product),
	path('customer/', views.customer),
]