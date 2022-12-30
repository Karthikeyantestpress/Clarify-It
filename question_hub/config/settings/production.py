from config.env import env

from .base import *

DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["question_hub.com", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": env("DATABASE_ENGINE"),
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
    }
}
