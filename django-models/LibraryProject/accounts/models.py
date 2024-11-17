from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields here
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=False, null=False)
    profile_photo = models.ImageField(upload_to='profile_pics/', blank=True)