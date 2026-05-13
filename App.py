import streamlit as st
from gradio_client import Client
import os

# App setup
st.set_page_config(page_title="SADAF AI - Saifullah Edition", page_icon="🎙️")
st.title("🎙️ SADAF: Asli Insani Awaaz")

# Simple Interface
st.markdown("### Saifullah bhai, yahan apna message likhein:")
user_text = st.text_area("", "Assalam-o-Alaikum, aaj system 100% chalega!", height=100)

if st.button("▶️ Awaaz Banayein"):
    if user_text:
        try:
            with st.spinner('AI Model se rabta ho raha hai...'):
                # Ye Facebook ka sabse behtareen Urdu model hai
                client = Client("facebook/mms-tts-urd")
                result = client.predict(
                    text=user_text,
                    api_name="/predict"
                )
                
                if result:
                    st.audio(result)
                    st.success("Mubarak ho! Ye rahi asli insani awaaz.")
                else:
                    st.error("Model ne jawab nahi diya, ek baar phir click karein.")
        except Exception as e:
            st.error(f"Internet ya Server ka masla hai: {e}")
    else:
        st.warning("Pehle kuch likh toh lein!")

st.info("💡 Note: Ye robot nahi hai, ye Meta (Facebook) ka AI hai jo Urdu samajhta hai.")
