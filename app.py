from flask import Flask, render_template, request, send_file, jsonify
from lyrics_generator import generate_lyrics
from tts_generator import generate_voice
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_song():
    name = request.form['name']
    occasion = request.form['occasion']
    relationship = request.form['relationship']
    language = request.form['language']
    theme = request.form['theme']

    lyrics = generate_lyrics(theme, occasion, relationship, language)
    
    # Insert user's name in the song's lyrics
    personalized_lyrics = lyrics.replace("[name]", name)
    
    song_file = generate_voice(personalized_lyrics, language)
    
    # Return JSON data with the lyrics and song file path
    return jsonify({'lyrics': personalized_lyrics, 'song_file': song_file})

@app.route('/download_lyrics', methods=['POST'])
def download_lyrics():
    lyrics = request.form['lyrics']
    file_path = "song_lyrics.txt"
    
    with open(file_path, "w") as file:
        file.write(lyrics)
    
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
