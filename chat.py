import streamlit as st
from gradio_client import Client

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
            st.write("JARVIS:", result)
    else:
        st.warning("Please enter something.")
