from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

def home(request):
    context = {
        'name': 'john Doe',
        'gender': None,
        'age': 30,
        'occupation': 'Software Developer',
        'hobbies': ['Reading', 'Gardening', 'Swimming'],
        'friends': [
            {'name': 'Jane Doe', 'age': 28, 'occupation': 'Doctor'},
            {'name': 'James Doe', 'age': 35, 'occupation': 'Engineer'},
            {'name': 'Jenny Doe', 'age': 32, 'occupation': 'Teacher'},
            {'name': 'Josh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
        ],
        'num': [1, 2, 3],
        'month': 'January - February - March - April - May - June - July - August - September - October - November - December',
        'sentence': 'this is a Sentence with some Words',
        'date': datetime.now(),
        'txt':'Loading daaata',
        'num_messages': 2,
        'cherry': 4,
        'tomato': 3,
        'blog': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",

    }
    return render(request, 'home.html', context)