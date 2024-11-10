from django.shortcuts import render
from django.utils.timezone import datetime

# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .models import UserProfile, SIMCard, Domain, Plan

# Create your views here.
def example_view(request, name):
    return render(
        request,
        'access_mobile_app/example_view.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )



"""
def home(request):
    return render(request, 'core/home.html')

def signup(request):
    # Signup logic here
    return render(request, 'core/signup.html')

def login_view(request):
    # Login logic here
    return render(request, 'core/login.html')

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'core/profile.html', {'profile': user_profile})

def dashboard(request):
    # Dashboard logic here
    return render(request, 'core/dashboard.html')

def register_sim(request):
    # SIM registration logic here
    return render(request, 'core/register_sim.html')

def view_domains(request):
    domains = Domain.objects.filter(user=request.user)
    return render(request, 'core/domains.html', {'domains': domains})

def top_up(request):
    # Top-up logic here
    return render(request, 'core/top_up.html')

def payment(request):
    # Payment processing logic here
    return render(request, 'core/payment.html')
"""