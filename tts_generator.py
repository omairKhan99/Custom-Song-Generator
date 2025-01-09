#I will use this Text-to-Speech API to generate vocals from the lyrics

from gtts import gTTS
import os

def generate_voice(lyrics, language):
    """
    Converts text (lyrics) to speech using gTTS and saves it as an MP3 file.

    :param lyrics: The generated lyrics to convert to speech
    :param language: The language for the speech synthesis (e.g., 'en' for English, 'es' for Spanish)
    :return: The filename of the generated MP3 file
    """
    tts = gTTS(text=lyrics, lang=language)
    filename = "output_song.mp3"
    tts.save(filename)
    
    return filename
