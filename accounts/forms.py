# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label="اسمك الأول",
        max_length=30, required=True)
    
    last_name = forms.CharField(
        label="اسمك الأخير",
        max_length=30, 
        required=True, 
)
    
    phone_number = forms.CharField(
        label="رقم هاتفك",
        max_length=30, 
        required=True, 
    )

    email = forms.EmailField(
        label="البريد الالكتروني",

    )

    password1 = forms.CharField(
        label="كلمة السر",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="يجب أن تحتوي كلمة المرور على الأقل 8 أحرف ولا يمكن أن تكون مشابهة للمعلومات الشخصية الأخرى."
    )
    password2 = forms.CharField(
        label="تأكيد كلمة السر",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    
    
    class Meta:
        model = CustomUser
        fields = ( 'first_name', 'last_name', 'phone_number' , 'email', 'password1', 'password2', )


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="البريد الالكتروني",

    )
    password = forms.CharField(
        label="كلمة السر",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    
    class Meta:
        model = AuthenticationForm

        fields = ('email' , 'password')

        

    remember_me = forms.BooleanField(
        label="تذكرني",

        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    def clean_remember_me(self):
        # Additional validation logic for the remember_me field
        remember_me = self.cleaned_data.get('remember_me')
        # Add your custom validation logic here if needed
        return remember_me


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number' , 'email']  # Add other fields as needed
