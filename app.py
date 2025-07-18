from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

def get_congestion_zone():
    """封裝：從 GeoJSON 讀取 CCZ 邊界"""
    with open('data/cczone.geojson') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cczone')
def cczone():
    zone_data = get_congestion_zone()
    return jsonify(zone_data)

if __name__ == '__main__':
    app.run(debug=True)
