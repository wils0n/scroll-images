from django.db import models

from django.contrib.auth.models import User

class UserCustom(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField()
