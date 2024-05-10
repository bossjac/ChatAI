import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "Orenguteng/Llama-3-8B-Lexi-Uncensored"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define a function to interact with the model
def chat_with_model(user_input):
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    output = model.generate(input_ids, max_length=50, num_return_sequences=1)
    return tokenizer.decode(output[0], skip_special_tokens=True)

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
