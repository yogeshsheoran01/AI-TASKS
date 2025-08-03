import random

# Function to get a random bot response based on user input
def get_bot_response(user_input):
    # Define lists of keywords for different types of user messages
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "exit"]
    help_requests = ["help", "assist", "support"]

    # Convert user input to lowercase for easier matching
    user_input_lower = user_input.lower()

    # Check if the user input contains any greeting keywords
    if any(word in user_input_lower for word in greetings):
        return random.choice([
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Need any assistance?"
        ])
    # Check if the user input contains any farewell keywords
    elif any(word in user_input_lower for word in farewells):
        return random.choice([
            "Goodbye! Have a great day!",
            "See you soon!",
            "Bye! Take care!"
        ])
    # Check if the user input contains any help request keywords
    elif any(word in user_input_lower for word in help_requests):
        return random.choice([
            "I'm here to assist you. What do you need?",
            "How can I support you today?",
            "Let me know how I can help."
        ])
    # Check if the user is asking about the weather
    elif "weather" in user_input_lower:
        return "I can't check the weather, but I hope it's nice where you are!"
    # Check if the user is asking for the bot's name
    elif "name" in user_input_lower:
        return "I'm ChatBot, your virtual assistant."
    # Check if the user is asking for a joke
    elif "joke" in user_input_lower:
        return "Why did the programmer quit his job? Because he didn't get arrays!"
    # Default responses for unrecognized input
    else:
        responses = [
            "Can you please tell me more?",
            "That's interesting! Tell me more.",
            "I'm a chatbot, ask me anything.",
            "Could you elaborate on that?",
            "I'm always learning. What else can you share?"
        ]
        return random.choice(responses)

def main():
    # Print welcome messages
    print("Welcome to ChatBot! Type 'exit' to quit.")
    print("You can ask me about my name, tell me hello, or ask for a joke!")
    chat_history = []  # List to store the conversation history

    while True:
        user_input = input("You: ")  # Get user input
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break  # Exit the chat loop
        response = get_bot_response(user_input)  # Get bot response
        chat_history.append(("You", user_input))  # Add user message to history
        chat_history.append(("ChatBot", response))  # Add bot response to history
        print(f"ChatBot: {response}")  # Print bot response

    # Print the entire chat history after exiting
    print("\nChat History:")
    for speaker, message in chat_history:
        print(f"{speaker}: {message}")

if __name__ == "__main__":
    main()