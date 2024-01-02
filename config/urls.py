"""config URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/defender/', include('defender.urls')), # defender admin
    

    path('hide-me-dont-show-me-fuck-you-if-you-got-it/', admin.site.urls),
    
    
    path('cart/', include('cart.urls', namespace='cart')),
    path('accounts/', include('accounts.urls')), 
    path('order/', include('order.urls', namespace='order')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('verification/', include('verify_email.urls' , namespace='verify_email')),	
    # path('error/', include('errorhandler.urls', namespace='error')),
    path('', include('about.urls', namespace='about-us')),
    path('', include('contactUs.urls')),
    path('', include('shop.urls', namespace='shop')),
    path('captcha/', include('captcha.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)