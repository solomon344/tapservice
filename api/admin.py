from django.contrib import admin
from .models import (ServiceRef, Service, ServiceReviews, Booking)

# Register your models here.
admin.site.register(ServiceRef)
admin.site.register(Service)
admin.site.register(ServiceReviews)
admin.site.register(Booking)