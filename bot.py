import os
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from openai import OpenAI
import pandas as pd
import time

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = App(token = os.environ["SLACK_TOKEN_USER"])

chatClient = OpenAI(api_key = os.environ['OPENAI_TOKEN'])

@app.event("app_mention")    
def handle_message_events(body, say):
    # Log message
    print(str(body["event"]["text"]).split(">")[1])
    
    # Create prompt for ChatGPT
    prompt = str(body["event"]["text"]).split(">")[1]
    
    say("Getting your message...")

    completion = chatClient.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": "Hello!"}
        ]
    )
    say(completion.choices[0].message.content)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_TOKEN_APP"]).start()