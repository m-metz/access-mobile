from django.urls import path

from access_mobile_app import views 

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('donatee/signin/', views.donatee_signin, name='donatee_signin'),
    path('donor/signin/', views.donor_signin, name='donor_signin'),
]
