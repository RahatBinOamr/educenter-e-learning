# chatbot/views.py

from django.http import JsonResponse
from django.shortcuts import render
from .nlp_utils import match_intent

def chatbot_response(request):
    user_input = request.GET.get('message', '')
    if not user_input:  # Handle the case when there's no user input (i.e., initial page load)
        return JsonResponse({'response': "Welcome! How can I assist you today?"})
    
    response = match_intent(user_input)
    return JsonResponse({'response': response})

def chatbot_page(request):
    return render(request, 'chatbot.html')