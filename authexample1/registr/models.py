from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Package(models.Model):
    name_of_package = models.CharField(max_length=150, default=0, null=True, blank=True)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField
    bio = models.TextField(max_length=250, blank=True, null=True)
    photo = models.ImageField(blank=True, default=None)
    packages = models.ForeignKey(Package, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username