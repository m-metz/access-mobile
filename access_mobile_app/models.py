from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class DonorAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# DonorAccount model with authentication
class DonorAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, primary_key=True)  # Email as the primary key
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = DonorAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


# DoneeAccount model
class DoneeAccount(models.Model):
    sim = models.CharField(max_length=20, primary_key=True)  # SIM as the primary key
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.sim})"


# Sponsorship model - linking DonorAccount and DoneeAccount
class Sponsorship(models.Model):
    donor_account = models.ForeignKey(DonorAccount, on_delete=models.CASCADE)
    donee_account = models.ForeignKey(DoneeAccount, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('donor_account', 'donee_account')

    def __str__(self):
        return f"Sponsorship: {self.donor_account.email} -> {self.donee_account.sim} with balance {self.balance}"