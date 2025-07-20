Use this for your project's main README.md file. It's comprehensive and welcoming to other developers.
🧭 Pathfinder: Your Personal AI Learning Guide
Ever wanted to learn a new skill but felt overwhelmed by where to start? Pathfinder is an intelligent web application designed to cut through the noise of information overload. It leverages the power of Google's Gemini AI to generate structured, personalized learning curricula for any topic imaginable.
Whether you want to learn Python, master sourdough baking, or understand the basics of quantum mechanics, Pathfinder provides a clear and actionable roadmap to guide your journey.
Key Features
🗺️ Personalized Curricula: Generates unique learning paths based on the user's topic and chosen skill level (Beginner, Intermediate, Advanced).
📝 Step-by-Step Structure: Breaks down complex subjects into 7 manageable steps, each with a clear title and a concise explanation.
📚 Curated Resource Suggestions: For each step, it suggests key terms and phrases to search for on Google or YouTube, pointing you toward high-quality learning materials.
🛠️ Practical Projects: Reinforces learning with a small, practical project idea for each step, ensuring you can apply what you've learned.
How It Works
Pathfinder uses a simple but powerful pipeline:
The user enters a topic and skill level into the Streamlit frontend.
A detailed, instruction-rich prompt is sent to the Google Gemini API.
The AI model processes the request and generates a structured curriculum in JSON format.
The Streamlit application parses the JSON and displays the learning path in a clean, interactive, and easy-to-read format.
Tech Stack
Language: Python
AI Model: Google Gemini API (gemini-1.5-flash)
Web Framework: Streamlit
API Key Management: python-dotenv
