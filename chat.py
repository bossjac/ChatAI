import streamlit as st
from gradio_client import Client
import requests
from io import BytesIO

# Initialize the Gradio client
client = Client("KingNish/JARVIS")

# Streamlit app
st.title("Interactive Chat with JARVIS")

user_input = st.text_input("You:", "")

if user_input:
    if st.button("Send") or st.session_state.enter_pressed:
        with st.spinner("Thinking..."):
            # Call the JARVIS model
            result = client.predict(prompt=user_input, api_name="/translate")
            # Prepend the URL
            audio_url = "https://kingnish-jarvis.hf.space/file=" + result
            # Display the audio
            audio_response = requests.get(audio_url)
            st.audio(BytesIO(audio_response.content), format='audio/wav', start_time=0)
            # Set auto play
            st.write("""
                <audio id="player" autoplay>
                    <source src="%s" type="audio/wav">
                </audio>
            """ % audio_url, unsafe_allow_html=True)

def handle_enter(event):
    if event.key == "Enter":
        st.session_state.enter_pressed = True

# Register event handler
st.write("Press Enter to generate audio:")
st.script_request_queue.RerunData.insert(0, {"on_key_down": handle_enter})
