
# Create your views here.


# contact_us/views.py

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success/')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})



def contact_success(request):
    return render(request, 'contact_success.html')
