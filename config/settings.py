"""Django settings for config project."""

import dotenv
import os
import dj_database_url
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

load_dotenv(dotenv_path)  # loads the configs from .env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = str(os.getenv('SECRET_KEY'))

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com'
    "*.ngrok-free.app"

]

# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',
]


    ##local app
LOCAL_APPS = [
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'order.apps.OrderConfig',
    'coupons.apps.CouponsConfig',
    'about.apps.AboutConfig',
    'contactUs',
    'accounts',
    'defender',
    "verify_email.apps.VerifyEmailConfig",
    "captcha"
]

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'defender.middleware.FailedLoginMiddleware',
]

ROOT_URLCONF = 'config.urls'


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# load environment variables from .env
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# load database from the DATABASE_URL environment variable
DATABASES = {}
DATABASES['default'] = dj_database_url.config()


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'config' ,'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'


#Crispy templates for form rendering
CRISPY_TEMPLATE_PACK = 'bootstrap4'

CART_SESSION_ID = 'cart'

# settings.py
AUTH_USER_MODEL = 'accounts.CustomUser'

LOGOUT_REDIRECT_URL = 'accounts:login'

LOGIN_REDIRECT_URL = "shop:product_list"

DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

# EMAIL VIRFYING SECTION ##################################################################

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # default authentication backend
    'accounts.backend.CustomEmailBackend',
    ]
# For Django Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'qstarsy@gmail.com'
EMAIL_HOST_PASSWORD = str(os.getenv('GOOGLE_SECRET'))  # os.environ['password_key'] suggested

EXPIRE_AFTER = "1h" 
MAX_RETRIES = 4
LOGIN_URL = 'accounts:login'

HTML_MESSAGE_TEMPLATE = "html-message-template.html"
VERIFICATION_SUCCESS_TEMPLATE = "VERIFICATION_SUCCESS_TEMPLATE.html"
VERIFICATION_FAILED_TEMPLATE = "VERIFICATION_FAILED_TEMPLATE.html"
REQUEST_NEW_EMAIL_TEMPLATE = "REQUEST_NEW_EMAIL_TEMPLATE.html"
LINK_EXPIRED_TEMPLATE  = "LINK_EXPIRED_TEMPLATE.html"
NEW_EMAIL_SENT_TEMPLATE = "NEW_EMAIL_SENT_TEMPLATE.html"
# EMAIL VIRFYING SECTION ##################################################################
