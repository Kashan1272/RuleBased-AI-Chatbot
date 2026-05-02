import re
from datetime import datetime

# Define intents with keywords
INTENTS = {
    "greeting": ["hi", "hello", "hey", "salam"],
    "goodbye": ["bye", "exit", "quit", "goodbye"],
    "name": ["your name", "who are you"],
    "help": ["help", "what can you do"],
    "time": ["time", "current time"],
    "date": ["date", "today"],
    "weather": ["weather", "temperature"],
    "thanks": ["thanks", "thank you"]
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    return text

from rapidfuzz import fuzz  # ADD THIS AT TOP

def detect_intent(user_input):
    user_input = clean_text(user_input)

    best_intent = "unknown"
    best_score = 0

    for intent, keywords in INTENTS.items():
        for word in keywords:
            score = fuzz.partial_ratio(user_input, word)

            if score > best_score and score > 70:
                best_score = score
                best_intent = intent

    return best_intent

def get_response(user_input):
    intent = detect_intent(user_input)

    if intent == "greeting":
        return "Hello! 👋 How can I assist you today?"

    elif intent == "goodbye":
        return "Goodbye! 👋 Have a great day."

    elif intent == "name":
        return "I am a Rule-Based AI Chatbot."

    elif intent == "help":
        return "I can respond to greetings, tell time/date, and answer simple questions."

    elif intent == "time":
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"

    elif intent == "date":
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"

    elif intent == "weather":
        return "I can't fetch live weather yet, but it's a great day to code!"

    elif intent == "thanks":
        return "You're welcome! 😊"

    else:
        return "I didn't fully understand that. Can you rephrase?"