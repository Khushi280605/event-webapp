from flask import Flask, render_template, redirect, request, url_for
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    with open('events.json') as f:
        events = json.load(f)
    return render_template('index.html', events=events)

@app.route('/get-tickets/<path:url>', methods=['POST'])
def get_tickets(url):
    email = request.form.get('email')
    # You could log or process the email here
    return redirect(url)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
