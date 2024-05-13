from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False) #이메일
    nickname = models.CharField(max_length=20, unique=True) #닉네임

    def __str__(self):
        return f'{self.username}'
