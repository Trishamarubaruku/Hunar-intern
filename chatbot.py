def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "weather" in user_input:
        return "The weather today is sunny with a chance of clouds."

    elif "time" in user_input:
        from datetime import datetime
        return "The current time is: " + datetime.now().strftime("%H:%M:%S")

    elif "name" in user_input:
        return "I am your friendly chatbot!"

    elif "bye" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Step 3: User Interaction using input()
print("Welcome to the Chatbot! Type 'bye' to exit.")
while True:
    user_query = input("You: ")

    # Exit condition
    if user_query.lower() == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    # Step 4: Bot Responses based on rules
    bot_reply = chatbot_response(user_query)
    print("Bot:", bot_reply)


