# app.py

from flask import Flask, render_template, request, jsonify
import json
import os # <-- Must be imported!

app = Flask(__name__)

# --- Load the Intents Data (The Fix is HERE) ---
def load_intents():
    # Use os.path.dirname(__file__) to get the absolute path of the directory
    # where app.py is located, which is necessary for Render/Linux systems.
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Get the correct base path
    intents_file = os.path.join(BASE_DIR, 'intents.json') 
    
    if not os.path.exists(intents_file):
        # This will fail the deployment but show a clear error in the logs
        raise FileNotFoundError(f"Intents file not found at: {intents_file}")
    
    with open(intents_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['intents']

# Load data once when the app starts
INTENTS_DATA = load_intents()

# ... (The rest of your app.py code is fine)
# ...