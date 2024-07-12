from django.shortcuts import render

# Create your views here.
def conact(request):
    return render(request, 'contact.html')
