import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_lyrics(theme, event, relationship, language):
    """
    Generates song lyrics using GPT-4 based on user input.

    :param theme: Theme of the song (e.g., romantic, funny)
    :param event: The occasion (e.g., birthday, anniversary)
    :param relationship: Who the song is for (e.g., wife, friend)
    :param language: Language of the song lyrics
    :return: Generated song lyrics as a string
    """
    prompt = f"Write a {theme} song for a {event} about my {relationship} in {language}."
    
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    
    return response.choices[0].text.strip()

