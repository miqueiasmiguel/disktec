import environ

from disktec_system.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}

# AWS

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")

AWS_S3_FILE_OVERWRITE = env.bool("AWS_S3_FILE_OVERWRITE", False)
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = env("DEFAULT_FILE_STORAGE")
