# app.py (Crucial lines for file loading)

from flask import Flask, render_template, request, jsonify
import json
import os # <-- Must be included!

# ...

# --- Load the Intents Data ---
def load_intents():
    # Use os.path.dirname(__file__) to get the absolute path
    intents_file = os.path.join(os.path.dirname(__file__), 'intents.json') 
    
    if not os.path.exists(intents_file):
        # This will throw an error if the file isn't found
        raise FileNotFoundError(f"Intents file not found at: {intents_file}")
    
    with open(intents_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['intents']

# Load data once when the app starts
INTENTS_DATA = load_intents() 
# ... (rest of the code follows)