# handlers.py

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_math(state):
    user_input = state["input"]
    prompt = f"Solve this math problem step-by-step:\n{user_input}"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    state["output"] = response.choices[0].message.content.strip()
    return state

def handle_code(state):
    user_input = state["input"]
    prompt = f"Write clean, well-commented Python code for the following task:\n{user_input}"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    state["output"] = response.choices[0].message.content.strip()
    return state

def handle_general(state):
    user_input = state["input"]
    prompt = f"Answer this question clearly and concisely:\n{user_input}"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    state["output"] = response.choices[0].message.content.strip()
    return state
