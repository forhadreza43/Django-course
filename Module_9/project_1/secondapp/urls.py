from django.urls import path
from secondapp import views

urlpatterns = [
    path('contact/', views.contact),
    path('', views.home),
]