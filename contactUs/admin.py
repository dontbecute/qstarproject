
# Register your models here.
# contact_us/admin.py

from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    search_fields = ['name', 'email']

admin.site.register(ContactMessage, ContactMessageAdmin)
