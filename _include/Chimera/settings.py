from databases import databases
import os


PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Michael', 'michael@mealsloth.com'),
)

MANAGERS = ADMINS

DATABASES = databases()

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'api.mealsloth.com']

SECRET_KEY = '$cl98j&&uh&h5$)zrj(mp62)-$(thx%r4+phj_fh(za6g0al!u'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Chimera.urls'

WSGI_APPLICATION = 'Chimera.wsgi.app'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Chimera'
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Google Cloud Storage

LIBCLOUD_PROVIDERS = {
    'google': {
        'type'  : 'libcloud.storage.types.Provider.GOOGLE_STORAGE',
        'user'  : 'mealsloth-chimera-ap01',
        'key'   : 'GOOG257P2OBJ6JUKAPST',
        'bucket': 'mealsloth-chimera-ap01-cloudstorage-bu-01',
    }
}

DEFAULT_LIBCLOUD_PROVIDER = 'google'
DEFAULT_FILE_STORAGE = 'storages.backends.apache_libcloud.LibCloudStorage'
STATICFILES_STORAGE = 'storages.backends.apache_libcloud.LibCloudStorage'

GOOGLE_STORAGE = 'gs'

LOCAL_FILE = 'file'

CLIENT_ID = 'mealsloth-chimera-ap01-cloudstorage-bu01'

CLIENT_KEY = 'GOOG257P2OBJ6JUKAPST'

CLIENT_SECRET = '3i8tSK69upv1aWEW0tCxBwj0/HST0/ladjxNpjG8'
