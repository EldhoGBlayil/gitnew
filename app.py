import streamlit as st
import json

# Load local JSON file
def load_local_data():
    try:
        with open("greek_mythology_data.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        st.error("Error: Failed to load JSON data. Please check the file format.")
        return []
    except FileNotFoundError:
        st.error("Error: JSON file not found. Please ensure 'greek_mythology_data.json' exists.")
        return []

# Streamlit UI
st.title("Greek Mythology Encyclopedia")
st.sidebar.header("Search for a Character")

# Load local JSON data
data = load_local_data()
names = [character["name"] for character in data] if data else []

# User input
if names:
    selected_name = st.sidebar.selectbox("Choose a character", names)
else:
    st.sidebar.warning("No characters available.")
    selected_name = None

def display_character_details(character):
    st.subheader(character["name"])
    st.write(f"**Type:** {character.get('type', 'Unknown')}")
    st.write(f"**Parents:** {', '.join(character.get('parents', ['Unknown']))}")
    st.write(f"**Strengths:** {', '.join(character.get('strengths', ['N/A']))}")
    st.write(f"**Stories:** {character.get('stories', 'No information available')}")
    if "image" in character and character["image"]:
        st.image(character["image"], caption=character["name"], width=300)
    else:
        st.warning("No image available.")

# Display data
if selected_name:
    character_data = next((char for char in data if char["name"] == selected_name), None)
    if character_data:
        display_character_details(character_data)
    else:
        st.error("Character not found in local data.")
