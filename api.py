from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load locations from JSON file
def load_locations():
    with open('places.json', 'r') as f:
        return json.load(f)

@app.route('/')
def welcome():
    return "Welcome to Nepal Locations API!"

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(load_locations())

@app.route('/locations/<int:location_id>', methods=['GET'])
def get_location_by_id(location_id):
    locations = load_locations()
    location = next((loc for loc in locations if loc["id"] == location_id), None)
    if location:
        return jsonify(location)
    return jsonify({"error": "Location not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
