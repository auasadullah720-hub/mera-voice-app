import streamlit as st
from gtts import gTTS
import os

st.title("Saifullah Bhai ka Voice App")

user_text = st.text_input("Yahan text likhein:", "Assalam-o-Alaikum, kaise hain aap?")

if st.button("Awaaz Banayein"):
    if user_text:
        try:
            # Urdu language support
            tts = gTTS(text=user_text, lang='ur', slow=False)
            tts.save("voice.mp3")
            
            audio_file = open("voice.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
            st.success("Ye lijiye awaaz taiyar hai!")
        except Exception as e:
            st.error(f"Masla aa gaya: {e}")
