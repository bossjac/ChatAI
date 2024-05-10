import streamlit as st
import requests
import tempfile
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from gradio_client import Client

# Initialize the Gradio client
client = Client("KingNish/JARVIS")

# Google Cloud Speech-to-Text setup
client_google = speech.SpeechClient()

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
            # Fetch the audio content
            audio_response = requests.get(audio_url)
            audio_content = audio_response.content

            # Transcribe the audio to text
            with tempfile.NamedTemporaryFile(delete=False) as tmp_audio_file:
                tmp_audio_file.write(audio_content)
                tmp_audio_file.close()

                # Open audio file
                with open(tmp_audio_file.name, 'rb') as audio_file:
                    content = audio_file.read()

                # Configure recognition
                audio = types.RecognitionAudio(content=content)
                config = types.RecognitionConfig(
                    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                    sample_rate_hertz=16000,
                    language_code='en-US'
                )

                # Perform recognition
                response = client_google.recognize(config=config, audio=audio)

                # Get transcription result
                transcribed_text = ''
                for result in response.results:
                    transcribed_text += result.alternatives[0].transcript

            # Display the transcribed text
            st.text("Transcribed Text: " + transcribed_text)
            # Display the generated text
            st.text("Generated Text: " + result)
            # Display the audio
            st.audio(BytesIO(audio_content), format='audio/wav', autoplay=True)
    else:
        st.warning("Please enter something.")
