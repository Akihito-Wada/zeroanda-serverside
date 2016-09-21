from .sandbox_settings import *

# zeroanda settings.
DEBUG = False
#
ALLOWED_HOSTS = ['*',]

MODE    = 'practice'

TEST = False

DOMAIN = 'https://api-fxtrade.oanda.com'
STREAMING_DOMAIN = 'https://stream-fxtrade.oanda.com'

TOKEN = "750d435f29ec40a4063eb0af6320cddc-40a0e6447f155e74cb50c6077a278d20"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zeroanda',
        'USER': 'wadaakihito',
        'PASSWORD': 'fukuronomono1',
        'HOST': 'i-2ccfc9b3-postgres-test.cedwl7sfyyos.ap-northeast-1.rds.amazonaws.com',
        'AUTOCOMMIT': True,
    }
}