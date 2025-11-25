print("Chatbot:Hi!I'm your assistant.Type 'bye' to exit.")
while True:
    user_input=input("You:").lower()
    if user_input=="hi" or user_input=="hello":
        print("Chatbot:Hello!How can I help you?")
    elif user_input=="how are you":
        print("Chatbot:I'm good!What about you?")
    elif user_input=="who are you":
        print("Chatbot:I'm a simple rule-based chatbot created using python.")
    elif user_input=="what can you do":
        print("Chatbot:I can reply basrd on predefined rules using if-else!")
    elif user_input=="bye":
        print("Chatbot:Goodbye! Have a nice day!")
        break
    else:
        print("Chatbot:Sorry,I didn't understand that. Try something else.")