from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# This is the updated function with more conditions
def get_ai_response(query):
    lower_query = query.lower()

    if 'burn' in lower_query:
        return "For minor burns, immediately run cool water over the area for 10-20 minutes. Do not use ice or butter. Cover the burn loosely with a sterile bandage."
    elif 'cut' in lower_query or 'bleeding' in lower_query:
        return "For minor cuts, first wash your hands. Clean the wound with soap and water. Apply a sterile bandage. If bleeding is heavy, apply direct pressure with a clean cloth."
    elif 'choking' in lower_query:
        return "If someone is choking, perform the Heimlich maneuver. Stand behind the person, wrap your arms around their waist, and make a fist with one hand. Place the thumb side of your fist just above the navel and perform five quick upward thrusts."
    elif 'cpr' in lower_query:
        return "For CPR, call emergency services first. Then, place the heel of your hand on the center of the person's chest. With your other hand on top, press down hard and fast, about 100-120 compressions per minute."
    elif 'fracture' in lower_query or 'broken bone' in lower_query:
        return "If you suspect a broken bone, do not move the person unless they are in immediate danger. Call emergency services. Keep the injured area as still as possible."
    elif 'fever' in lower_query or 'temperature' in lower_query:
        return "For a fever, rest and drink plenty of fluids. Over-the-counter medication like acetaminophen or ibuprofen can help. If the fever is very high or persistent, consult a doctor."
    elif 'sprain' in lower_query:
        return "For a sprain, use the R.I.C.E method: Rest the injured joint, Ice the area, apply Compression with a bandage, and Elevate the limb. If the pain is severe or you can't bear weight, see a doctor."
    elif 'allergic reaction' in lower_query or 'allergy' in lower_query:
        return "For a mild allergic reaction, identify and remove the allergen. An over-the-counter antihistamine may help. For a severe reaction (anaphylaxis) with difficulty breathing or swelling, use an epinephrine auto-injector if available and call for emergency medical help immediately."
    elif 'emergency' in lower_query:
        return "For a medical emergency, please call your local emergency number immediately. I can only provide general first-aid guidance."
    else:
        return "I'm sorry, I can only provide basic first-aid advice. Please type a specific condition like 'burn', 'cut', 'choking', 'fever', or 'sprain'."

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat_page():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    ai_response = get_ai_response(user_message)
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)