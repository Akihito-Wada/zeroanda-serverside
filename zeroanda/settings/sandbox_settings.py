from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'dev_reversid'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dev_zeroanda',
        'USER': 'wadaakihito',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        # 'special': {
        #     '()': 'project.logging.SpecialFilter',
        #     'foo': 'bar',
        # }
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'logging.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     'filters': ['special']
        # },
        'to_file': {
            'formatter': 'verbose',
            'level': 'DEBUG',
            # 'class': 'logging.FileHandler',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            # 'filename': BASE_DIR/'logs/debug.log',
            'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
            # 'maxBytes': 1024 * 1024 * 5,
            'backupCount': 20,
        },
    },
    'loggers': {
        'django': {
            'handlers':['to_file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'trade': {
            'handlers':['to_file'],
            'propagate': True,
            'level':'DEBUG',
        },
        # 'django': {
        #     'handlers':['to_file'],
        #     'propagate': True,
        #     'level':'INFO',
        # },
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': False,
        # },
        # 'myproject.custom': {
        #     'handlers': ['console', 'mail_admins'],
        #     'level': 'INFO',
        #     'filters': ['special']
        # }
    }
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# zeroanda settings.
MODE = 'sandbox'

# Domain.
DOMAIN = 'http://api-sandbox.oanda.com'
STREAMING_DOMAIN = 'http://stream-sandbox.oanda.com'

TOKEN = "ACCESS-TOKEN"

ACCOUNT_ID  = "account_id"