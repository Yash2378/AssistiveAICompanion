# utils/openai_utils.py
import openai
import os

# Get OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Please set the 'OPENAI_API_KEY' environment variable.")

openai.api_key = OPENAI_API_KEY

def get_openai_response(query, conversation_history):
    print("Thinking...")
    try:
        conversation_history.append({"role": "user", "content": query})
        limited_history = conversation_history[-100:]  # Only keep recent history
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=limited_history
        )
        
        response_text = response.choices[0].message["content"].strip()
        conversation_history.append({"role": "assistant", "content": response_text})
        return response_text
    except Exception as e:
        print(f"Error in OpenAI Chat API call: {e}")
        return "I'm having trouble accessing my knowledge base right now."
