from dotenv import load_dotenv
import os

load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY')

ACCESS_TOKEN_EXPIRE_MINUTES = 5
REFRESH_TOKEN_EXPIRE_DAYS = 7
ALGORITHM = "HS256"

