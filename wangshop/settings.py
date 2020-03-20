"""
Django settings for wangshop project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3+ps$=$u^egavs9rxal+%8g_9#^&ux^s*39-*tfg$nmeem$cp5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
APPEND_SLASH = False
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    # 'rest_framework.pagination',
    'account.apps.AccountConfig',
    'common',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wangshop.urls'
AUTH_USER_MODEL = 'account.MyUser'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'wangshop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop',
        'USER': 'root',
        'PASSWORD': '19981008',
        'HOST': '47.106.77.191',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
TIME_ZONE = 'Asia/Shanghai'

DATETIME_FORMAT = 'Y-m-d H:i:s'

DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'H:i:s'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
)
try:
    from .local_settings import *
except Exception as e:
    pass

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'detail': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d[%(pathname)s:%(lineno)d] %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s [%(pathname)s:%(lineno)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s [%(lineno)d] %(message)s'
        },
        'operation': {
            'format': '[%(asctime)s] %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log', 'main.log'),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 30,  # 30MB
            'backupCount': 50,
        },
        'biz_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log', 'biz.log'),
            'formatter': 'operation',
            'maxBytes': 1024 * 1024 * 30,  # 30MB
            'backupCount': 50,
        },
        'trade_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log', 'trade.log'),
            'formatter': 'operation',
            'maxBytes': 1024 * 1024 * 30,  # 30MB
            'backupCount': 50,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'my.server': {
            'handlers': ['console', 'file'] if DEBUG else ['file'],
            'level': 'DEBUG' if DEBUG else 'DEBUG'  # 'INFO'
        },
        'my.biz': {
            'handlers': ['console', 'biz_file'] if DEBUG else ['biz_file'],
            'level': 'DEBUG' if DEBUG else 'DEBUG'  # 'INFO'
        },
        'my.trade': {
            'handlers': ['console', 'trade_file'] if DEBUG else ['trade_file'],
            'level': 'DEBUG' if DEBUG else 'DEBUG'  # 'INFO'
        }
    }
}
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'wangshop.utils.authentication.CsrfExemptSessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'EXCEPTION_HANDLER': 'wangshop.utils.exception_handler.my_exception_handler',
}

# 跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
