import os

G1 = True
USE_PROD_DB = False
USE_LOCAL_DB = not USE_PROD_DB


def databases():
    dbs = {}

    # Chimera db

    if G1:
        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
            dbs.update({
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '/cloudsql/mealsloth-chimera-ap01:mealsloth-chimera-ap01-cloudsqlg1-in02',
                    'NAME': 'chimera_prod01',
                    'USER': 'root',
                }
            })
        elif os.getenv('SETTINGS_MODE') == 'prod' or USE_PROD_DB is True:
            dbs.update({
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '173.194.108.241',
                    'NAME': 'chimera_prod01',
                    'USER': 'generic',
                    'PASSWORD': 'ZtuQGCRWhWpaLtV6e93kD59uWjjC8r',
                }
            })
        else:
            dbs.update({
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'chimera_prod01',
                    'USER': 'root',
                    'HOST': 'localhost',
                    'PORT': '3306',
                }
            })
    else:
        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
            dbs.update({
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '/cloudsql/mealsloth-chimera-ap01:mealsloth-chimera-ap01-cloudsqlg2-in01',
                    'NAME': 'chimera_prod01',
                    'USER': 'root',
                    'PASSWORD': 'HSnwYMVq53ZR7vfdRU39QhPk32H77yra',
                }
            })
        elif os.getenv('SETTINGS_MODE') == 'prod' or USE_PROD_DB is True:
            dbs.update({
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '104.196.63.245	',
                    'NAME': 'chimera_prod01',
                    'USER': 'root',
                    'PASSWORD': 'HSnwYMVq53ZR7vfdRU39QhPk32H77yra',
                }
            })
        else:
            dbs.update({
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'chimera_prod01',
                    'USER': 'root',
                    'HOST': 'localhost',
                    'PORT': '3306',
                }
            })

    # Siren db

    if G1:
        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
            dbs.update({
                'siren': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '/cloudsql/mealsloth-chimera-ap01:mealsloth-chimera-ap01-cloudsqlg1-in02',
                    'NAME': 'siren_prod01',
                    'USER': 'root',
                }
            })
        else:
            dbs.update({
                'siren': {
                    'ENGINE': 'django.db.backends.mysql',
                    'HOST': '173.194.108.241',
                    'NAME': 'siren_prod01',
                    'USER': 'generic',
                    'PASSWORD': 'ZtuQGCRWhWpaLtV6e93kD59uWjjC8r',
                }
            })

    return dbs
