from django.shortcuts import render
from .models import Food


def menu(request):
    foods = Food.objects.all()

    return render(request, 'Menu/menu.html', context={'foods': foods})
