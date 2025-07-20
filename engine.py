# engine.py - Powered by Google Gemini
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

def generate_learning_path(topic, level):
    """
    Generates a learning path using the Google Gemini API.
    """
    
    # Load the API key from the .env file
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Google API Key not found. Please set it in the .env file.")
    
    # Configure the Gemini API client
    genai.configure(api_key=api_key)

    # The great news is that our master prompt is universal and doesn't need to change!
    prompt = f"""
    You are an expert curriculum designer AI named "Pathfinder". 
    Your task is to create a personalized, step-by-step learning path for a user.

    The user wants to learn about: "{topic}"
    Their current knowledge level is: "{level}"

    Generate a 7-step curriculum. For a beginner, start with the absolute basics. For an intermediate user, assume they know the fundamentals.

    For each step, you MUST provide the following four fields:
    1. "step_title": A clear, concise title for the concept (e.g., "The Foundation: Your Starter").
    2. "explanation": A one-paragraph explanation of the concept, tailored to the user's level.
    3. "resources_to_find": 2-3 specific phrases or keywords the user can search for on Google or YouTube to find tutorials, articles, or videos.
    4. "project_idea": A small, practical project to test their understanding of this specific step.

    Your final output MUST be a single, valid JSON object. This object should contain a single key "learning_path" which is a list of the 7 steps. Do not include any text or explanations outside of the JSON object.
    """

    # Set up the model with instructions for JSON output
    generation_config = genai.GenerationConfig(
        response_mime_type="application/json",
    )
    model = genai.GenerativeModel(
        "gemini-1.5-flash-latest", # A fast and capable model
        generation_config=generation_config
    )

    try:
        # Call the API to generate the content
        response = model.generate_content(prompt)
        
        # Parse the JSON string from the response into a Python dictionary
        learning_path_data = json.loads(response.text)
        
        return learning_path_data.get("learning_path", [])

    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the API response.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# This part is for testing our function directly from the terminal
if __name__ == '__main__':
    test_topic = "The History of Ancient Rome"
    test_level = "Beginner"
    print(f"Generating a path for a {test_level} learning {test_topic}...")
    path = generate_learning_path(test_topic, test_level)
    
    if path:
        # Pretty-print the JSON output
        print(json.dumps(path, indent=2))