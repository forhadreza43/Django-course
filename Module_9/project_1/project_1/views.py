from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse("Contact page from project_1/views.py")

def home(request):
    return HttpResponse("Home page from project_1/views.py")