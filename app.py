import streamlit as st
import google.generativeai as genai

# Configure the API Key
try:
  GOOGLE_API_KEY = "AIzaSyD35TxKi_c67ZcVZ5TT0jH7My7FuVkyZWM"  # Replace with your actual API key
  genai.configure(api_key=GOOGLE_API_KEY)
except KeyError:
    st.error("API key not found. Please add your GOOGLE_API_KEY to Streamlit secrets.")
    st.stop()  # Stop execution if the key is missing

# Function to translate text
def translate_text(text, source_lang, target_lang):
    try:
        model = genai.GenerativeModel("gemini-pro") # Or a suitable Gemini model.
        prompt = f"""Translate the following {source_lang} text to {target_lang}:

        ```
        {text}
        ```
        """  # Improved prompt for better translations.

        response = model.generate_content(prompt)
        return response.text if response and response.text else "Translation error." # Check for valid response.

    except Exception as e:
        st.error(f"An error occurred during translation: {e}") # Display error in Streamlit.
        return None  # Return None to indicate failure.

# Streamlit UI
st.title("🌍 TransLingua - AI-Powered Translator")

# Input fields
source_text = st.text_area("Enter text to translate:", "")

# Language selection with more options
languages = ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Korean", "Hindi", "Telugu", "Arabic", "Russian"]  # Expanded language list
source_lang = st.selectbox("Select source language", languages)
target_lang = st.selectbox("Select target language", languages)

# Translate button
if st.button("Translate"):
    if source_text:
        with st.spinner("Translating..."):  # Show a spinner while translating
            translation = translate_text(source_text, source_lang, target_lang)
            if translation:  # Check if translation was successful
                st.subheader("Translated Text:")
                st.write(translation)
    else:
        st.warning("Please enter text to translate.")


# About section (optional)
st.sidebar.title("About TransLingua")
st.sidebar.info("TransLingua is a cutting-edge web application powered by Google's Gemini AI. It provides seamless language translation services. This is a demo application.")