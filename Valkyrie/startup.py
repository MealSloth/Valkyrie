from django.core.exceptions import MiddlewareNotUsed
from django.core.management import call_command
import MySQLdb as Mdb


class StartupMiddleware(object):
    def __init__(self):
        Mdb.connect()
        call_command('syncdb', interactive=False)
        raise MiddlewareNotUsed('Startup complete')
