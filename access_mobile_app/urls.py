from django.urls import path

from access_mobile_app import views 

urlpatterns = [
    path('hello/<name>', views.example_view, name='example_view'),
]
