import streamlit as st
import requests
import random

# API Configuration
BASE_URL = "https://danadavis.dev/thegreekmythapi/gods"

def get_god_details(god_name):
    response = requests.get(f"{BASE_URL}/{god_name.lower()}")
    if response.status_code == 200:
        return response.json()
    return None

# Initialize session state variables
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# Streamlit UI
st.title("Number Guessing Game")
st.write("Guess the number between 1 and 100!")

# User Input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
        st.balloons()
        # Reset the game
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0

# Streamlit UI
st.title("Greek Mythology Chatbot")
st.write("Ask about a Greek god and get detailed information!")

# User Input
god_name = st.text_input("Enter a Greek god's name", "Zeus")

if st.button("Ask"):  
    if god_name:
        data = get_god_details(god_name)
        if data:
            st.subheader(f"About {data['name']}")
            st.write(f"**Title:** {data.get('title', 'Unknown')}")
            st.write(f"**Parents:** {', '.join(data.get('parents', ['Unknown']))}")
            st.write(f"**Siblings:** {', '.join(data.get('siblings', ['Unknown']))}")
            st.write(f"**Children:** {', '.join(data.get('children', ['Unknown']))}")
            st.write(f"**Description:** {data.get('description', 'No description available.')}")
        else:
            st.error("God not found. Please enter a valid Greek god's name.")
    else:
        st.warning("Please enter a name.")
print("Hello World")