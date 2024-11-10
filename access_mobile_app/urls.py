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
    path('charity_finder/', views.charity_finder, name='charity_finder'),
    path('enter_sim/', views.enter_sim, name='enter_sim'),
    path('factory_reset_explanation/', views.factory_reset_explanation, name='factory_reset_explanation'),
    path('factory_reset/', views.factory_reset, name='factory_reset'),
    path('pay_sim/', views.pay_sim, name='pay_sim'),
    path('register_sim/', views.register_sim, name='register_sim'),
]