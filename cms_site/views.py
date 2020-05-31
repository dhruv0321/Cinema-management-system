from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from cms_site.models import Booking,Customer,Reserved_seat,Screening,Film
# Create your views here.

def index(request):
    #all_customers = Booking.objects.all()
    return render(request, 'index.html')
def bookingsearch(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            details = Reserved_seat.objects.filter(booking_id = search_id)
            return render(request, 'booking.html', {'details': details})
        except Reserved_seat.DoesNotExist:
            return HttpResponse("no such user")  
    else:
        return render(request, 'index.html')

def customersearch(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            details = Customer.objects.filter(id = search_id)
            return render(request, 'customer.html', {'details': details})
        except Customer.DoesNotExist:
            return HttpResponse("no such user")  
    else:
        return render(request, 'index.html')

def screeningsearch(request):
    if request.method == 'POST':
        # search_id = request.POST.get('textfield', None)
        try:
            details = Screening.objects.all()
            return render(request, 'screening.html', {'details': details})
        except Screening.DoesNotExist:
            return HttpResponse("no such user")  
    else:
        return render(request, 'index.html')

def films(request):
    if request.method == 'POST':
        # search_id = request.POST.get('textfield', None)
        try:
            details = Film.objects.all()
            return render(request, 'film.html', {'details': details})
        except Screening.DoesNotExist:
            return HttpResponse("no such user")  
    else:
        return render(request, 'index.html')

def film_detail(request, pk):
    film = Screening.objects.filter(film = pk)
    return render(request, 'film_detail.html', {'film': film})

