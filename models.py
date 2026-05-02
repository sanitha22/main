from django.db import models
from django.contrib.auth.models import User


class Register(models.Model):
    GENDER_CHOICE = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Others'),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICE,
        null=True,
        blank=True
    )

    image = models.FileField(upload_to='images/', null=True, blank=True)

class LoginHistory(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models

class CaptionImage(models.Model):

    image = models.ImageField(upload_to="uploads/")
    cartoon_url = models.URLField(blank=True, null=True)

    scene = models.TextField(blank=True)

    caption_en = models.TextField(blank=True)
    caption_ml = models.TextField(blank=True)
    caption_hi = models.TextField(blank=True)
    caption_ta = models.TextField(blank=True)
    caption_es = models.TextField(blank=True)

    hashtags = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Caption {self.id}"