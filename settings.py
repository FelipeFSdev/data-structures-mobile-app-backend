import os
from os.path import dirname, join
from dotenv import load_dotenv


dotenv_path = join(dirname(".env"), ".env")
load_dotenv(dotenv_path)

DB_URL = os.environ.get("DB_URL")
JWT_KEY = os.environ.get("JWT_KEY")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
HASH_KEY = os.environ.get("HASH_KEY")
