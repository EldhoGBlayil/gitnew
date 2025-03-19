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

# Dictionary mapping god names to their image files
GOD_IMAGES = {
    "Zeus": "zeus.jpg",
    "Poseidon": "poseidon.jpg",
    "Hades": "hades.jpg",
    "Apollo": "apollo.jpg",
    "Athena": "athena.jpg",
    "Ares": "ares.jpg",
    "Aphrodite": "aphrodite.jpg"
    # Add more gods and their image files as needed
}

# Stories of Greek gods
GOD_STORIES = {
    "Prometheus Steals Fire": """
    Long ago, humans lived in darkness without fire. Zeus had forbidden humans from having fire, 
    keeping it exclusively for the gods. Prometheus, a Titan who had helped create humans from clay, 
    felt sorry for their suffering. Against Zeus's orders, Prometheus stole fire from Mount Olympus by 
    hiding a flame in a hollow fennel stalk and brought it to humanity. This gift allowed humans to cook food, 
    stay warm, and begin developing civilization. When Zeus discovered this betrayal, he was furious. As punishment, 
    Zeus had Prometheus chained to a rock where an eagle would eat his liver each day, only for it to regenerate 
    each night so his torment could continue eternally. Eventually, Heracles (Hercules) freed Prometheus from 
    this punishment during his twelve labors.
    """,
    
    "Persephone and the Seasons": """
    Persephone was the beautiful daughter of Demeter, goddess of the harvest. One day while gathering flowers, 
    she was abducted by Hades, god of the underworld, who had fallen in love with her. Demeter was devastated 
    and in her grief, she caused all plants on Earth to wither and die, creating the first winter. Zeus eventually 
    intervened and ordered Hades to return Persephone. However, because Persephone had eaten six pomegranate seeds 
    in the underworld, she was bound to return to Hades for six months each year. During these months when Persephone 
    is with Hades, Demeter mourns and winter comes to the world. When Persephone returns to her mother, Demeter rejoices 
    and spring begins, explaining the cycle of the seasons.
    """,
    
    "The Judgment of Paris": """
    At the wedding of Peleus and Thetis, Eris, the goddess of discord, tossed a golden apple inscribed "For the fairest" 
    among the guests. Three goddesses claimed the apple: Hera, Athena, and Aphrodite. Zeus appointed Paris, a prince of Troy, 
    to judge who should receive the apple. Each goddess offered Paris a bribe: Hera offered power, Athena offered wisdom and 
    skill in battle, and Aphrodite offered the most beautiful woman in the world, Helen of Sparta. Paris chose Aphrodite's gift, 
    awarding her the golden apple. With Aphrodite's help, Paris abducted Helen (who was already married to King Menelaus of Sparta), 
    which led directly to the Trojan War, one of the most devastating conflicts in Greek mythology.
    """,
    
    "Orpheus and Eurydice": """
    Orpheus was a legendary musician whose music could charm all living things. He fell deeply in love with and married the beautiful 
    nymph Eurydice. Shortly after their wedding, Eurydice was bitten by a venomous snake and died. Devastated, Orpheus traveled to the 
    underworld to bring her back. His music so moved Hades and Persephone that they agreed to let Eurydice return to the world of the living, 
    but with one condition: Orpheus must walk in front of her and not look back until they both reached the upper world. As they neared the 
    surface, Orpheus, anxious to see if Eurydice was still behind him, turned to look at her. Because he turned before they had both reached 
    the upper world, Eurydice immediately vanished, this time forever. Orpheus spent the rest of his life in mourning until he too was killed, 
    finally reuniting with his beloved in the underworld.
    """,
    
    "Arachne's Challenge": """
    Arachne was a talented mortal weaver who boasted that her skills surpassed even those of Athena, goddess of crafts. Hearing this, 
    Athena disguised herself as an old woman and gave Arachne a chance to retract her boast. When Arachne refused, Athena revealed herself 
    and challenged Arachne to a weaving contest. Arachne's tapestry was flawless and depicted the gods' failings and misdeeds. Athena could 
    find no fault with Arachne's work but was angered by the disrespectful subject matter. In a fit of rage, Athena tore Arachne's tapestry 
    and struck her with her shuttle. Humiliated, Arachne attempted to hang herself. Taking pity, Athena transformed Arachne into a spider, 
    allowing her to weave for all eternity. This myth explains the origin of spiders and serves as a warning against pride and challenging the gods.
    """
}

# Interesting facts about Greek mythology
INTERESTING_FACTS = [
    "The ancient Greeks believed that dreams were messages from the gods and could foretell the future.",
    
    "Mount Olympus, home of the gods, is a real mountain in Greece and stands at 9,573 feet (2,918 meters) tall, making it the highest peak in Greece.",
    
    "Ancient Greek democracy excluded women, slaves, and foreigners, allowing only about 10-20% of the population to participate.",
    
    "The word 'typhoon' comes from Typhon, a monstrous storm giant considered the most deadly creature in Greek mythology.",
    
    "The constellation Scorpius is associated with the myth of Orion; after Orion boasted he could kill any creature, a giant scorpion killed him, and both were placed in the sky as constellations.",
    
    "The Greek afterlife had multiple locations including the Elysian Fields (paradise for heroes), Tartarus (prison for the wicked), and Asphodel Meadows (neutral area for ordinary souls).",
    
    "The Oracle of Delphi, Apollo's priestess, would enter a trance state possibly caused by natural gases from a geological fault under the temple.",
    
    "The ancient Olympic Games began in 776 BCE as a religious festival to honor Zeus, and athletes competed completely naked.",
    
    "Hermes was not just the messenger of the gods but also the patron of travelers, merchants, thieves, and orators.",
    
    "The myth of the Minotaur (half-man, half-bull) may have originated from Minoan bull-leaping ceremonies practiced in ancient Crete."
]

def get_available_gods():
    """Fetch a list of available gods from the API"""
    try:
        response = requests.get(f"{BASE_URL}/all")
        response.raise_for_status()
        gods_data = response.json()
        
        # Extract god names from the response
        if gods_data and isinstance(gods_data, list):
            return [god.get("name") for god in gods_data if god.get("name")]
        else:
            # If API doesn't return a list or format changes, use our predefined list
            return list(GOD_DESCRIPTIONS.keys())
            
    except requests.exceptions.RequestException:
        # Fall back to predefined list if API call fails
        return list(GOD_DESCRIPTIONS.keys())

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

# Set page configuration
st.set_page_config(
    page_title="GreekFetcher",
    page_icon="🔱",
    layout="wide"
)

# Add multi-page functionality
st.sidebar.title("🔱 Navigation")
page = st.sidebar.radio("Go to", ["God Explorer", "Family Tree", "Did You Know", "Stories"])

if page == "God Explorer":
    # ============ Greek Mythology Explorer ============ #
    st.title("🔱 Greek Fetcher")
    st.write("Select a Greek god to learn more about them!")

    # Get the list of available gods
    available_gods = get_available_gods()

    # Create dropdown for god selection
    selected_god = st.selectbox("Select a Greek god", available_gods)

    # Display god information when selected
    if selected_god:
        data = get_god_details(selected_god)
        
        if data and data.get("status") == "OK":
            # Extract correct fields safely
            god_name = data.get("name", selected_god)
            
            # Display image if available
            if god_name in GOD_IMAGES:
                try:
                    st.image(GOD_IMAGES[god_name], caption=f"Image of {god_name}", width=300)
                except Exception as e:
                    st.error(f"Could not load image: {e}")
            
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
            st.write(f"👨‍👩‍👧‍👦 Parents: {', '.join(parents) if parents else 'Unknown'}")
            st.write(f"👥 Siblings: {', '.join(siblings) if siblings else 'Unknown'}")
            st.write(f"💍 Spouses: {', '.join(spouses) if spouses else 'None'}")
            st.write(f"👶 Children: {', '.join(children) if children else 'Unknown'}")
            st.write(f"📜 Description: {description}")
        else:
            st.error(f"⚠ Could not retrieve information for {selected_god}.")

elif page == "Family Tree":
    # ============ Greek Mythology Family Tree Page ============ #
    st.title("🌳 Greek Mythology Family Tree")
    st.write("Explore the divine lineage of Greek mythology.")
    
    # Display family tree image
    try:
        st.image("Visual Family Tree of Greek Gods - Illustrated Connections.jpg", caption="Greek Mythology Family Tree", use_column_width=True)
    except Exception as e:
        st.error(f"Could not load family tree image: {e}")
    
    # Display text-based family tree with emojis
    st.subheader("📊 Text-Based Family Tree")
    
    family_tree = """

    🌌 Chaos  
     ├── 🌍 Gaia (Earth)  
     │    ├── ☁️ Uranus (Sky) → Mate of Gaia  
     │    │    ├── ⏱️ Cronus (Titan) → Married to Rhea  
     │    │    │    ├── ⚡ Zeus (King of gods, sky) → Married to Hera  
     │    │    │    │    ├── 🗡️ Ares (War)  
     │    │    │    │    ├── 🧪 Hebe (Youth)  
     │    │    │    │    ├── 🔨 Hephaestus (Forge, fire)  
     │    │    │    │    ├── 🎵 Apollo (Sun, music) → With Leto  
     │    │    │    │    ├── 🏹 Artemis (Hunt, moon) → With Leto  
     │    │    │    │    ├── 📨 Hermes (Messenger) → With Maia  
     │    │    │    │    ├── 🦉 Athena (Wisdom) → Born from Zeus' head  
     │    │    │    │    └── 🍷 Dionysus (Wine, festivity) → With mortal Semele  
     │    │    │    │    
     │    │    │    ├── 🌊 Poseidon (Sea) → Married to Amphitrite  
     │    │    │    │    └── 🐚 Triton (Sea god)  
     │    │    │    │    
     │    │    │    ├── 👑 Hades (Underworld) → Married to Persephone  
     │    │    │    │    
     │    │    │    ├── 🌾 Demeter (Agriculture) → Mother of Persephone  
     │    │    │    │    
     │    │    │    └── 🔥 Hestia (Hearth, home)  
     │    │    
     │    │    ├── 🌋 Oceanus (Titan of Sea) → Married to Tethys  
     │    │    │    
     │    │    ├── 💫 Hyperion (Titan of Light) → Married to Theia  
     │    │    │    
     │    │    ├── 🏛️ Coeus, Crius, Iapetus, Themis, Mnemosyne, Phoebe (Titans)  
     │    │    
     │    ├── 🌙 Nyx (Night)  
     │    ├── 🌑 Erebus (Darkness)  
     │    └── ⚫ Tartarus (Abyss)  
     │    
     │    
     ├── 🦸 Demigods & Heroes  
     │    ├── 💪 Heracles (Son of Zeus & Alcmene)  
     │    ├── ⚔️ Perseus (Son of Zeus & Danaë)  
     │    ├── 🛡️ Achilles (Son of Thetis & Peleus)  
     │    ├── 🧵 Theseus (Son of Poseidon or Aegeus)  
     │    ├── 🚢 Jason (Son of Aeson)  
     │    ├── 🧠 Odysseus (Son of Laertes)  
     │    └── 🎭 Orpheus (Son of Apollo or Oeagrus)  
     │    
     │    
     └── 💀 Underworld Figures  
          ├── ⛵ Charon (Ferryman of the dead)  
          ├── 🐕 Cerberus (Three-headed dog)  
          ├── 🔮 Hecate (Magic, ghosts)  
          └── ⚰️ Thanatos (Death)  
    """
    
    st.code(family_tree, language=None)
    
    # Add an explanation section
    st.subheader("📝 About the Family Tree")
    st.write("""
    This family tree shows the major figures in Greek mythology and their relationships. 
    The lineage begins with Chaos, the primordial void, and branches out to include:
    
    - The primordial deities (Gaia, Uranus, etc.)
    - The Titans (Cronus, Rhea, etc.)
    - The Olympian gods (Zeus, Poseidon, etc.)
    - Notable demigods and heroes
    - Important underworld figures
    
    Each deity is represented with an emoji that symbolizes their domain or characteristics.
    """)

elif page == "Did You Know":
    # ============ Did You Know Page ============ #
    st.title("🧠 Did You Know? - Greek Mythology Facts")
    st.write("Discover fascinating facts about Greek mythology that you might not know!")
    
    # Display interesting facts with numbers
    st.subheader("10 Interesting Facts About Greek Mythology")
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    # Display facts in two columns
    for i, fact in enumerate(INTERESTING_FACTS[:5], 1):
        with col1:
            st.markdown(f"**{i}. {fact}**")
            st.write("")
    
    for i, fact in enumerate(INTERESTING_FACTS[5:], 6):
        with col2:
            st.markdown(f"**{i}. {fact}**")
            st.write("")
    
    # Add a fun image related to Greek mythology facts
    try:
        st.image("Greek Gods.jpg", caption="Greek Mythology Fun Facts", use_column_width=True)
    except Exception:
        st.info("💡 Did you know? The word 'mythology' comes from the Greek words 'mythos' (story) and 'logos' (speech), literally meaning 'the telling of stories'.")
    
    # Add educational context
    st.subheader("Why Greek Mythology Matters Today")
    st.write("""
    Greek mythology continues to influence modern culture in numerous ways:
    
    - Many company logos and brands draw inspiration from Greek mythology (Nike, Amazon, etc.)
    - Countless books, movies, and video games incorporate Greek mythological themes
    - Astronomical bodies are named after Greek deities (planets, moons, constellations)
    - Psychological concepts like the Oedipus complex derive from Greek myths
    - Common English words and phrases have mythological origins ("Achilles' heel," "Pandora's box")
    
    Learning about Greek mythology helps us understand cultural references and appreciate the lasting impact of these ancient stories on our modern world.
    """)

else:  # Stories page
    # ============ Stories Page ============ #
    st.title("📚 Greek Mythology Stories")
    st.write("Read fascinating tales from Greek mythology.")
    
    # Create a selection for different stories
    selected_story = st.selectbox(
        "Choose a story to read:",
        list(GOD_STORIES.keys())
    )
    
    # Display the selected story
    if selected_story:
        st.subheader(f"📖 {selected_story}")
        st.write(GOD_STORIES[selected_story])
        
        # Add related imagery if available
        story_images = {
            "Prometheus Steals Fire": "prometheus_fire.jpg",
            "Persephone and the Seasons": "persephone_seasons.jpg",
            "The Judgment of Paris": "judgment_paris.jpg",
            "Orpheus and Eurydice": "orpheus_eurydice.jpg",
            "Arachne's Challenge": "arachne_athena.jpg"
        }
        
        try:
            st.image(story_images.get(selected_story, "Greek Gods.jpg"), caption=f"Illustration of {selected_story}", use_column_width=True)
        except Exception:
            pass
        
        # Add reflection questions for educational purposes
        st.subheader("🤔 Reflection Questions")
        
        reflection_questions = {
            "Prometheus Steals Fire": [
                "Why do you think Zeus didn't want humans to have fire?",
                "Was Prometheus right to steal fire for humanity despite Zeus's command?",
                "How does this myth explain humanity's relationship with technology?"
            ],
            "Persephone and the Seasons": [
                "How does this myth explain natural phenomena?",
                "What does Persephone's journey represent symbolically?",
                "How does this story reflect ancient Greek views on family relationships?"
            ],
            "The Judgment of Paris": [
                "Which gift would you have chosen if you were Paris?",
                "How does this myth demonstrate the consequences of choices?",
                "What does this story reveal about what the ancient Greeks valued?"
            ],
            "Orpheus and Eurydice": [
                "Why do you think Orpheus looked back before reaching the surface?",
                "What does this story teach us about love, trust, and patience?",
                "How does music function as a power in this myth?"
            ],
            "Arachne's Challenge": [
                "Was Athena's punishment of Arachne fair?",
                "What does this myth teach about pride and respecting the gods?",
                "How might this story have influenced how ancient Greeks viewed spiders?"
            ]
        }
        
        for question in reflection_questions.get(selected_story, []):
            st.markdown(f"- {question}")
        
        # List all available stories
        st.subheader("📚 All Available Stories")
        for i, story_title in enumerate(GOD_STORIES.keys(), 1):
            if story_title != selected_story:
                st.markdown(f"{i}. [{story_title}](#)")
