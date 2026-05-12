import streamlit as st
import asyncio
import edge_tts
import os

st.title("Saifullah Bhai ka Super Voice App")

# Text input box
user_text = st.text_input("Yahan text likhein:", "Assalam-o-Alaikum, kaise hain aap?")

async def generate_voice(text_to_speak):
    # 'Asma' ki awaaz urdu ke liye behtareen hai
    voice = "ur-PK-AsmaNeural"
    communicate = edge_tts.Communicate(text_to_speak, voice)
    await communicate.save("voice.mp3")

if st.button("Behtareen Awaaz Banayein"):
    if user_text:
        try:
            with st.spinner('Awaaz ban rahi hai...'):
                # Naya loop banane ka behtar tareeka
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(generate_voice(user_text))
                
                # Audio play karein
                audio_file = open("voice.mp3", "rb")
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")
                st.success("Mubarak ho! Awaaz taiyar hai.")
        except Exception as e:
            st.error(f"Server Busy hai, 1 minute baad try karein. Error: {e}")
