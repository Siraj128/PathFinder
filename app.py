# app.py - Now with Password Protection
import streamlit as st
from engine import generate_learning_path
import requests
from streamlit_lottie import st_lottie

def check_password():
    """Returns `True` if the user has entered the correct password."""
    
    # Check if the password is correct
    def password_entered():
        if st.session_state["password"] == st.secrets["APP_PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store password
        else:
            st.session_state["password_correct"] = False

    # Initialize session state if not already done
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    # Show password input
    if not st.session_state["password_correct"]:
        st.text_input(
            "Enter Password", type="password", on_change=password_entered, key="password"
        )
        if st.session_state.get("password_correct") == False:
            st.error("😕 Password incorrect. Please try again.")
        return False
    else:
        return True
        
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main_app():
    """This function runs the main part of the Streamlit app."""
    # --- UI Configuration ---
    st.set_page_config(page_title="Pathfinder", page_icon="🧭", layout="centered")

    # --- Header ---
    st.title("🧭 Pathfinder")
    st.subheader("Your Personal AI Learning Guide, powered by Gemini")

    # --- User Inputs ---
    topic = st.text_input("What topic do you want to master?", placeholder="e.g., Python, Guitar, Marketing")
    level_options = ["Beginner", "Intermediate", "Advanced"]
    level = st.selectbox("What is your current skill level?", level_options)

    # --- Generate Button and Logic ---
    if st.button("Craft My Learning Path", type="primary"):
        if not topic:
            st.warning("Please enter a topic to learn.")
        else:
            with st.spinner("🧭 Pathfinder is charting your course..."):
                try:
                    learning_path = generate_learning_path(topic, level)
                    if learning_path:
                        https://lottie.host/09c9b9a6-d5d8-4809-9b57-7973784b2671/Vp0yBngHwt.json
                        lottie_success = load_lottieurl(lottie_success_url)
    
                        # Display the animation
                        if lottie_success:
                            st_lottie(lottie_success, speed=1, height=200, key="success_animation")

                        # st.toast('Your path has been crafted!', icon='🧭')
                        st.success("Your personalized learning path is ready!")
                        for i, step in enumerate(learning_path):
                            with st.expander(f"**Step {i+1}: {step.get('step_title', 'Untitled Step')}**", expanded=(i==0)):
                                st.markdown(f"**Explanation:**\n{step.get('explanation', 'No explanation provided.')}")
                                st.markdown(f"**📚 Resources to Find:**")
                                resources = step.get('resources_to_find', [])
                                for resource in resources:
                                    st.markdown(f"- `{resource}`")
                                st.markdown(f"**🛠️ Project Idea:**\n{step.get('project_idea', 'No project idea provided.')}")
                    else:
                        st.error("Sorry, I couldn't generate a learning path. Please try again.")
                except Exception as e:
                    st.error(f"A critical error occurred: {e}")

# --- Main App Execution ---
if check_password():
    main_app()
