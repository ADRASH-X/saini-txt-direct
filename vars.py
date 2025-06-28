#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "13460015"))
API_HASH = environ.get("API_HASH", "bd452af645d2a569f654f70b366ce577")
BOT_TOKEN = environ.get("BOT_TOKEN", "7884870907:AAEWL7PppE7-hj8KOc9B8-0kGPodlBZbH58")
OWNER = int(environ.get("OWNER", "5431970720"))
CREDIT = "HmGamer"
AUTH_USER = os.environ.get('AUTH_USERS', '5431970720').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
