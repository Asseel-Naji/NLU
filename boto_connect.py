import boto3
import json
import time
import os
from dotenv import load_dotenv

load_dotenv("secrets/.env")

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

session = boto3.Session(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


def extract():
    with open("./random_tests/transcript.txt", "r") as f:
        text = f.read()

    print(text[19:25])
    comprehend = session.client(service_name="comprehend", region_name="eu-central-1")
    # text =data
    print(text)

    print("Calling DetectEntities")
    ents = comprehend.detect_entities(Text=text, LanguageCode="ar")
    ents = ents["Entities"]
    print(ents)
    print(type(ents))
    print("End of DetectEntities\n")

    for entity in ents[-10:]:
        with open("./random_tests/entities.txt", "a") as f:
            f.write(entity["Text"] + " : ")
            f.write(entity["Type"])
            f.write("\n")


while True:
    time.sleep(1)
    extract()
    time.sleep(3)
