from flask import Flask, render_template, request, send_file
import openai
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

