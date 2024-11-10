from django.shortcuts import render
from django.utils.timezone import datetime

# Create your views here.
def example_view(request, name):
    return render(
        request,
        'access_mobile_app/example_view.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )