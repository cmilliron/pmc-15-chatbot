import openai
from dotenv import load_dotenv
import os

load_dotenv()

class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPEN_AI_KEY")

    def get_response(self, user_input):
        messages = [
            {"role": "system", "content": "You are a general chatbot."},
            {"role": "user", "content": user_input},
        ]
        response = openai.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=messages).choices[0].message.content
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds")
    print(response)
