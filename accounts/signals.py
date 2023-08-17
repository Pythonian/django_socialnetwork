from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile, Relationship


@receiver(post_save, sender=User)
def create_save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Relationship)
def add_to_friend(sender, instance, created, **kwargs):
    """Signal to create a relationship between two users."""
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'ACCEPTED':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()
