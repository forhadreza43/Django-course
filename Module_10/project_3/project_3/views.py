from django.shortcuts import render
from datetime import datetime
def home(request):
    context = {'name': 'Reza', 
         'occupation': 'Software Engineer', 
         'hobbies': ['Programming', 'Eating'],
         'city':'Dhaka', 
         'state':'Bangladesh', 
         'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         'email': ['forhad', '.','bimt', '@', 'gmail', '.', 'com'],
         'salary': 1000,
         'phone': ['0', '1', '7', '1', '1', '1', '1', '1', '1', '1', '1'],
         'date': datetime.now(),
         }
    return render(request, 'home.html', context)