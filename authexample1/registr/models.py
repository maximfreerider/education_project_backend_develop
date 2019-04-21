from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# class Package(models.Model):
#     name_of_package = models.CharField(max_length=150, default=0, null=True, blank=True)


class AskAnswerMode(models.Model):
    pass


class TestMode(models.Model):
    pass


class ModeOfStudy(models.Model):
    asks_answers = models.ForeignKey(AskAnswerMode, on_delete=models.CASCADE, blank=True, null=True)
    tests = models.ForeignKey(TestMode, on_delete=models.CASCADE, blank=True, null=True)


class Package(models.Model):
    name_of_package = models.CharField(max_length=150, default=0, null=True, blank=True)
    mode_of_study = models.ForeignKey(ModeOfStudy, on_delete=models.CASCADE,blank=True, null=True)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField
    bio = models.TextField(max_length=250, blank=True, null=True)
    photo = models.ImageField(blank=True, default=None)
    packages = models.ForeignKey(Package, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.username