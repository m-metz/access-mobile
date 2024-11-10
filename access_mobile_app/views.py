from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import datetime
from .models import DoneeAccount, Sponsorship, DonorAccount, DonorAccountManager
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Sum
from .forms import DoneeEditForm, DonorProfileForm
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
    
    # Look up the donor linked through the sponsorship and fetch balance if available
    sponsorship = Sponsorship.objects.filter(donee_account=donee).first()
    donor = sponsorship.donor_account if sponsorship else None
    balance = sponsorship.balance if sponsorship else None
    
    return render(request, 'access_mobile_app/donee_dashboard.html', {
        'donee': donee,
        'donor': donor,
        'balance': balance
    })

def edit_donee_info(request, sim):
    donee = get_object_or_404(DoneeAccount, sim=sim)
    
    if request.method == 'POST':
        form = DoneeEditForm(request.POST, instance=donee)
        if form.is_valid():
            form.save()
            return redirect('donee_dashboard', sim=donee.sim)
    else:
        form = DoneeEditForm(instance=donee)
    
    return render(request, 'access_mobile_app/edit_donee_info.html', {'form': form, 'donee': donee})

def donor_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('donor_dashboard')
        else:
            return render(request, 'access_mobile_app/donor_login.html', {'error': 'Invalid credentials'})

    return render(request, 'access_mobile_app/donor_login.html')

def donor_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        if DonorAccount.objects.filter(email=email).exists():
            return render(request, 'access_mobile_app/donor_signup.html', {'error': 'Email already in use'})
        
        user = DonorAccount.objects.create_user(email=email, password=password, name=name)
        login(request, user)
        return redirect('donor_dashboard')

    return render(request, 'access_mobile_app/donor_signup.html')

@login_required
def donor_dashboard(request):
    donor = request.user  # Gets the currently logged-in user
    sponsorship_count = Sponsorship.objects.filter(donor_account=donor).count()  # Count sponsorships

    context = {
        'donor': donor,
        'sponsorship_count': sponsorship_count,
    }
    return render(request, 'access_mobile_app/donor_dashboard.html', context)

@login_required
def edit_donor_info(request):
    donor = request.user  # Get the currently authenticated donor
    if request.method == 'POST':
        form = DonorProfileForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_dashboard')  # Redirect to the donor dashboard after saving
    else:
        form = DonorProfileForm(instance=donor)  # Prepopulate the form with current donor data

    return render(request, 'access_mobile_app/edit_donor_info.html', {'form': form})

@login_required
def view_donees(request):
    donor = request.user  # The authenticated user is a donor account
    donees = DoneeAccount.objects.filter(sponsorship__donor_account=donor)

    donee_info = []
    for donee in donees:
        # Calculate the remaining balance (or total sponsorship amount)
        total_sponsorship = Sponsorship.objects.filter(donee_account=donee, donor_account=donor).aggregate(total_balance=Sum('balance'))
        remaining_balance = total_sponsorship.get('total_balance', 0)

        donee_info.append({
            'donee': donee,
            'remaining_balance': remaining_balance
        })

    return render(request, 'access_mobile_app/view_donees.html', {'donee_info': donee_info})

@login_required
def order_sim(request):
    return render(request, 'access_mobile_app/order_sim.html')

@login_required
def donate_phone(request):
    return render(request, 'access_mobile_app/donate_phone.html')


def donor_donees(request):
    donees = DoneeAccount.objects.all()[:3]  # Get the first three donees
    return render(request, 'access_mobile_app/donor_donees.html', {'donees': donees})

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