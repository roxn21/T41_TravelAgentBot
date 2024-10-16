from api import get_groq_response
from itinerary import generate_itinerary

def chatbot():
    print("Welcome to the Travel Agent Chatbot!")

    while True:
        user_input = input("Assistant: How can I help you today?\n")
        if "travel" in user_input.lower():
            destination = input("Assistant: Where would you like to travel?\n")
            days = int(input("Assistant: For how many days?\n"))
            itinerary = generate_itinerary(destination, days)
            print(itinerary)
        else:
            print("Assistant: Let me process your request with Groq AI.")
            response = get_groq_response(user_input)
            print(f"Assistant: {response}")

        # Check if the user wants to continue
        continue_chat = input("Do you want to ask anything else? (yes/no)\n")
        if continue_chat.lower() != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    chatbot()
