from django.contrib.auth.models import User
from .models import Stadium,Pitch,Booking
from django.dispatch import Signal,receiver
from django.db.models.signals import post_save,post_delete
    
    
@receiver(post_save, sender=User)
def user_save(sender, instance, created, **kwargs):
    print("Your Account created successfully", instance)

@receiver(post_save, sender=Stadium)
def stadium_save(sender, instance, created, **kwargs):
    print("Your Stadium created successfully", instance)

@receiver(post_save, sender=Pitch)
def pitch_save(sender, instance, created, **kwargs):
    print("Your Pitch created successfully", instance)
    
@receiver(post_save, sender=Booking)
def booking_save(sender, instance, created, **kwargs):
    print("Your booking created successfully", instance)

@receiver(post_delete, sender=User)
def user_delete(sender, instance, **kwargs):
    print("Your Account deleted successfully", instance)

@receiver(post_delete, sender=Stadium)
def stadium_delete(sender, instance, **kwargs):
    print("Your Stadium deleted successfully", instance)

@receiver(post_delete, sender=Pitch)
def pitch_delete(sender, instance, **kwargs):
    print("Your Pitch deleted successfully", instance)

@receiver(post_delete, sender=Booking)
def booking_save(sender, instance, **kwargs):
    print("Your Booking deleted successfully", instance)