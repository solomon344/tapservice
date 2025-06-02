from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class ServiceRef(models.Model):
    """
    Model representing a service ref that can be tapped.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    cover_image = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    """
    Model representing a service that can be tapped.
    """
    service_ref = models.ForeignKey(ServiceRef, on_delete=models.CASCADE, related_name='services')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')
    cover_image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_ref.name} by {self.user.username}"
    

class ServiceReviews(models.Model):
    """
    Model representing reviews for a service.
    """
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    rate = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self) -> str:
        return self.by.username


class BookingChoices(models.TextChoices):
    PENDING = 'PENDING', 'pending'
    CONFIRMED = 'CONFIRMED', 'confirmed'
    CANCELLED = 'CANCELLED', 'cancelled'
     

class Booking(models.Model):
    """
    Model representing a booking for a service.
    """
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    date = models.CharField(max_length=20)  # Assuming date is stored as a string, e.g., 'YYYY-MM-DD'
    time = models.CharField(max_length=10)  # Assuming time is stored as a string, e.g., 'HH:MM'
    address = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=BookingChoices.choices, default=BookingChoices.PENDING) 


    def __str__(self):
        return f"Booking by {self.user.username} for {self.service.service_ref.name} on {self.date}"
    
