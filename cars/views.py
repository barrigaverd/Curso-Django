from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    search = request.GET.get('search')
    cars = Car.objects.filter(model__contains=search) if search else Car.objects.all()

    return render(
        request, 
        'cars.html', 
        {'cars': cars }
    )
