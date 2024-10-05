import openai

# Initialize OpenAI API key
# openai.api_key = 'sk-UMN6GqNHPbBtZH932Uep8Y4h49NHvD65DuMBmVliqBT3BlbkFJuV618N8TPajTvf9xCWyGevc-v9v2IMqz-TN3XSgC0A'

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

