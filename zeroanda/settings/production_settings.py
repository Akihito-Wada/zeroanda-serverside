from .sandbox_settings import *

MODE    = 'production'

DOMAIN = 'https://api-fxtrade.oanda.com'
STREAMING_DOMAIN = 'https://stream-fxtrade.oanda.com'

TOKEN = "750d435f29ec40a4063eb0af6320cddc-40a0e6447f155e74cb50c6077a278d20"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zeroanda',
        'USER': 'wadaakihito',
        'PASSWORD': '',
        'HOST': 'localhost',
        'AUTOCOMMIT': True,
    }
}