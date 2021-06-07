from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WeChatUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE)