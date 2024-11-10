from django.db import models

# Create your models here.
class example_model(models.Model):
    FirstName = models.CharField(max_length=50)

    def __str__(self):
        return self.FirstName