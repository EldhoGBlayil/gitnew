import streamlit as st
import requests

# API Configuration
BASE_URL = "https://anfi.tk/greekApi/person/en"

# Manually added descriptions for major gods (if API lacks them)
GOD_DESCRIPTIONS = {
    "Zeus": "Zeus is the god of the sky and thunder in Greek mythology.",
    "Poseidon": "Poseidon is the god of the sea, earthquakes, and horses.",
    "Hades": "Hades is the ruler of the underworld and the god of the dead.",
    "Apollo": "Apollo is the god of the sun, music, healing, and prophecy.",
    "Athena": "Athena is the goddess of wisdom, war, and crafts.",
    "Ares": "Ares is the god of war, known for his aggressive and violent nature.",
    "Aphrodite": "Aphrodite is the goddess of love, beauty, and desire."
}

def get_god_details(god_name):
    """Fetch details of a Greek god from GreekAPI by newsh."""
    try:
        response = requests.get(f"{BASE_URL}/{god_name}")

        if response.status_code == 404:
            return None  # God not found
        
        response.raise_for_status()  # Raises error for 4xx and 5xx responses

        data = response.json()
        
        return data  # Return JSON data

    except requests.exceptions.RequestException as e:
        st.error(f"❌ API request failed: {e}")
        return None

# ============ Greek Mythology Chatbot ============ #
st.title("🔱 Greek Mythology Chatbot")
st.write("Ask about a Greek god and get detailed information!")

# User Input for Greek God Name
god_name = st.text_input("Enter a Greek god's name", "Zeus")

if st.button("Ask"):
    if god_name.strip():  # Ensure input is not empty
        data = get_god_details(god_name)
        
        if data and data.get("status") == "OK":
            # Extract correct fields safely
            god_name = data.get("name", "Unknown")

            # Parents (Check if mother/father exists before accessing)
            mother = data.get("mother", {}).get("name", None)
            father = data.get("father", {}).get("name", None)
            parents = [p for p in [mother, father] if p]  # Remove None values

            # Extract siblings
            brothers = [b["name"] for b in data.get("brother", [])]  # Extract brother names
            sisters = [s["name"] for s in data.get("sister", [])]  # Extract sister names
            siblings = brothers + sisters  # Combine both
            
            # Extract children
            sons = [s["name"] for s in data.get("son", [])]  # Extract sons' names
            daughters = [d["name"] for d in data.get("daughter", [])]  # Extract daughters' names
            children = sons + daughters  # Combine both

            # Extract spouse/wife (if available)
            spouses = [w["name"] for w in data.get("wife", [])] if "wife" in data else []

            # *Check if the API provides a description, otherwise use our predefined list*
            description = data.get("description", GOD_DESCRIPTIONS.get(god_name, "No description available."))

            # Display information
            st.subheader(f"📖 About {god_name}")
            st.write(f"👨‍👩‍👧‍👦 Parents:** {', '.join(parents) if parents else 'Unknown'}")
            st.write(f"👥 Siblings:** {', '.join(siblings) if siblings else 'Unknown'}")
            st.write(f"💍 Spouses:** {', '.join(spouses) if spouses else 'None'}")
            st.write(f"👶 Children:** {', '.join(children) if children else 'Unknown'}")
            st.write(f"📜 Description:** {description}")
        else:
            st.error("⚠ God not found. Please enter a valid Greek god's name.")
    else:
        st.warning("⚠ Please enter a name.")