# chatbot/management/commands/populate_intents.py

from django.core.management.base import BaseCommand
from chatbot.models import Intent

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        intents = [
            {"question": "how are you", "answer": "I'm just a chatbot, but I'm here to help! How can I assist you today?"},
            {"question": "how does this work", "answer": "I'm your virtual assistant! You can ask me about order status, product details, or account help."},
            {"question": "tell me a joke", "answer": "Why don't scientists trust atoms? Because they make up everything!"},
            {"question": "who are you", "answer": "I'm your personal assistant chatbot, here to help you with questions about this site."},
            {"question": "thank you", "answer": "You're welcome! Feel free to ask me anything else."},
            {"question": "bye", "answer": "Goodbye! Have a great day!"},
            {"question": "order status", "answer": "Please provide your order ID to check the status."},
            {"question": "product price", "answer": "Please specify the product name for pricing information."},
            {"question": "create account", "answer": "To create an account, click on 'Sign Up' at the top of the page and fill in your details."},
            {"question": "forgot password", "answer": "To reset your password, click on 'Forgot Password' on the login page and follow the instructions."},
            {"question": "payment methods", "answer": "We accept various payment methods including credit cards, PayPal, and Stripe."},
            {"question": "shipping information", "answer": "Shipping times vary based on your location and selected shipping method. You can view estimated delivery times at checkout."},
            {"question": "return policy", "answer": "You can return items within 30 days of purchase. Please check our return policy page for detailed instructions."},
            {"question": "discount code", "answer": "You can enter discount codes at checkout to receive discounts on your order."},
            {"question": "cancel my order", "answer": "To cancel your order, please contact our support team within 24 hours of placing the order."},
            {"question": "is this product available", "answer": "Please provide the product name to check its availability."},
            {"question": "How can I forgot password", "answer": "To reset your password, click on 'Forgot Password' on the login page and follow the instructions."},
            {"question": "How can I reset my password?", "answer": "To reset your password, click on 'Forgot Password' on the login page and follow the instructions."},
            {"question": "mechanical keyboard?", "answer": "Keychron Q5 Max [Q1 Max, Q2 Max, etc.]."},
        ]
        
        for intent in intents:
            Intent.objects.create(question=intent["question"], answer=intent["answer"])

        self.stdout.write(self.style.SUCCESS('Successfully populated intents'))
