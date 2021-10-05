from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):    
    return HttpResponse('Главная страница блога YaTube')

def group_post(request, slug):    
    return HttpResponse(f'Группа постов {slug}')