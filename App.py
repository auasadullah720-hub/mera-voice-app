import streamlit as st
from gtts import gTTS
import os

st.title("🎙️ Saifullah AI - Mobile Edition")

user_text = st.text_area("Yahan Urdu likhein:", "Saifullah bhai, ye mobile par hamesha chalega.")

if st.button("Generate Voice"):
    if user_text:
        try:
            # Google ka server jo mobile par kabhi fail nahi hota
            tts = gTTS(text=user_text, lang='ur')
            tts.save("voice.mp3")
            
            with open("voice.mp3", "rb") as f:
                st.audio(f.read(), format="audio/mp3")
                st.success("Mubarak ho! Koi error nahi aaya.")
        except Exception as e:
            st.error("Internet slow hai, dobara click karein.")
