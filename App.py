import streamlit as st
import asyncio
import edge_tts
import os
import time

st.title("🎙️ SADAF - Real Voice Studio")

user_text = st.text_area("Yahan text likhein:", "Assalam-o-Alaikum Saifullah bhai, ab check karein!")
speed = st.slider("Awaaz ki Raftar (Speed):", 0.5, 2.0, 1.0)
speed_str = f"{'+' if speed >= 1.0 else '-'}{int(abs(speed-1)*100)}%"

async def generate_voice(text, rate):
    voice = "ur-PK-AsmaNeural"
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save("sadaf_real.mp3")

if st.button("Asli Awaaz Banayein"):
    if user_text:
        success = False
        attempts = 0
        while not success and attempts < 3:
            try:
                with st.spinner(f'Koshish #{attempts+1}: Awaaz ban rahi hai...'):
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(generate_voice(user_text, speed_str))
                    
                    if os.path.exists("sadaf_real.mp3"):
                        st.audio("sadaf_real.mp3")
                        st.success("Mubarak ho! Ye real awaaz hai.")
                        success = True
            except Exception:
                attempts += 1
                time.sleep(2) # 2 second intezar
        
        if not success:
            st.error("Microsoft ka server abhi bhi busy hai. 5 minute baad try karein.")
