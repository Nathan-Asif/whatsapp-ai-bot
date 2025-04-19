import os
import requests
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def ask_openai(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-0125",
#         messages=[
#             {"role": "system", "content": "You are an order assistant for WhatsApp."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response['choices'][0]['message']['content']


def geminiModel(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + os.getenv("GEMINI_API_KEY")
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{
            "parts":[{"text": prompt}]
        }]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()