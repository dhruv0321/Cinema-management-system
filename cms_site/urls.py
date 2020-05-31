from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.bookingsearch, name='bookingsearch'),
    path('customer', views.customersearch, name='customersearch'),
    path('screening', views.screeningsearch, name='screeningsearch'),
    path('film', views.films, name='films'),
    path('film/<int:pk>/',views.film_detail, name='film_detail')


    #path('customer', views.custom_sql_db_display, name='Customer'),
    #path('room', views.custom_sql_db_display, name='Room'),
    #path('screening', views.custom_sql_db_display, name='Screening'),
    #path('seat', views.custom_sql_db_display, name='Seat'),
    #path('booking', views.custom_sql_db_display, name='Booking'),
    #path('reserved', views.custom_sql_db_display, name='Reserved_seat'),
    
]
