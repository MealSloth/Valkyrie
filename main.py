from google.appengine.ext.webapp import util
from django.conf import settings
import django.core.handlers.wsgi
import django.db


settings._target = None
app = django.core.handlers.wsgi.WSGIHandler()


def main():
    util.run_wsgi_app(app)

if __name__ == '__main__':
    main()
