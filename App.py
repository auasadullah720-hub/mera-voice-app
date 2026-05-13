import streamlit as st
import asyncio
import edge_tts
import os

st.title("🎙️ SADAF - Real Voice")

user_text = st.text_area("Urdu likhein:", "Saifullah bhai, ab check karein!")

async def make_voice(text):
    # Asma ki awaaz sabse best hai
    communicate = edge_tts.Communicate(text, "ur-PK-AsmaNeural")
    await communicate.save("test.mp3")

if st.button("Awaaz Banayein"):
    if user_text:
        with st.spinner('Loading...'):
            try:
                asyncio.run(make_voice(user_text))
                if os.path.exists("test.mp3"):
                    st.audio("test.mp3")
                    st.success("Ye rahi awaaz!")
            except Exception as e:
                st.error("Server busy hai, 1 minute baad try karein.")
