import streamlit as st
import asyncio
import edge_tts
import os

st.title("🎙️ SADAF - Free Voice App")

# User se text lena
user_text = st.text_area("Yahan text likhein:", "Assalam-o-Alaikum Saifullah bhai, kaise hain aap?")

# Speed Control (Slider)
speed = st.slider("Awaaz ki Raftar (Speed):", 0.5, 2.0, 1.0)

# Speed ko Microsoft ke format mein badalna
speed_str = f"{'+' if speed >= 1.0 else '-'}{int(abs(speed-1)*100)}%"

async def generate_voice(text, rate):
    voice = "ur-PK-AsmaNeural"
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save("sadaf_voice.mp3")

if st.button("Awaaz Banayein"):
    if user_text:
        try:
            with st.spinner('Awaaz ban rahi hai...'):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(generate_voice(user_text, speed_str))
                
                if os.path.exists("sadaf_voice.mp3"):
                    st.audio("sadaf_voice.mp3")
                    st.success("Ye lijiye, bilkul free!")
        except Exception as e:
            st.error("Server busy hai, ek baar phir try karein.")
