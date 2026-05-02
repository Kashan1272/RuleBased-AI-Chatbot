from chatbot import get_response

print("Chatbot is running! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    response = get_response(user_input)
    print("Bot:", response)

    if user_input.lower() in ["exit", "bye"]:
        break