from django.urls import path
from . import views

app_name = 'errorhandler'

urlpatterns = [
    path('403/', views.you_dont_have_permission, name='error_403'),
]