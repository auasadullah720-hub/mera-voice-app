import streamlit as st
import asyncio
import edge_tts
import os

st.title("Saifullah Bhai ka Super Voice App")

user_text = st.text_input("Yahan text likhein:", "Assalam-o-Alaikum, kaise hain aap?")

async def generate_voice(text):
    voice = "ur-PK-FatimaNeural" 
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("voice.mp3")

if st.button("Behtareen Awaaz Banayein"):
    if user_text:
        with st.spinner('Awaaz ban rahi hai...'):
            asyncio.run(generate_voice(user_text))
            st.audio("voice.mp3")
