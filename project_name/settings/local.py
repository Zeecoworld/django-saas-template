# -*- coding: utf-8 -*-
'''
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
'''

from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = os.getenv('DJANGO_DEBUG') #DJANGO_DEBUG


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = os.getenv("SECRET_KEY")

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = os.getenv('DJANGO_EMAIL_PORT')
EMAIL_BACKEND = os.getenv('DJANGO_EMAIL_BACKEND')

# Firebase Configuration
FIREBASE_CREDENTIALS_PATH = os.path.join(ROOT_DIR, 'django-saas.json')
FIREBASE_DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL") #,default="https://django-saas-96901-default-rtdb.firebaseio.com"
# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND' : 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS'       : [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}


# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# Your local stuff: Below this line define 3rd party library settings