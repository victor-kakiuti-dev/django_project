from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render



def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luiz Otávio',
    })


def contato(request):
    return render(request, 'me-apague/temp.html')


def sobre(request):
    return HttpResponse('sobre')
