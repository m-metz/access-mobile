from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from .models import DoneeAccount

# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .models import UserProfile, SIMCard, Domain, Plan

# Create your views here.
def landing_page(request):
    return render(request, 'access_mobile_app/landing_page.html')

def donee_signin(request):
    if request.method == 'POST':
        sim = request.POST.get('sim')
        try:
            donee = DoneeAccount.objects.get(sim=sim)
            # Redirect to the donee dashboard page with the correct SIM in the URL
            return redirect('donee_dashboard', sim=donee.sim)
        except DoneeAccount.DoesNotExist:
            # If SIM doesn't exist, show an error message
            return render(request, 'access_mobile_app/donee_signin.html', {'error': 'Non-existent SIM'})
    return render(request, 'access_mobile_app/donee_signin.html')

def donor_signin(request):
    return render(request, 'access_mobile_app/donor_signin.html')

def access_mobile(request):
    return render(request, 'access_mobile_app/access_mobile.html')

def donee(request):
    return render(request, 'access_mobile_app/donee.html')

def donee_dashboard(request, sim):
    try:
        donee = DoneeAccount.objects.get(sim=sim)
    except DoneeAccount.DoesNotExist:
        return redirect('donatee_signin')  # Redirect back to sign-in if SIM is not found
    return render(request, 'access_mobile_app/donee_dashboard.html', {'donee': donee})

def edit_profile(request):
    return render(request, 'access_mobile_app/edit_profile.html')

def sign_up(request):
    return render(request, 'access_mobile_app/sign_up.html')

def donor(request):
    return render(request, 'access_mobile_app/donor.html')