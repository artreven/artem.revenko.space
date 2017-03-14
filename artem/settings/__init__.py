from .dev import *

##### DJANGO SECRETS
SECRET_KEY = 'b@(ts_q5x#=x%@+4-dl&ka*xw$kwcqxpe4(k8o16r_#@#2#7de'
DATABASES['default']['PASSWORD'] = 'disambig_password'
DATABASES['default']['USER'] = 'artreven'
DATABASES['default']['NAME'] = 'disambig_db'

# Finally grab the SECRET KEY
try:
    SECRET_KEY
except NameError:
    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
    SECRET_KEY = get_random_string(50, chars)
