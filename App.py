import streamlit as st
import gradio_client as gr
import requests
import json
import os

# --- APP CONFIGURATION ---
st.set_page_config(layout="centered", page_title="Saifullah AI")
st.title("🎙️ Saifullah's RVC Studio")
st.subheader("Real Voice Cloning & Conversion")

# Sidebar for Settings
st.sidebar.header("RVC Settings")

# IMP: Yahan apni choice ke Model ka Link dalein (e.g., Hugging Face Space)
# Filhaal main aik default link dal rahi hoon, aap badal sakte hain.
RVC_MODEL_ENDPOINT = st.sidebar.text_input("RVC Model Endpoint:", "https://huggingface.co/spaces/example-user/rvc-space-url")
HF_TOKEN = st.sidebar.text_input("Hugging Face Token (Secret):", type="password")

# Speed Option
speed_factor = st.sidebar.slider("Awaaz ka Lahja (Speed/Pitch):", -12, 12, 0, help="Neg=Deep, Pos=High Pitch")

# --- UI Options ---
option = st.radio("Chunein ke kya karna hai:", ["Text se Apni Awaaz Banayein (TTS+RVC)", "Awaaz Badlein (VC)"])

if option == "Text se Apni Awaaz Banayein (TTS+RVC)":
    # Step 1: Text Input
    user_text = st.text_area("Yahan wo likhein jo aap apni awaaz mein bulwana chahte hain:", "Assalam-o-Alaikum Saifullah bhai, ab main bol raha hoon aapki awaaz mein!")
    
    # Step 2: Source Voice (TTS) - Hum default Urdu female voice use kar ke uspar RVC lagayenge
    st.info("AI pehle Urdu text ko simple awaaz mein badlega, phir use RVC ke zariye aapki awaaz mein convert karega.")

    if st.button("Clone voice Generate Karein"):
        if not user_text:
            st.error("Pehle text likhein.")
        elif not RVC_MODEL_ENDPOINT.startswith("https://huggingface.co/spaces/"):
            st.error("Sidebar mein valid Hugging Face Space ka Link dalein.")
        elif not HF_TOKEN:
            st.error("Sidebar mein valid Hugging Face Token (API Key) dalein.")
        else:
            with st.spinner('Zabardast voice ban rahi hai... (Thora waqt lagega)'):
                try:
                    # RVC API Call
                    # Note: Ye call exact tabhi kaam karegi jab upar link sahi hoga.
                    client = gr.Client(RVC_MODEL_ENDPOINT, hf_token=HF_TOKEN)
                    
                    # We send text directly to the model. Many spaces have TTS built-in now.
                    # API calls need specific parameters depending on how the RVC space is set up.
                    # This is an example call:
                    # results = client.predict(user_text, speed_factor, api_name="/tts")
                    
                    # Instead, we will simulate a full conversion flow
                    results = client.predict(
                            user_text,	# str in 'User Input Text' Textbox component
                            # Additional options if needed by the specific Space...
                            # speed_factor,
                            api_name="/predict"
                    )
                    
                    st.success("Mubarak ho! Aapki clone voice tayar hai.")
                    # Results will vary; many return path or tuple
                    if isinstance(results, tuple):
                        st.audio(results[0])
                    elif isinstance(results, str):
                        st.audio(results)

                except requests.exceptions.HTTPError as e:
                    st.error(f"Error: Connection Fail (Link check karein): {e}")
                except Exception as e:
                    st.error(f"Server is busy, try again: {e}")

elif option == "Awaaz Badlein (VC)":
    st.write("### Voice to Voice Conversion")
    uploaded_file = st.file_uploader("Apni recorded awaaz upload karein ya text read karein:", type=['mp3', 'wav', 'm4a'])

    if uploaded_file:
        st.audio(uploaded_file)
        if st.button("Awaaz Convert Karein"):
            if not RVC_MODEL_ENDPOINT or not HF_TOKEN:
                 st.error("Link ya Token missing hai!")
            else:
                with st.spinner("RVC is processing..."):
                    try:
                        # Gradio client needs path, so we save file briefly
                        with open("temp_upload.wav", "wb") as f:
                            f.write(uploaded_file.getbuffer())

                        # Send file to RVC space
                        client = gr.Client(RVC_MODEL_ENDPOINT, hf_token=HF_TOKEN)
                        result = client.predict("temp_upload.wav", speed_factor, api_name="/convert")

                        st.success("Awaaz badal gayi!")
                        if isinstance(result, str):
                            st.audio(result)
                        
                        os.remove("temp_upload.wav")

                    except Exception as e:
                        st.error(f"Error converting voice: {e}")
