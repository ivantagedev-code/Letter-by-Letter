import random
import streamlit as st

easy_words = ["hello", "castle", "garden", "window", "shadow", "pickle", "theory",
              "planet", "bridge", "candle", "jungle", "pencil", "rocket", "purple", "monkey"]

medium_words = ["volcano", "paradox", "nonsense", "skeleton", "aquarium", "telescope", "hurricane",
                "mountain", "elephant", "notebook", "universe", "keyboard", "umbrella",
                "adventure", "chocolate"]

hard_words = ["suspicious", "hypothesis", "government", "quarantine", "bureaucracy", "renaissance",
              "perseverance", "mischievous", "hippopotamus", "constellation",
              "refrigerator", "extraordinary", "responsibility", "communication",
              "pronunciation", "disappointment", "archaeology", "electricity"]

st.title("Letter by Letter")

options = ["Easy", "Medium", "Hard"]
selected_mode = st.selectbox("Choose your difficulty", options, index = None, placeholder="Difficulty?")
st.write(f"Your selected difficulty: {selected_mode}")