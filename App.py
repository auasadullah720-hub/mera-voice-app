import streamlit as st
from gtts import gTTS
import os

st.title("Saifullah Bhai ka Voice App")
user_text = st.text_input("Yahan text likhein:", "G kon bol raha hai?")

if st.button("Awaaz Banayein"):
    if user_text:
        tts = gTTS(text=user_text, lang='hi', slow=False)
        tts.save("voice.mp3")
        audio_file = open("voice.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
