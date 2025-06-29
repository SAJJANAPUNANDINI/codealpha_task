# Basic Chatbot

def chatbot():
    print("Hello! I'm a simple chatbot. You can talk to me!")
    
    while True:
        user_input = input("You: ").lower()  # Get user input and convert to lowercase

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Exit the loop when user says 'bye'
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

# Start the chatbot
chatbot()