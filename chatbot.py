import json
import os
import random

knowledge_base_path = "knowledge_base.json"


def load_knowledge_base():
    if os.path.exists(knowledge_base_path):
        with open(knowledge_base_path, "r") as file:
            return json.load(file)
    else:
        return {}


def save_knowledge_base(knowledge_base):
    with open(knowledge_base_path, "w") as file:
        json.dump(knowledge_base, file)


def get_response(user_input, knowledge_base):
    user_input = user_input.lower()

    if user_input in knowledge_base:
        responses = knowledge_base[user_input]
        return random.choice(responses)
    else:
        print("I'm sorry, I don't know the answer. Please provide one or more responses (type 'done' to finish): ")
        responses = []
        while True:
            response = input("> ")
            if response.lower() == "done":
                break
            responses.append(response)
        knowledge_base[user_input] = responses
        save_knowledge_base(knowledge_base)
        return "Thank you for teaching me."


def main():
    knowledge_base = load_knowledge_base()

    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            break

        response = get_response(user_input, knowledge_base)
        print("Chatbot:", response)

    print("Chatbot: Goodbye!")


if __name__ == "__main__":
    main()
