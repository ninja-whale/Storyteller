from transformers import pipeline
import requests
from urllib import request
from PIL import Image

def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    image_path = './static/input_image.jpg'
    request.urlretrieve(url, image_path)
    input_file = Image.open(open(image_path, 'rb'))
    text = image_to_text(input_file, max_new_tokens=50)
    tex = text[0]['generated_text']
    return tex

def generate_story(scenario):
    generator = pipeline("text-generation", model="distilgpt2")
    story = generator(scenario, min_length=100, max_length=150, num_return_sequences=1)
    return story[0]['generated_text']


def text_to_speech(story):
    API_URL = "API"
    headers = {"Authorization": "__"}

    payload = {
        "inputs": story
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    with open('static/audio.mp3', 'wb') as file:
        file.write(response.content)

def inputer(url):
    sce = img2text(url)
    s = generate_story(sce)
    text_to_speech(s)
    return s


