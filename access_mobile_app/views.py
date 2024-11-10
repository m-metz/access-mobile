from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import datetime
from .models import DoneeAccount, Sponsorship, DonorAccount
from .forms import DoneeEditForm

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