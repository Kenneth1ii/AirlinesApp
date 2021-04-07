from django.contrib import admin
from .models import Flight, Airport, Passenger
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id','origin','destination','duration')

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

# Add Models to Site:8000/Admins To Use.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)