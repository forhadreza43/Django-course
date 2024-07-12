from django.urls import path
from firstapp import views
urlpatterns = [
    path('contact/', views.contact),
    path('', views.home),
]
