# accounts/urls.py
from django.urls import path
from .views import SignUpView , CustomLoginView
from .views import ProfileView , CustomLogoutView , ProfileUpdateView 


app_name = 'accounts'


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/edit/', ProfileUpdateView.as_view(), name='profile_update'),

    ]
