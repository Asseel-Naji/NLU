from google.cloud import speech, translate
from config import *

import os
import openai


def amazonify(*args, **kwargs):
    print("here comes the log writing function")
    def inner(func):
        # code functionality here
        print("here will be the before function")
        print("here will be the after function")

    # returning inner function
    return inner


def translate_text(text, project_id="shining-reality-357514"):
    """Translating Text."""

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    # Translate text from English to French
    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": "ar-JO",
            "target_language_code": "en",
        }
    )

    # Display the translation for each input text provided
    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))
        with open("./random_tests/trans.txt", "w") as f:
            f.write(str(translation.translated_text))

        return(complete_product(text))
prompt_products = """I feel tired when I set for a long time on the computer:
A standup desk.

I feel blinded when I walk in the sun:
summer sunglasses.

I want to be faster at typing:
A mechanical keyboard.

"""


def complete_product(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt_products + text + ":",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response['choices'][0]['text']
    
# x = complete_product("I want to be faster at driving")

# print(x)