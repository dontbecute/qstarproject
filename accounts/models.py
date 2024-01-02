from audioop import reverse
from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
import uuid
from django.utils import timezone




class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=15 , 
    validators=[
        RegexValidator(
            regex='^[a-zA-Zأ-ي]+$',
            message='First name must only contain letters.',
            code='invalid_first_name'
        )
    ],
    )

    last_name = models.CharField(max_length=15, 
    validators=[
        RegexValidator(
            regex='^[a-zA-Zأ-ي]+$',
            message='Last name must only contain letters.',
            code='invalid_last_name'
        )
    ],
    )
    
    email  = models.EmailField(unique=True)

    username = models.CharField(max_length=36, unique=True, default=uuid.uuid4, editable=False)

    phone_number = models.CharField(max_length=15, blank=True, validators=[
        RegexValidator(
            regex='^[0-9]{8}$',
            message='Phone number must be a valid Syrian number starting with 09 and consisting of 10 digits.',
            code='invalid_phone_number'
        )
    ],
    )
    
    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Profile for {self.user.username}'

