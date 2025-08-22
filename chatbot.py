# CodSoft AI Internship – Task 1
# Created by Payal Sonwaniya

def intro():
    print("🤖 Hello! I'm your CodSoft ChatBot.")
    print("Type 'quit' to end the chat.\n")

def get_response(message):
    rules = {
        "hello": "Hi! How can I assist you?",
        "hi": "Hello there!",
        "your name": "I'm CodSoftBot, your internship helper 🤖",
        "how are you": "I'm just a bot, but doing great!",
        "bye": "See you soon. Have a great day!",
    }

    for key in rules:
        if key in message.lower():
            return rules[key]
    return "I'm sorry, I don't understand that."

def chat():
    intro()
    while True:
        user = input("You: ")
        if user.lower() == "quit":
            print("Bot: Chat ended. Goodbye! 👋")
            break
        reply = get_response(user)
        print("Bot:", reply)

chat()
