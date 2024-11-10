from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('access-mobile/', views.access_mobile, name='access_mobile'),
    path('donee-signin/', views.donee_signin, name='donee_signin'),
    path('donee/', views.donee, name='donee'),
    path('donee-dashboard/<str:sim>', views.donee_dashboard, name='donee_dashboard'),
    path('donor/', views.donor, name='donor'),
    path('donor-signin/', views.donor_signin, name='donor_signin'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('sign-up/', views.sign_up, name='sign_up'),
]