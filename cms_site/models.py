from django.db import models
import datetime
# Create your models here.

class Film(models.Model):
    id = models.AutoField(primary_key = True) # an auto)increment feild as a primary key
    name = models.CharField(max_length = 45,null = False)# automaticaly assigns a not null value
    length_min = models.IntegerField(null = False)
    def __str__(self):
        return self.name

class Customer(models.Model):
    #id = models.AutoField(primary_key = True) django automatically assigns id feild as primary key if not specified
    first_name = models.CharField(max_length = 45,null = True)
    last_name = models.CharField(max_length = 45 ,null = False)
    email = models.EmailField(null = False)
    def __str__(self):
        return self.last_name
    def fullname(self):
        return str(self.first_name) + " - " + self.last_name

class Room(models.Model):
    name = models.CharField(max_length = 45,null = False)
    no_seats = models.IntegerField(null = False)
    def __str__(self):
        return self.name 

class Screening(models.Model):
    film = models.ForeignKey('Film',on_delete = models.CASCADE,)
    room = models.ForeignKey('Room',on_delete = models.CASCADE,)
    start_time = models.DateTimeField()
    def __str__(self):
        return self.film.name + " " + str(self.start_time)

class Seat(models.Model):
    row_id = models.CharField(max_length =1,null = False)
    seat_number = models.IntegerField(null = False)
    room = models.ForeignKey('Room',on_delete=models.CASCADE)
    def __str__(self):
        return self.row_id + "" + str(self.seat_number) + " " + self.room.name

class Booking(models.Model):
    screening = models.ForeignKey('Screening',on_delete = models.CASCADE,)
    customers = models.ForeignKey('Customer',on_delete = models.CASCADE,)
    def __str__(self):
        return self.screening.film.name + " " + self.customers.fullname()

class Reserved_seat(models.Model):
    booking = models.ForeignKey('Booking',on_delete = models.CASCADE,)
    seat = models.ForeignKey('Seat',on_delete = models.CASCADE,)