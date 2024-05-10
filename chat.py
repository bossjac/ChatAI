import streamlit as st
from gradio_client import Client
import requests
from io import BytesIO

# Initialize the Gradio client
client = Client("KingNish/JARVIS")

# Streamlit app
st.title("Interactive Chat with JARVIS")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            # Call the JARVIS model
            result = client.predict(prompt=user_input, api_name="/translate")
            # Prepend the URL
            audio_url = "https://kingnish-jarvis.hf.space/file=" + result
            # Display the audio with autoplay enabled
            audio_response = requests.get(audio_url)
            
            # Process the audio to remove "slash s" phrase
            audio_content = audio_response.content.replace(b"slash s", b"")
            
            # Display the text string
            st.text("Generated Text: " + result)
            # Display the audio
            st.audio(BytesIO(audio_content), format='audio/wav', autoplay=True)
    else:
        st.warning("Please enter something.")
