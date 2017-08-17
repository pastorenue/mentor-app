


import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


DEBUG = False
ALLOWED_HOSTS =  ['thebossoffice.herokuapp.com', '.thebossoffice.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# add this
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
SECRET_KEY = os.environ.get('SECRET_KEY', 'swsdw313!@-2esdwq34{_3dse)&^^<t364551wdreqwe2')

ADMINS = (
    ('Pastor Emmanuel', 'pastorenuel@gmail.com'),
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #install apps 
    'accounts',
    'mentee',
    'mentor',
    'expert',
    'contacts',
    'sorl.thumbnail',
    'states'
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
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
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

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

#Login Credentials and urls
LOGIN_URL = 'login' #reverse_lazy('login') ##VERY HARMFUL TO LOGINREQUIRED VIEWS
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

PAGE_SIZE = 20
PAGE_ORPHANS = 5        

#Email_configuration
DEFAULT_FROM_EMAIL = 'noreply@thebossoffice.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '' #'emails.address.email_addr'

