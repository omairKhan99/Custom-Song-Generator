from flask import Flask, render_template, request, send_file
from lyrics_generator import generate_lyrics
from tts_generator import generate_voice

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
    
    song_file = generate_voice(lyrics, language)
    
    return send_file(song_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
