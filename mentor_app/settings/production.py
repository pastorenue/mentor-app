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