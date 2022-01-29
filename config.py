import os
from dotenv import load_dotenv


class Config:
    load_dotenv(dotenv_path="secrets.env")
    DEBUG = os.getenv("FLASK_DEBUG")

    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

    MONGODB_HOST = os.getenv("FLASK_MONGODB_HOST")
