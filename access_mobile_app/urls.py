from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('access-mobile/', views.access_mobile, name='access_mobile'),
    path('donee-signin/', views.donee_signin, name='donee_signin'),
    path('donee/', views.donee, name='donee'),
    path('donee-dashboard/<str:sim>', views.donee_dashboard, name='donee_dashboard'),
    path('donee-dashboard/<str:sim>/edit/', views.edit_donee_info, name='edit_donee_info'),
    path('edit-donor-info/', views.edit_donor_info, name='edit_donor_info'),
    path('view-donees/', views.view_donees, name='view_donees'),
    path('order-sim/', views.order_sim, name='order_sim'),
    path('donate-phone/', views.donate_phone, name='donate_phone'),
    path('donor/', views.donor, name='donor'),
    path('donor-signin/', views.donor_signin, name='donor_signin'),
    path('donor-login/', views.donor_login, name='donor_login'),
    path('donor-signup/', views.donor_signup, name='donor_signup'),
    path('donor-dashboard/', views.donor_dashboard, name='donor_dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('charity_finder/', views.charity_finder, name='charity_finder'),
    path('enter_sim/', views.enter_sim, name='enter_sim'),
    path('factory_reset_explanation/', views.factory_reset_explanation, name='factory_reset_explanation'),
    path('factory_reset/', views.factory_reset, name='factory_reset'),
    path('pay_sim/', views.pay_sim, name='pay_sim'),
    path('register_sim/', views.register_sim, name='register_sim'),
]
