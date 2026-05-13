import streamlit as st
import asyncio
import edge_tts
import os

st.set_page_config(page_title="SADAF AI", layout="centered")
st.title("🎙️ SADAF - Real Urdu Voice")

# Input
user_text = st.text_area("Yahan Urdu likhein:", "Saifullah bhai, ye sabse asan aur free tarika hai.")

async def generate_voice(text):
    # 'ur-PK-AsmaNeural' sabse natural Urdu awaaz hai
    communicate = edge_tts.Communicate(text, "ur-PK-AsmaNeural")
    await communicate.save("sadaf_final.mp3")

if st.button("Awaaz Banayein"):
    if user_text:
        with st.spinner('Awaaz ban rahi hai...'):
            try:
                # Running the async function
                asyncio.run(generate_voice(user_text))
                
                if os.path.exists("sadaf_final.mp3"):
                    st.audio("sadaf_final.mp3")
                    st.success("Ye lijiye Saifullah bhai!")
                    # File delete kar dete hain taake agli baar fresh bane
                    os.remove("sadaf_final.mp3")
            except Exception as e:
                st.error("Server ne phir nakhre kiye, ek baar phir button dabayein.")
    else:
        st.warning("Pehle kuch likh toh lein!")

st.info("💡 Ye Microsoft ki 'Neural' voice hai, jo aam robot se behtar hai.")
