from .base_settings import *

# Debugging settings...
DEBUG = True
TEMPLATE_DEBUG = True

# Database settings...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'scopeinitial',
        'PASSWORD': 'ogpss2011',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres'
    }
}