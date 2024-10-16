import requests

API_KEY = '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' 
API_URL = 'https://api.groq.com/openai/v1/chat/completions'

def get_groq_response(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "prompt": prompt,
        "max_tokens": 150
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    elif response.status_code == 404:
        return "Error: The requested resource could not be found."
    else:
        return f"Error: {response.status_code}, {response.text}"
