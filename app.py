from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- EXPANDED RULE-BASED RESPONSE DICTIONARY (50+ Examples) ---
FIRST_AID_RESPONSES = {
    # 1-10: Injuries & Trauma
    'burn': "For minor burns, immediately run cool water over the area for 10-20 minutes. Do not use ice or butter. Cover the burn loosely with a sterile bandage.",
    'cut': "For minor cuts, wash hands, clean the wound with soap and water, and apply a sterile bandage. Apply direct pressure for heavy bleeding.",
    'bleeding': "Apply firm, direct pressure to the wound with a clean cloth or bandage. Elevate the injured area if possible. If bleeding soaks through, do not remove the cloth; add more over it.",
    'choking': "Perform the Heimlich maneuver: 5 back blows followed by 5 abdominal thrusts. Call emergency services if the victim loses consciousness.",
    'cpr': "Call emergency services first. Begin chest compressions: 100-120 compressions per minute on the center of the chest. Follow any dispatcher instructions.",
    'fracture': "Do not move the person unless in danger. Stabilize the injured area, and call emergency services immediately. Keep the injured area as still as possible.",
    'broken bone': "Treat it like a fracture: immobilize the limb, apply a cold pack (not directly to skin), and seek professional medical help immediately.",
    'sprain': "Use the R.I.C.E method: Rest, Ice (20 mins on, 20 mins off), Compression (with a bandage), and Elevation. Seek medical attention if swelling is severe.",
    'strain': "Rest the strained muscle, apply ice, and use mild compression. Gentle stretching may help after the initial pain subsides, but avoid heavy activity.",
    'dislocation': "Do NOT try to push the joint back into place. Immobilize the limb with a splint or sling and seek emergency medical care immediately.",

    # 11-20: Environmental & Bites
    'heat exhaustion': "Move the person to a cool place. Have them lie down and loosen clothing. Give sips of cool water or a sports drink. If symptoms worsen, call emergency services.",
    'heatstroke': "This is an emergency. Call emergency services immediately. Cool the person rapidly using cold wet cloths or an ice bath.",
    'hypothermia': "Move the person to a warm, dry place. Remove wet clothing. Warm the center of the body first (chest, neck, head, groin) with blankets. Do NOT rub the victim.",
    'frostbite': "Move to a warm place. Slowly warm the affected area with body heat or warm water (not hot). Do not rub the skin or use a heating pad.",
    'bee sting': "Remove the stinger by scraping it off (do not pinch). Wash the area and apply ice. Monitor for signs of severe allergic reaction.",
    'snake bite': "Call emergency services immediately. Keep the person calm and still. Keep the bitten area below the heart level. Do NOT try to suck out the venom or apply a tourniquet.",
    'spider bite': "Clean the area with soap and water and apply a cold compress. If you suspect a venomous spider or the bite looks infected, seek medical attention.",
    'splinter': "Sterilize tweezers with rubbing alcohol. Gently pull the splinter out in the direction it entered. Clean the area and apply a bandage.",
    'nosebleed': "Lean slightly forward (not back). Pinch the soft part of the nose just above the nostrils for 10-15 minutes. Apply an ice pack to the nose or cheeks.",
    'concussion': "Seek medical evaluation. Watch for loss of consciousness, confusion, vomiting, or severe headache. Do not leave the person alone; wake them every two hours to check responsiveness.",

    # 21-30: Illness & Allergic Reactions
    'fever': "Rest, drink fluids, and use over-the-counter medication (acetaminophen/ibuprofen) as directed. Consult a doctor if the fever is very high or lasts longer than two days.",
    'temperature': "If the temperature is high, treat as a fever: stay hydrated and use OTC medication. Seek medical advice if it exceeds 103°F (39.4°C).",
    'allergic reaction': "For mild reactions, take an antihistamine and avoid the allergen. For severe reactions (anaphylaxis: difficulty breathing, swelling), use an EpiPen if available and call emergency services immediately.",
    'asthma attack': "Use the prescribed rescue inhaler immediately. If breathing does not improve within a few minutes or worsens, call emergency services.",
    'diarrhea': "Drink plenty of clear fluids (water, broth) to prevent dehydration. Avoid dairy and greasy foods. Seek medical advice if symptoms persist or fever is present.",
    'vomiting': "Rest and avoid solid foods for a few hours. Sip small amounts of clear, non-caffeinated liquids (like water or broth) to stay hydrated.",
    'seizure': "Protect the person from injury by moving objects away. Do not restrain them or put anything in their mouth. Time the seizure. Call emergency services if the seizure lasts longer than 5 minutes.",
    'stroke': "Think FAST: Face drooping, Arm weakness, Speech difficulty, Time to call 911/emergency services. Time is critical; call immediately.",
    'headache': "Rest in a dark, quiet room. Apply a cold pack to the forehead or neck. Use over-the-counter pain relievers.",
    'dizziness': "Sit or lie down immediately to prevent falling. Slowly sip water. If dizziness is severe or accompanied by other symptoms (like chest pain), seek medical help.",

    # 31-40: Foreign Objects & Minor Issues
    'cough': "Avoid touching your eyes, nose, or mouth, all of which are easy entry points for bacteria and viruses into your body where they may cause infection.",
    'eye injury': "Do not rub the eye. If a small particle is present, flush the eye with clean water. For chemical exposure or a large object, cover the eye loosely and seek emergency care.",
    'foreign object': "If an object is embedded in the skin, do not remove it; stabilize it and seek medical help. If swallowed, call for advice immediately.",
    'splashing chemical': "Immediately flush the affected skin or eye with large amounts of cool water for at least 15-20 minutes. Call poison control or emergency services.",
    'nausea': "Rest in a cool, quiet place. Try sipping clear fluids. Avoid strong odors and heavy foods. Ginger products may help.",
    'stomach pain': "Rest and use a heating pad. Sip water. Avoid solid food for a few hours. Call a doctor if the pain is severe or accompanied by fever/bloody stool.",
    'blister': "If intact, do not pop it; cover with a loose bandage. If broken, clean the area gently with soap and water and apply an antibiotic ointment.",
    'sunburn': "Apply cool compresses or take a cool shower. Use an aloe vera lotion or moisturizing cream. Drink extra water. Avoid further sun exposure.",
    'minor abrasion': "Clean the area gently with mild soap and water. Apply a thin layer of antibiotic ointment and cover with a sterile, non-stick bandage.",
    'bruise': "Apply a cold compress or ice pack to the area for 15-20 minutes. If the bruise is large or very painful, consult a healthcare provider.",
    'unresponsive': "Check if the person is breathing. If not breathing, begin CPR and call emergency services immediately. Do not move them unless they are in danger.",

    # 41-50: Miscellaneous & Critical
    'chest pain': "This is a potential emergency. Call emergency services immediately. Have the person sit down and loosen tight clothing. If they take nitroglycerin, assist them.",
    'diabetic emergency': "If the person is conscious and able to swallow, give them a sweet drink or food (like juice, candy, or glucose tablets). If they lose consciousness, call emergency services.",
    'drowning': "Call emergency services immediately. Carefully remove the person from the water. Begin rescue breathing and/or CPR if they are not breathing.",
    'electric shock': "Do not touch the person if they are still connected to the power source! Turn off the electricity immediately. Once safe, check for breathing and call emergency services.",
    'severe bleeding': "Call emergency services. Apply continuous, direct, firm pressure to the wound. If possible, elevate the injury above the heart.",
    'poisoning': "Call your regional poison control center immediately. Follow their instructions. Do NOT induce vomiting unless specifically instructed to do so.",
    'unconsciousness': "Check for breathing and injuries. If breathing, place the person in the recovery position and call emergency services. If not breathing, begin CPR.",
    'animal bite': "Wash the wound thoroughly with soap and water. Apply clean dressings and seek medical attention for risk of infection or rabies.",
    'foreign body ear': "Do not use tweezers or cotton swabs. Tilt the head and shake gently. If an insect, pour mineral oil into the ear. Seek medical help if the object remains.",
    'chemical eye exposure': "Flush the eye immediately and continuously with running water for 15 minutes. Call emergency services while flushing.",
    'emergency': "For a medical emergency, please call your local emergency number immediately. I can only provide general first-aid guidance."
}

# --- AI Logic Function (Uses the Dictionary) ---
def get_ai_response(query):
    lower_query = query.lower()
    
    # Check for keywords in the dictionary
    for key, response in FIRST_AID_RESPONSES.items():
        if key in lower_query:
            return response

    # Default response for unrecognized queries
    return "I'm sorry, I can only provide basic first-aid advice. Please type a specific condition like 'burn', 'cut', 'choking', 'fever', or 'sprain'."


# --- Flask Routes ---
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
    # Use Flask's built-in server for local development
    app.run(debug=True)