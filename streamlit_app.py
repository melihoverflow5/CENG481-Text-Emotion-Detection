import streamlit as st
import requests
import pandas as pd

# --- Page config ---
st.set_page_config(page_title="Emotion Detection", layout="centered")
st.title("🎭 Emotion Detection in Text")
st.markdown("Enter a sentence and analyze the emotional content with using custom DeBERTa model.")

# Emotion labels and colors (consistent with API)
label_map = {0: "sadness", 1: "joy", 2: "love", 3: "anger", 4: "fear", 5: "surprise"}

# --- User input ---
text_input = st.text_area("Input Text", height=100, placeholder="Type a sentence here...")
analyze = st.button("🔍 Analyze Emotion")

# --- Analyze action ---
if analyze and text_input.strip():
    with st.spinner("Analyzing... Please wait..."):
        try:
            response = requests.post(
                "http://localhost:5000/predict",  # Flask API endpoint
                json={"text": text_input.strip()}
            )
            if response.status_code == 200:
                result = response.json()

                # Show predicted emotion
                st.success(f"**Predicted Emotion:** `{result['predicted_label']}`")

                # Show bar chart of probabilities
                probs = result["label_probabilities"]
                df = pd.DataFrame({
                    "Emotion": list(probs.keys()),
                    "Probability": list(probs.values())
                }).sort_values(by="Probability", ascending=False)

                st.markdown("### Emotion Probabilities")
                st.bar_chart(df.set_index("Emotion"))

            else:
                st.error(f"Error: {response.status_code} — {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

elif analyze:
    st.warning("Please enter some text before analyzing.")
