"""
Django settings for djtwapp project.
Generated by 'django-admin startproject' using Django 2.1.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import json

import django_heroku
import tweepy
import firebase_admin
from firebase_admin import credentials

from . import constants

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Firebase setup
if "DEPLOY" in os.environ.keys():
    firebase_credentials = {}
    firebase_credentials["private_key"]=os.environ["private_key"].replace('/\\n/g', '\n'),
    firebase_credentials["private_key_id"]=os.environ["private_key_id"]
    firebase_credentials["client_email"]=os.environ["client_email"]
    firebase_credentials["client_id"]=os.environ["client_id"]
    firebase_credentials["client_x509_cert_url"]=os.environ["client_x509_cert_url"]
    firebase_credentials["type"]=os.environ["type"]
    firebase_credentials["project_id"]=os.environ["project_id"]
    firebase_credentials["auth_uri"]=os.environ["auth_uri"]
    firebase_credentials["token_uri"]=os.environ["token_uri"]
    firebase_credentials["auth_provider_x509_cert_url"]=os.environ["auth_provider_x509_cert_url"]
else:
    firebase_credentials = BASE_DIR+"/firebase_credentials.json"

CRED = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(CRED, {'databaseURL': 'https://djtwapp.firebaseio.com'})

# Tweepy keys
CONSUMER_KEY = constants.CONSUMER_KEY
CONSUMER_SECRET = constants.CONSUMER_SECRET

ACCESS_TOKEN = constants.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = constants.ACCESS_TOKEN_SECRET

AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Tweepy API
TWEEPY_API = tweepy.API(AUTH)

# Tweepy exceptions
RATE_LIMIT_ERROR = tweepy.RateLimitError
TWEEP_ERROR = tweepy.TweepError


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#(_*2fl%tei_s^e5q86lljh4&wz)cf&y0%er!8==7f!0pm2lex'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "https://djtwapp.herokuapp.com/"]


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'profiles',
]


AUTH_USER_MODEL = "accounts.User"

# redirect urls
LOGIN_URL = "/accounts/login/"

REGISTER_REDIRECT_URL= "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djtwapp.urls'

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

WSGI_APPLICATION = 'djtwapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Activate Django-Heroku.
django_heroku.settings(locals())
