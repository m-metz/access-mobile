from django.db import models

# Create your models here.






"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

class SIMCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sim_number = models.CharField(max_length=20)
    is_registered = models.BooleanField(default=False)

class Domain(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    plan = models.CharField(max_length=50)

class Plan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
"""