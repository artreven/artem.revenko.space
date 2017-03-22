# Import some utility functions
from os.path import join
# Fetch our common settings
from .base import *

# #########################################################

# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

ALLOWED_HOSTS = []


# ##### DATABASE CONFIGURATION ############################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# ##### APPLICATION CONFIGURATION #########################
