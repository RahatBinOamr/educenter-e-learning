# chatbot/nlp_utils.py

from chatbot.intents import INTENTS
from .models import Intent

def match_intent(user_input):
    user_input = user_input.lower()

    # Check if the user input matches any intent in the database using i_contains
    intents = Intent.objects.filter(question__icontains=user_input)

    if intents.exists():
        # If a match is found, return the corresponding answer
        return intents.first().answer
    
    # If no match found, return a default response
    return "Sorry, I couldn't understand your question. Could you rephrase it?"


def match_intent(user_input):
    user_input = user_input.lower()
    
    for intent, data in INTENTS.items():
        for pattern in data['patterns']:
            if pattern in user_input:
                return INTENTS[intent]['response']
    
    # If no match found, return a default response
    return INTENTS['unknown']['response']
