from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_post(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_post(sender, instance, **kwargs):
    instance.profile.save()

# this could be written like 
# def create_post(sender, instance, created, **kwargs):
#    if created:
#       Profile.objects.create(user = instance)

# post_save.connect(create_post, sender = User)
