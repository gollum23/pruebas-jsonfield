from .settings import *
SECRET_KEY = 'wu2)67kguhkt6t%loe1kxo^x*-gew%h%853g%gj0w@@myj&on8'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS += [
    'django_nose',
    # 'debug_toolbar',
    # 'debug_panel',
]
# Tell nose to measure coverage on the 'foo' and 'bar' apps
DEBUG_TOOLBAR_PATCH_SETTINGS = False
# MIDDLEWARE_CLASSES += ('debug_panel.middleware.DebugPanelMiddleware',)

INTERNAL_IPS = ('172.18.0.1',)

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=.',
    '--cover-html',
]
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
)
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DB_NAME', 'jsonfield'),
        'USER': os.environ.get('DB_USERNAME', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'platzi'),
        'HOST': os.environ.get('DB_HOST', 'jsonfield-postgresql'),
        'PORT': os.environ.get('DB_PORT', '5432')
    }
}
