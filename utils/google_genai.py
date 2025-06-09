# utils/google_genai.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API with the key from .env
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")
genai.configure(api_key=api_key)

# Initialize the Gemini model (e.g., gemini-1.5-flash or gemini-pro)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_response(prompt):
    """
    Generate a response using Google Gemini API.
    
    Args:
        prompt (str): The input text to generate a response for.
    
    Returns:
        str: The generated response, or None if an error occurs.
    """
    try:
        # Use generate_content instead of generate_text
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
        return None