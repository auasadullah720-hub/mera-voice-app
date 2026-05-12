import streamlit as st
import asyncio
import edge_tts
import os

st.title("Saifullah Bhai ka Super Voice App")

user_text = st.text_input("Yahan text likhein:", "Assalam-o-Alaikum, kaise hain aap?")

async def generate_voice(text):
    # Humne 'Asma' ki awaaz use ki hai jo zyada stable hai
    voice = "ur-PK-AsmaNeural" 
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("voice.mp3")

if st.button("Behtareen Awaaz Banayein"):
    if user_text:
        try:
            with st.spinner('Awaaz ban rahi hai...'):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(generate_voice(user_text))
                
                if os.path.exists("voice.mp3"):
                    st.audio("voice.mp3")
                    st.success("Ab check karein!")
                else:
                    st.error("Maafi chahte hain, awaaz ki file nahi ban saki. Dobara try karein.")
        except Exception as e:
            st.error(f"Server ka masla hai: {e}")
