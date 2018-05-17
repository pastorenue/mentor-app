"""
Django settings for mentor_app project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

ADMINS = (
    ('Pastor Emmanuel', 'pastorenuel@gmail.com'),
)

DEBUG = True   
SECRET_KEY = os.environ.get('SECRET_KEY', 'i-a=nwysyhwu8^xhck3k78oar=%fryvcn^5c7n7m-_=a6+!2-6')
EMAIL_HOST_PASSWORD = ''
ALLOWED_HOSTS = ['.thebossoffice.com', '138.68.145.121', 'localhost']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'thebossoffice',
#         'USER': 'theboss_admin',
#         'PASSWORD': 'Welcome*234',
#         'HOST': 'localhost',
#         'PORT': ''
#         }
# }

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #install apps
    'accounts',
    'forum',
    'mentee',
    'mentor',
    'expert',
    'contacts',
    'sorl.thumbnail',
    'states',
    'anymail',
    'notifications',
    'newsroom',
    'tinymce',
    'newsletters',
    'django_messages',  
    'django_summernote'
  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mentor_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(PROJECT_DIR, 'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.trending_data',
                'django_messages.context_processors.inbox',
            ],
        },
    },
]

WSGI_APPLICATION = 'mentor_app.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AGE_RANGE_CHOICES = (
    ('25-30', '25-30 years'),
    ('31-35', '31-35 years'),
    ('36-40', '36-40 years'),
    ('41-50', '41-50 years'),
    ('51-60', '51-60 years'),
    ('60+', '60+ years')

)
TITLE_CHOICES = (
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Miss', 'Miss'),
    ('Dr.', 'Dr.'),
    ('Prof.', 'Prof.'),
    ('Alhaji', 'Alhaji'),
    ('Chief', 'Chief'),
    ('Prince', 'Prince'),
    ('Princess', 'Princess')
)
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

#Login Credentials and urls
LOGIN_URL = '/auth/login' #reverse_lazy('login') ##VERY HARMFUL TO LOGINREQUIRED VIEWS
LOGIN_REDIRECT_URL = 'mentee:mentee-list'
LOGOUT_REDIRECT_URL = '/auth/login'

PAGE_SIZE = 20
PAGE_ORPHANS = 5
TOP_READ_SIZE = 15

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": os.environ.get("MAILGUN_API_KEY", "key-5b8244a85dd4969806098365b885bf55"),
    "MAILGUN_SENDER_DOMAIN": 'thebossoffice.com',  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'postmaster@thebossoffice.com'
EMAIL_HOST_PASSWORD = '6a2325ce9d3215a77a7823540ba0422f'
EMAIL_USE_TLS = True

TEMPLATE_DEBUG=True

#Newsletter settings
NEWSLETTER_CONFIRM_EMAIL = False
SITE_ID=2
DEFAULT_DOMAIN = "thebossoffice.com"

