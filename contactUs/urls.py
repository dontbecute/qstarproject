# contact_us/urls.py

from django.urls import path
from .views import contact_us, contact_success

app_name = 'contactUs'


urlpatterns = [
    path('contact/', contact_us, name='contact_us'),
    path('contact/success/', contact_success, name='contact_success'),
]
