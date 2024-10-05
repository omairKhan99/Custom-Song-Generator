from flask import Flask, render_template, request, send_file
from lyrics_generator import generate_lyrics
from tts_generator import generate_voice

