from django.conf import settings
from django.core.management import call_command

def before_all(context):
    settings.DEBUG = True
    settings.INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'my_ecommerce',
    ]
    call_command('makemigrations')
    call_command('migrate')