from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField()