from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField()   # no pillow needed
    category = models.CharField(max_length=100)
    redirect_url = models.URLField()

    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.IntegerField(default=0)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)