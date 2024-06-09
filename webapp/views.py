from django.shortcuts import render
import datetime


def index(request):
    context = {
        'name': 'Changos Rent Webapp\'s index page',
        'date': datetime.datetime.now()
    }
    return render(request, 'index.html', context)
