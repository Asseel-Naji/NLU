"""This module is just to keep the config in one place"""
import os
from dotenv import load_dotenv

load_dotenv("secrets/.env")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./secrets/gkey.json"
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


RATE = 16000
CHUNK = int(RATE / 10)
