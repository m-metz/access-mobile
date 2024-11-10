from django.shortcuts import render
from django.utils.timezone import datetime

# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .models import UserProfile, SIMCard, Domain, Plan

# Create your views here.
def landing_page(request):
    return render(request, 'access_mobile_app/landing_page.html')

def donatee_signin(request):
    return render(request, 'access_mobile_app/donatee_signin.html')

def donor_signin(request):
    return render(request, 'access_mobile_app/donor_signin.html')