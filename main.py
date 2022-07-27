import os
import openai
from dotenv import load_dotenv


load_dotenv("secrets/.env")

OPENAI_API = os.getenv('OPENAI_API')
OPENAI_ORG = os.getenv('OPENAI_ORG')
openai.api_key = os.getenv("OPENAI_API_KEY")


test = openai.Model.list()

print(test)

