from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['ENV'] = os.getenv('FLASK_ENV')
app.config['DEBUG'] = os.getenv('DEBUG') == 'True'

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

@app.route('/')
def index():
    return render_template("index.html", api_key=GOOGLE_MAPS_API_KEY)
