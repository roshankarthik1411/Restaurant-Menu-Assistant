import os
import json
import google.generativeai as genai
from utils.config import SYSTEM_PROMPT

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a quota-safe model
model = genai.GenerativeModel("models/gemini-flash-latest")


def ask_assistant(user_query: str):
    try:
        full_prompt = SYSTEM_PROMPT.replace("{user_query}", user_query)

        response = model.generate_content(full_prompt)

        if not response or not response.text:
            return "I'm here to help with restaurant recommendations! Are you looking for a place to dine?"

        text = response.text.strip()

        # Try JSON parsing (restaurant query)
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            # Off-topic conversational response
            return text

    except Exception:
        return "Sorry, I'm having trouble right now. Please try again later."
