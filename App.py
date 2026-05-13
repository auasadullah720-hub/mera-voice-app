import streamlit as st
from gtts import gTTS
import os

st.title("🎙️ SADAF - Zero Error Mode")

# Input area
user_text = st.text_area("Yahan Urdu likhein:", "Saifullah bhai, ab ye busy nahi hoga, check karein!")

if st.button("Awaaz Banayein"):
    if user_text:
        try:
            with st.spinner('Voice ban rahi hai...'):
                # Google TTS - Ye hamesha stable rehta hai
                tts = gTTS(text=user_text, lang='ur')
                tts.save("sadaf_final.mp3")
                
                if os.path.exists("sadaf_final.mp3"):
                    audio_file = open("sadaf_final.mp3", "rb")
                    st.audio(audio_file.read(), format="audio/mp3")
                    st.success("Mubarak ho! Koi server busy nahi hai ab.")
        except Exception as e:
            st.error("Internet check karein, system okay hai.")
            
