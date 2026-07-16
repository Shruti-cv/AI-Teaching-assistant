import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
print("API Key Loaded:", GOOGLE_API_KEY[:10] + "...")
print("API Key Length:", len(GOOGLE_API_KEY))

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")



def generate_answer(query, analysis):

    prompt = f"""
You are an AI Teaching Assistant.

Student Question:
{query}

Intent:
{analysis['intent']}

Topic:
{analysis['topic']}

Difficulty:
{analysis['difficulty_level']}

Explain the answer in a simple way.

Also include:
1. Explanation
2. One Example
3. Three Key Points
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        return f"""
## 📘 Explanation

**Topic:** {analysis['topic']}

Your question is related to **{analysis['topic']}**.

This project is currently running in **offline mode** because the Gemini API is temporarily unavailable.

### Example

Here is a simple example related to **{analysis['topic']}**:

- Study the basic concepts.
- Practice with real examples.
- Solve a few exercises.

### Key Points

- Understand the fundamentals.
- Practice consistently.
- Revise regularly.
"""