"""
Django settings for zeroanda project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9qzl7g@vw%p9bxz=3x(bliha(-unm@rzt6)(4%d%m!t-d@c1@o'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = []

# INSTRUMENTS = ('USD_JPY','EUR_USD','USD_CAD')
INSTRUMENTS = ('EUR_USD',)

WAIT_TIME = 1/2

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'snippets',
    'rest_framework',
    'django_user_agents',
    'zeroanda',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'zeroanda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'zeroanda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ja-jp'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
)

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
    ]
}

# rate
LEVERAGE    = 25
CURRENCY    = 10000

EXPIRY_MINITES = 1  # minutes

TEST_PRESENTATION_DURATION_MINITUS = 30

# DURATION_GET_ACCOUNT_EXCUTE_TIME= -60  # seconds
DURATION_GET_ACCOUNT_EXCUTE_TIME= -15  # seconds

DURATION_GET_PRICE_EXCUTE_TIME  = -10 # seconds

DURATION_IFDOCO_EXCUTE_TIME     = -3  # seconds

# UNTILE_GET_TRANSACTION_EXCUTE_TIME     = EXPIRY_MINITES * 60
# UNTILE_GET_TRANSACTION_EXCUTE_TIME     = EXPIRY_MINITES * 10

GET_TRANSACTION_EXCUTE_TIME = 70 # seconds

# ask
IFDOCO_ASK_ENTRY_POINT = 0.05

ASK_UPPER_BOUND_PROFIT_MARGIN = IFDOCO_ASK_ENTRY_POINT + 0.1

ASK_LOWER_BOUND_PROFIT_MARGIN = IFDOCO_ASK_ENTRY_POINT - 0.05

ASK_STOP_LOSS_MARGIN = IFDOCO_ASK_ENTRY_POINT - 0.1

#bid
IFDOCO_BID_ENTRY_POINT = - 0.05

BID_UPPER_BOUND_PROFIT_MARGIN = IFDOCO_BID_ENTRY_POINT + 0.05

BID_LOWER_BOUND_PROFIT_MARGIN = IFDOCO_BID_ENTRY_POINT - 0.1

BID_STOP_LOSS_MARGIN = IFDOCO_BID_ENTRY_POINT + 0.1

# mail settings
ADMIN_EMAIL = "13southdawn10@gmail.com"

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'system@example.com'

TEST = True

