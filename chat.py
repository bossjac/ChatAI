import streamlit as st
from transformers import pipeline

# Load the model
model = pipeline("text-to-text-generation", model="Orenguteng/Llama-3-8B-Lexi-Uncensored")

# Define a function to interact with the model
def chat_with_model(user_input):
    response = model(user_input)
    return response[0]['generated_text']

# Streamlit app
st.title("Interactive Chat with Llama-3-8B-Lexi-Uncensored")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            bot_response = chat_with_model(user_input)
            st.write("Llama-3-8B-Lexi-Uncensored:", bot_response)
    else:
        st.warning("Please enter something.")
