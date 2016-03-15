from .sandbox_settings import *

# zeroanda settings.
# DEBUG = False
#
# ALLOWED_HOSTS = ['*',]

MODE    = 'practice'

DOMAIN = 'https://api-fxpractice.oanda.com'
STREAMING_DOMAIN = 'https://stream-fxpractice.oanda.com'

TOKEN = "8713400a434b3f4cfd2e2f9580da45ed-41a3452617aa84f441be90ca6ab0fc55"

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'dev_reversid'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dev_zeroanda',
        'USER': 'wadaakihito',
        'PASSWORD': '',
        'HOST': 'localhost',
        'AUTOCOMMIT': True,
    }
}