# router_graph.py

from langgraph.graph import StateGraph, END
from langchain_core.runnables import Runnable
from openai import OpenAI

from dotenv import load_dotenv
import os
from handlers import handle_math, handle_code, handle_general


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_input(state):
    user_input = state["input"]

    prompt = f"""
    Classify the following user input into one of these categories:
    - Math
    - Code
    - General Question

    Input: "{user_input}"
    Only return the category name.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
    classification = response.choices[0].message.content.strip()
    state["category"] = classification
    return state

def build_graph():
    builder = StateGraph(dict)  # <-- Correct way to define the state schema

    builder.add_node("classify", classify_input)
    builder.add_node("handle_math", handle_math)
    builder.add_node("handle_code", handle_code)
    builder.add_node("handle_general", handle_general)

    builder.set_entry_point("classify")

    builder.add_conditional_edges(
        "classify",
        lambda state: state["category"],
        {
            "Math": "handle_math",
            "Code": "handle_code",
            "General Question": "handle_general"
        }
    )

    builder.add_edge("handle_math", END)
    builder.add_edge("handle_code", END)
    builder.add_edge("handle_general", END)

    return builder.compile()
