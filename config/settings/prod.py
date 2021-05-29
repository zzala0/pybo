from .base import *


ALLOWED_HOSTS = ['localhost', '*.zzala.myds.me']

CSRF_TRUSTED_ORIGINS = ['*.zzala.myds.me']

STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []

# DEBUG = False