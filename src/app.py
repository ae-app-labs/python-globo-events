from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_KEY = os.getenv('API_KEY')
# Setting up some mock response so that we don't hit the API always
MOCK_RESPONSE = os.getenv('MOCK_RESPONSE')

@app.route('/')
def index():
    return render_template('index.html')

# Get all events for a city
@app.route('/events', methods = ['GET'])
def get_events():
    city = request.args.get('city')

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}&city={city}"

    if MOCK_RESPONSE:
        response_file = "responses/toronto.json"
        with open(response_file, 'r') as file:
            file_contents = file.read()
        return file_contents, 200, {'Content-Type': 'text/json'}

    response = requests.get(url)

    if response.status_code == 200:
        events_data = response.json()
        return jsonify(events_data)
    else:
        return jsonify({"error" : "Failed to retrieve events"}), 500

# Get images for an event
@app.route('/events/<event_id>/images', methods=['GET'])
def get_event_images(event_id):
    url = f"https://app.ticketmaster.com/discovery/v2/events/{event_id}/images.json?apikey={API_KEY}"

    if MOCK_RESPONSE:
        response_file = "responses/event_images.json"
        with open(response_file, 'r') as file:
            file_contents = file.read()
        return file_contents, 200, {'Content-Type': 'text/json'}

    response = requests.get(url)
    print(response._content)

    if response.status_code == 200:
        images_data = response.json()
        return jsonify(images_data)
    else:
        return jsonify({"error" : "Failed to retrieve images"}), 500

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)