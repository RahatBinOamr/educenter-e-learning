# chatbot/intents.py

INTENTS = {

    "how_are_you": {
        "patterns": ["how are you", "how are you doing", "what's up"],
        "response": "I'm just a chatbot, but I'm here to help! How can I assist you today?"
    },
    "how_does_this_work": {
        "patterns": ["how does this work", "how to use this", "what can you do"],
        "response": "I'm your virtual assistant! You can ask me about order status, product details, account help, or anything related to the website."
    },
    "tell_joke": {
        "patterns": ["tell me a joke", "make me laugh", "say something funny"],
        "response": "Why don't scientists trust atoms? Because they make up everything!"
    },
    "who_are_you": {
        "patterns": ["who are you", "what are you", "are you a bot"],
        "response": "I'm your personal assistant chatbot, here to help you with questions about this e-commerce site!"
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "thanks a lot"],
        "response": "You're welcome! Feel free to ask me anything else."
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you later"],
        "response": "Goodbye! Have a great day!"
    },
    "order_status": {
        "patterns": ["order status", "track my order", "where is my order"],
        "response": "Please provide your order ID to check the status."
    },
    "product_price": {
        "patterns": [
            "what is the price of this product",
            "how much does this product cost",
            "price of this product",
            "product price",
            "how much is",
            "cost of"
        ],
        "response": "Please specify the product name for pricing information."
    },
    "create_account": {
        "patterns": ["how can i create an account", "how do i sign up", "create account", "register account"],
        "response": "To create an account, go to the sign-up page by clicking the 'Sign Up' button at the top of the page. Fill out the required details, and then click 'Submit' to register."
    },
    "password_reset": {
        "patterns": ["how can i forgot password", "how can i reset my password", "forgot password", "reset password"],
        "response": "To reset your password, click on 'Forgot Password' on the login page and follow the instructions."
    },
    "payment_methods": {
        "patterns": ["payment options", "how can I pay", "payment methods"],
        "response": "We accept various payment methods including credit cards, PayPal, and Stripe."
    },
    "unknown": {
        "response": "Sorry, I couldn't understand your question. Could you rephrase it?"
    }
}
