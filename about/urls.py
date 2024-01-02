from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('about-us/', views.about_us, name='about_us'),
    
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
    path('privacy-statement/' , views.privacy_statement , name='privacy_statement'),
    path('exchange-refund-policy/', views.exchange_refund_policy, name='exchange_refund_policy'),
    path('hack/', views.bug_bounty_program, name='bug_bounty_program'),

]

