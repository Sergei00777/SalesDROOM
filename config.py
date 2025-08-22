import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Обязательные настройки
SECRET_KEY = 'ваш-очень-секретный-ключ-здесь-измените-это'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'autosalon.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Дополнительные настройки
DEBUG = True