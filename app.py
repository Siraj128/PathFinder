# app.py
import streamlit as st
from engine import generate_learning_path # Import our Gemini-powered brain

# --- UI Configuration ---
st.set_page_config(page_title="Pathfinder", page_icon="🧭", layout="centered")

# --- Header ---
st.title("🧭 Pathfinder")
st.subheader("Your Personal AI Learning Guide, powered by Gemini")

# --- User Inputs ---
topic = st.text_input("What topic do you want to master?", placeholder="e.g., Python, Guitar, Marketing")

level_options = ["Beginner", "Intermediate", "Advanced"]
level = st.selectbox("What is your current skill level?", level_options)

# --- Generate Button and Logic (will be fully implemented in the next phase) ---
# In app.py, replace the final if-statement block with this:

if st.button("Craft My Learning Path", type="primary"):
    if not topic:
        st.warning("Please enter a topic to learn.")
    else:
        # Use a spinner to show the app is working
        with st.spinner("🧭 Pathfinder is charting your course... This may take a moment."):
            try:
                # Call the engine to get the learning path
                learning_path = generate_learning_path(topic, level)

                # Check if the path was generated successfully
                if learning_path:
                    st.balloons() # A fun little celebration!
                    st.success("Your personalized learning path is ready!")
                    
                    # Display each step in a collapsible expander
                    for i, step in enumerate(learning_path):
                        with st.expander(f"**Step {i+1}: {step.get('step_title', 'Untitled Step')}**", expanded=(i==0)):
                            st.markdown(f"**Explanation:**\n{step.get('explanation', 'No explanation provided.')}")
                            
                            st.markdown(f"**📚 Resources to Find:**")
                            # It's good practice to check if the key exists
                            resources = step.get('resources_to_find', [])
                            for resource in resources:
                                st.markdown(f"- `{resource}`")
                            
                            st.markdown(f"**🛠️ Project Idea:**\n{step.get('project_idea', 'No project idea provided.')}")
                else:
                    st.error("Sorry, I couldn't generate a learning path. The AI might be busy, or the topic too niche. Please try again.")

            except Exception as e:
                st.error(f"A critical error occurred: {e}")