import os
import openai
from dotenv import load_dotenv


load_dotenv()

OPENAI_API = os.getenv('OPENAI_API')
OPENAI_ORG = os.getenv('OPENAI_ORG')
openai.api_key = os.getenv("OPENAI_API_KEY")


openai.Model.list()