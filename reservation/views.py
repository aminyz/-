from django.shortcuts import render, HttpResponse


def reserve(request):
    return render(request, 'reservation/reserve.html')
