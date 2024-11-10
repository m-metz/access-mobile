from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('donatee-signin/', views.donatee_signin, name='donatee_signin'),
    path('donee/', views.donee, name='donee'),
    path('donee-dashboard/', views.donee_dashboard, name='donee_dashboard'),
    path('donor/', views.donor, name='donor'),
    path('donor-signin/', views.donor_signin, name='donor_signin'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('sign-up/', views.sign_up, name='sign_up'),
]