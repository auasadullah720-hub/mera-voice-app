import streamlit as st
from gtts import gTTS
import os

# App ka Title
st.title("🎙️ SADAF - Stable Voice App")

# Text Input
user_text = st.text_area("Yahan text likhein:", "Assalam-o-Alaikum Saifullah bhai!")

# Speed Option
speed_choice = st.checkbox("Slow Awaaz (Pyari lagti hai)")

if st.button("Awaaz Banayein"):
    if user_text:
        try:
            with st.spinner('Awaaz ban rahi hai...'):
                # gTTS (Google Text-to-Speech)
                tts = gTTS(text=user_text, lang='ur', slow=speed_choice)
                tts.save("sadaf_voice.mp3")
                
                # Play Audio
                audio_file = open("sadaf_voice.mp3", "rb")
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")
                st.success("Mubarak ho! Ye wala error nahi dega.")
        except Exception as e:
            st.error(f"Oho! Choti si galti hui: {e}")
