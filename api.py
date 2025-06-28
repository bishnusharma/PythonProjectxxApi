from flask import Flask, jsonify, send_from_directory, render_template
import json
import os

app = Flask(__name__)

def load_locations():
    with open('places.json', 'r') as f:
        return json.load(f)

@app.route('/')
def welcome():
    return "Welcome to Nepal Locations API!<br><br>" \
           "<a href='/locations'>View all locations</a><br>" \
           "<a href='/locations/1'>View Pokhara</a>"

@app.route('/locations')
def get_locations():
    locations = load_locations()
    return render_template('locations.html', locations=locations)

@app.route('/locations/<int:location_id>')
def get_location(location_id):
    locations = load_locations()
    location = next((loc for loc in locations if loc["id"] == location_id), None)
    if location:
        return render_template('location.html', location=location)
    return "Location not found", 404

@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    os.makedirs('static/images', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True)