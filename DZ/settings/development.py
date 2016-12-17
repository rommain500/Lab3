from settings.production import *

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
]

AUTH_PASSWORD_VALIDATORS = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s:%(module)s:%(asctime)s: %(message)s',
        },
        'verbose_with_pid': {
            'format': '%(levelname)s:%(module)s:%(asctime)s [PID %(process)s]: %(message)s',
        },
        'simple': {
            'format': '%(levelname)s:%(module)s: %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file_log': {
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'verbose',
            'level': 'DEBUG',
            'filename': '/logs/iu551.log',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file_log'],
            'level': 'DEBUG',
        },
        'django.db': {
            'handlers': ['console', 'file_log'],
            'level': 'DEBUG',
        },
    },
}
