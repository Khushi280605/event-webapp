from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/events', methods=['GET'])
def get_events():
    with open('events.json', 'r') as f:
        events = json.load(f)
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
