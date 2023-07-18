from django.contrib import admin
from .models import Availability, Appointment,Notice,Review,Insuranceininfo

# Register your models here.
@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'available_date', 'available_time', 'is_available')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('availability', 'client', 'is_approved')
admin.site.register((Notice,Review,Insuranceininfo))