import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


AUTH_USER_MODEL = 'clients.CustomUser'

SECRET_KEY = 'django-insecure-38-lgtufsimbflg=3*0x&qres_u_oota+@%km9e&b6*39n)l7+'

DEBUG = True

ALLOWED_HOSTS = ['*',]


DJANGO_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'products',
    'clients',
    'orders',
]

THIRD_PARTY_APPS = [
    'modeltrans',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters',
    'drfpasswordless',
    'drf_yasg',
    'versatileimagefield',
    'debug_toolbar',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


INTERNAL_IPS = [
    "127.0.0.1",
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DATE_FORMAT': '%d-%b-%Y',
}


PASSWORDLESS_AUTH = {
   'PASSWORDLESS_AUTH_TYPES': 'MOBILE',
   'PASSWORDLESS_SMS_CALLBACK': 'clients.utils.send_sms_with_callback_token',
}


ROOT_URLCONF = 'core.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'), 
#         'PASSWORD': os.environ.get('DB_PASS'),
#         'HOST': os.environ.get('DB_HOST'), 
#         #'PORT': '5432',
#     }
# }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
    ('uz', 'Uzbek'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'product_headshot': [
        ('full_size', 'url'),
        ('thumbnail', 'thumbnail__100x100'),
        ('medium_square_crop', 'crop__400x400'),
        #('small_square_crop', 'crop__50x50')
    ]
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGGING = {
    'version': 1,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'}
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}


X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True