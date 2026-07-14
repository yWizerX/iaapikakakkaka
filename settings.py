import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'chave-secreta-provisoria-para-o-render'
DEBUG = False
ALLOWED_HOSTS = ['*'] # Permite que o Render acesse a aplicação externamente

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'
