"""
Django settings for myblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vtt4)wt5ug9u9pyich2#^$4w2awb8l60^4d513@aw3gfqp7od#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'article',
    #'south',
    'disqus',
)

DISQUS_API_KEY = 'LH9KQW0fXhZ7wFWDaw745lLbPMb2XbCYEqxnoyJcKDG9f1X2GhGCsh8wUSpzyYZG'
DISQUS_WEBSITE_SHORTNAME = 'wxublog'

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
	'django.core.context_processors.request',
)

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myblog.urls'

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'myblog',
#	'USER': 'root',
#        'PASSWORD': 'nettuts',
#	'HOST':'',
#	'PORT':'',
    }
}


#parse database configureation from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

#Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#Simplified static file serving.
# https://warehouse.python.org/project/whitenoise

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


import os.path
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__)) # this is not Django setting.
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
    # here you can add another templates directory if you wish.
)


SITE_ID = 1
