print("ChatBot: Hello! I am KavyaBot. Type 'help' to see commands or 'bye' to exit.")

while True:
    user_input = input("You: ").strip().lower()
    
    if user_input == "hello" or user_input == "hi":
        print("ChatBot: Hey there! Glad you said hi. How can I help?")
    
    elif user_input == "how are you":
        print("ChatBot: I'm just code, but I'm running perfectly! How about you?")
    
    elif user_input == "your name":
        print("ChatBot: I'm KavyaBot, built for Horizon TechX Task 4.")
    
    elif user_input == "help":
        print("ChatBot: I understand: hello, how are you, your name, bye")
    
    elif user_input == "bye":
        print("ChatBot: Goodbye! Thanks for chatting. Keep coding")
        break
    
    else:
        print("ChatBot: I didn't understand that. Type 'help' to see what I know.")