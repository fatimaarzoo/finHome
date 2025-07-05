from django.shortcuts import render
import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_response(user_input):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

def chatbot(request):
    response = None
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        if user_input:
            response = get_response(user_input)
    return render(request, "chatbot/chatbot.html", {"response": response})