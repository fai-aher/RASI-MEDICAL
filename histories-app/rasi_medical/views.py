from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la vista de pacientes.")

def index(request):
    return render(request, 'index.html')

def healthCheck(request):
    return HttpResponse('ok')
