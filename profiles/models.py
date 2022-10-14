from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

# Class provided by DRF-API walkthrough, updates and modifications made. 


class Profile(models.Model):
    """
    Profile model for database.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    country = models.CharField(max_length=60, blank=True)
    username = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_qdjgyp',
    )
    
    class Meta:
        """
        Display profiles in order they were created.
        Newest first.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Changing display name from ID
        to username.
        """
        return f"{self.username}'s profile."

# Function provided by DRF-API walkthrough project. 

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
