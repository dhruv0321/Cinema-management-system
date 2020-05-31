from django.contrib import admin
from cms_site.models import Film
from cms_site.models import Customer
from cms_site.models import Room
from cms_site.models import Screening
from cms_site.models import Seat
from cms_site.models import Booking
from cms_site.models import Reserved_seat

admin.site.register(Film)
admin.site.register(Customer)
admin.site.register(Room)
admin.site.register(Screening)
admin.site.register(Seat)
admin.site.register(Booking)
admin.site.register(Reserved_seat)

# Register your models here.
