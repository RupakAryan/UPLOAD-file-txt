ab#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29978901"))
API_HASH = environ.get("API_HASH", "500fc876c5356cf04ed3698912dc2edf")
BOT_TOKEN = environ.get("BOT_TOKEN", "8464714544:AAEhz5jgFxhf3_mHy1oHOTynWBDCfSzkIAU")

OWNER = int(environ.get("OWNER", "5776977809"))
CREDIT = environ.get("CREDIT", "blackheart.ex")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7338678521').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5776977809').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set



