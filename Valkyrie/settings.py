import os


PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

DEBUG = False
USE_PROD_DB = False
USE_LOCAL_DB = not USE_PROD_DB
TEMPLATE_DEBUG = DEBUG

G1 = True

ADMINS = (
    ('Michael', 'michael@mealsloth.com'),
)

MANAGERS = ADMINS

if G1:
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'HOST': '/cloudsql/mealsloth-chimera-ap01:mealsloth-chimera-ap01-cloudsqlg1-in02',
                'NAME': 'chimera_prod01',
                'USER': 'root',
            }
        }
    elif os.getenv('SETTINGS_MODE') == 'prod' or USE_PROD_DB is True:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'HOST': '173.194.108.241',
                'NAME': 'chimera_prod01',
                'USER': 'generic',
                'PASSWORD': 'ZtuQGCRWhWpaLtV6e93kD59uWjjC8r',
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'chimera_prod01',
                'USER': 'root',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
else:
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'HOST': '/cloudsql/mealsloth-chimera-ap01:mealsloth-chimera-ap01-cloudsqlg2-in01',
                'NAME': 'chimera_prod01',
                'USER': 'root',
                'PASSWORD': 'HSnwYMVq53ZR7vfdRU39QhPk32H77yra',
            }
        }
    elif os.getenv('SETTINGS_MODE') == 'prod' or USE_PROD_DB is True:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'HOST': '104.196.63.245	',
                'NAME': 'chimera_prod01',
                'USER': 'root',
                'PASSWORD': 'HSnwYMVq53ZR7vfdRU39QhPk32H77yra',
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'chimera_prod01',
                'USER': 'root',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'admin.mealsloth.com']

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

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

MIDDLEWARE_CLASSES = (
    # 'Valkyrie.startup.StartupMiddleware',
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
    '_include.Chimera',
    'Valkyrie',
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
