from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        label="اسمك الأول",
        max_length=30, required=True)
    
    last_name = forms.CharField(
        label="اسمك الأخير",
        max_length=30, required=True)
    
    phone_number = forms.CharField(
        label="رقم هاتفك",
        max_length=30, required=True)

    pay_account_user = forms.CharField(
        label="رقم حساب سيرياتيل كاش",
        max_length=30, required=True)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number' , 'pay_account_user' , 'latitude', 'longitude']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        # Check if the phone number is valid for Syria
        if not phone_number.startswith('09') or not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError('Please enter a valid Syrian phone number 09xxxxxxxx.')

        return phone_number