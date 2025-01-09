from openai import OpenAI

api_key = "123456789"  # Replace this with your actual API key

client = OpenAI(api_key=api_key)

def generate_lyrics(theme, event, relationship, language):
    prompt = f"Write a {theme} song for a {event} about my {relationship} in {language}."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # change to "gpt-3" "gpt-4" 
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes song lyrics."},
            {"role": "user", "content": prompt}
        ]
    )

    lyrics = response.choices[0].message.content.strip()
    return lyrics

if __name__ == "__main__":
    theme = "romantic"
    event = "birthday"
    relationship = "wife"
    language = "English"
    generated_lyrics = generate_lyrics(theme, event, relationship, language)
    
