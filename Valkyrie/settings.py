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

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'admin.mealsloth.com']

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/login/'

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'wi=od%+rgt^bdabhp3qdq)b!xb0+_q2^faa$dkh65wja-%j&n+'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Valkyrie.urls'

WSGI_APPLICATION = 'Valkyrie.wsgi.application'

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
    'Valkyrie',
    '_include.Chimera.Chimera',
    '_include.Siren.Siren',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

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

CACHES = {
    'default': {
        'BACKEND': 'Valkyrie.gae_memcached_cache.GaeMemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Google Cloud Storage

GCS_CLIENT_ID = 'mealsloth-chimera-ap01-cloudstorage-bu01'

GCS_CLIENT_KEY = 'GOOG257P2OBJ6JUKAPST'

GCS_CLIENT_SECRET = '3i8tSK69upv1aWEW0tCxBwj0/HST0/ladjxNpjG8'

LIBCLOUD_PROVIDERS = {
    'google': {
        'type': 'libcloud.storage.types.Provider.GOOGLE_STORAGE',
        'user': 'mealsloth-chimera-ap01',
        'key': GCS_CLIENT_KEY,
        'bucket': GCS_CLIENT_ID,
    }
}

GOOGLE_CLOUD_STORAGE_BUCKET = '/' + GCS_CLIENT_ID
GOOGLE_CLOUD_STORAGE_URL = 'http://storage.googleapis.com/'
GOOGLE_CLOUD_STORAGE_DEFAULT_CACHE_CONTROL = 'public, max-age: 7200'

DEFAULT_FILE_STORAGE = 'google.storage.google_cloud.GoogleCloudStorage'
