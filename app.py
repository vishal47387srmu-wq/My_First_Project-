from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Ask the user for a topic
topic = input("Enter a topic: ")

# Create the study prompt
prompt = f"""
You are a friendly AI Study Assistant.

The student is learning about: {topic}

Explain the topic at a beginner-friendly college-student level.

Give the answer in this format:

1. Simple Explanation
2. Real-World Example
3. Three Important Points
4. One Quiz Question

Keep the explanation clear, simple, and easy to understand.
"""

# Send the request to OpenAI
response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

# Display the AI response
print("\n===== AI STUDY ASSISTANT =====\n")
print(response.output_text)
