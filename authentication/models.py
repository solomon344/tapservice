from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    # You can add additional fields here if needed
    email = models.EmailField(unique=True, blank=False, null=False)
    picture = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    def save(self, *args, **kwargs):
        """
        Override the save method to ensure the email is unique.
        """
        if not self.email:
            raise ValueError("The Email field must be set.")
        super().save(*args, **kwargs)
    pass
    
   


