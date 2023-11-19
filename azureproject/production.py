import os
import sys
from .settings import *  # noqa
from .settings import BASE_DIR
from socket import gethostname, gethostbyname

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] + [gethostname(), gethostbyname(gethostname())] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] + [gethostname(), gethostbyname(gethostname())] if 'WEBSITE_HOSTNAME' in os.environ else []
DEBUG = False

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add whitenoise middleware after the security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = INSTALLED_APPS + [
    'storages'
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': conn_str_params['dbname'],
        'HOST': conn_str_params['host'],
        'USER': conn_str_params['user'],
        'PASSWORD': conn_str_params['password'],
    }
}


# For hosting of media files
DEFAULT_FILE_STORAGE = 'backend.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'backend.custom_azure.AzureStaticStorage'

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

AZURE_ACCOUNT_NAME = "dronereconstorage"
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'


# Recaptchu
GOOGLE_RECAPTCHA_SITE_KEY = os.environ['GOOGLE_RECAPTCHA_SITE_KEY']
GOOGLE_RECAPTCHA_SECRET_KEY = os.environ['GOOGLE_RECAPTCHA_SECRET_KEY']


#Logging
if not DEBUG:
    LOGGING = {
        'version': 1,
        "handlers": {
            "azure": {
                "level": "DEBUG",
                "class": "opencensus.ext.azure.log_exporter.AzureLogHandler",
                'connection_string': os.environ['APPLICATIONINSIGHTS_CONNECTION_STRING']
            },
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '.logs/debug_server.log',
                'formatter': 'simple',
            },
        },
        "loggers": {
            "django": {"handlers": ["azure", "console",'file']},
        },
        'formatters': {
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            }
        }
    }
else:
    LOGGING = {
        'version': 1,
        'loggers': {
            'django': {
                'handlers': ['file','console'],
                'level': 'DEBUG'
            },
        },
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '.logs/debug.log',
                'formatter': 'simple',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'formatters': {
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            }
        }
    }