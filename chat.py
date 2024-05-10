from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Orenguteng/Llama-3-8B-Lexi-Uncensored")
model = AutoModelForCausalLM.from_pretrained("Orenguteng/Llama-3-8B-Lexi-Uncensored")

# Function to generate response
def generate_response(prompt):
    # Tokenize prompt
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)

    # Generate response
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100, temperature=0.9, num_return_sequences=1)
    
    # Decode and return response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Interactive chat loop
print("Welcome to the chatbot! Type 'exit' to end the conversation.")
while True:
    # Get user input
    user_input = input("You: ")

    # Check if user wants to exit
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Generate response
    response = generate_response(user_input)

    # Print response
    print("Bot:", response)

