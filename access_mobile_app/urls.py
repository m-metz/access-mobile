from django.urls import path

from access_mobile_app import views 

urlpatterns = [
    path('hello/<name>', views.example_view, name='example_view'),
]

"""
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register-sim/', views.register_sim, name='register_sim'),
    path('domains/', views.view_domains, name='view_domains'),
    path('top-up/', views.top_up, name='top_up'),
    path('payment/', views.payment, name='payment'),
]
"""