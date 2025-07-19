from flask import Flask, render_template, jsonify
import json
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['ENV'] = os.getenv('FLASK_ENV')
app.config['DEBUG'] = os.getenv('DEBUG') == 'True'

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_congestion_zone():
    """封裝：從 GeoJSON 讀取 CCZ 邊界"""
    with open('data/cczone.geojson') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template("index.html", api_key=GOOGLE_MAPS_API_KEY)

@app.route('/cczone')
def cczone():
    zone_data = get_congestion_zone()
    return jsonify(zone_data)

if __name__ == '__main__':
    app.run(debug=True)
