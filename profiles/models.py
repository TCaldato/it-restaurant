from django.db import models
from django.contrib.auth.models import User

# Create your views here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank=False)
