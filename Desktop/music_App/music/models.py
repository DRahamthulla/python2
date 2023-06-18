from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from uuid import uuid4

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email
class MusicFile(models.Model):
    file = models.FileField(upload_to='music/')
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title