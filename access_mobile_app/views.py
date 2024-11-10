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

def access_mobile(request):
    return render(request, 'access_mobile_app/access_mobile.html')

def donee(request):
    return render(request, 'access_mobile_app/donee.html')

def donee_dashboard(request):
    return render(request, 'access_mobile_app/donee_dashboard.html')

def edit_profile(request):
    return render(request, 'access_mobile_app/edit_profile.html')

def sign_up(request):
    return render(request, 'access_mobile_app/sign_up.html')

def donor(request):
    return render(request, 'access_mobile_app/donor.html')

def factory_reset(request):
    return render(request, 'access_mobile_app/factory_reset.html')

def factory_reset_explanation(request):
    return render(request, 'access_mobile_app/factory_reset_explanation.html')

def pay_sim(request):
    return render(request, 'access_mobile_app/pay_sim.html')

def register_sim(request):
    return render(request, 'access_mobile_app/register_sim.html')

def charity_finder(request):
    return render(request, 'access_mobile_app/charity_finder.html')

def enter_sim(request):
    return render(request, 'access_mobile_app/enter_sim.html')