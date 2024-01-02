# accounts/views.py
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView , UpdateView
from accounts.models import CustomUser
from .forms import CustomUserCreationForm , CustomAuthenticationForm , CustomUserUpdateForm
from django.contrib.auth.views import LoginView

from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

from django.contrib.auth.views import LogoutView
from django.contrib import messages

from verify_email.email_handler import send_verification_email



class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # Use the custom form
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('verify_email:request-new-link-from-email')  

    def form_valid(self, form):
        user = form.save()
        response = super(SignUpView, self).form_valid(form)
        send_verification_email(self.request, form)
        return response


class CustomLogoutView(LogoutView):
    
    template_name = 'profile.html'
    
    redirect_to = 'accounts:login'


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.user.is_authenticated:
                firstname = self.request.user.first_name
                messages.success(self.request, f'مرحباً بك {firstname}')  # Add this line for success message
        
        return response
            
        
class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        # Retrieve the user based on the captured username
        username = self.kwargs.get('username')
        user = get_object_or_404(CustomUser, username=username)

        # Check if the logged-in user is the same as the requested user
        if self.request.user == user:
            return user
        else:
            return reverse("errorhandler:error_403")
        

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'profile_update.html'  # Create this template

    def get_object(self, queryset=None):
        return self.request.user  # Use the logged-in user as the object to be updated

    def get_success_url(self):
        return reverse('accounts:profile' , kwargs={'username': self.request.user.username})
    
