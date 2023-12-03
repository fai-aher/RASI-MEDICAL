from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'is_authenticated': True,
        'username': "jsurrea",
    }
    return render(request, 'index.html', context) #TODO add context is_authenticated, username

def healthCheck(request):
    return HttpResponse('ok')
