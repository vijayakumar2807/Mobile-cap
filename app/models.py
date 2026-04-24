from django.db import models   # 🔥 MUST

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()