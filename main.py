import os
import openai
from config import *
from stream_gcp import StartTalking

openai.api_key = OPENAI_API_KEY

from utils import *

talk = StartTalking()
talk.start()


test = openai.Model.list()

