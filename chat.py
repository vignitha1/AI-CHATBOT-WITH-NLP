import random
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Custom Q&A pairs
custom_qna = {
    "what is your name": "I'm a friendly chatbot 😊",
    "how are you": "I'm doing well, thank you! How about you?",
    "who made you": "I was created by someone awesome!",
    "what can you do": "I can chat with you, answer simple questions, and keep you company."
}

# Intent-based replies
responses = {
    "greeting": {
        "keywords": ["hello", "hi", "hey"],
        "responses": ["Hey!", "Hi there!", "Hello!", "Nice to see you!"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye!", "Take care!", "Bye! Have a nice day."]
    },
    "thanks": {
        "keywords": ["thanks", "thank you"],
        "responses": ["You're welcome!", "No problem!", "Anytime!"]
    },
    "default": {
        "responses": ["I'm not sure I understand.", "Tell me more!", "Interesting... go on."]
    }
}
def tokenize(text):
    words = nltk.word_tokenize(text.lower())
    return [lemmatizer.lemmatize(w) for w in words]


def get_intent(user_input):
    tokens = tokenize(user_input)
    for intent, data in responses.items():
        if intent == "default":
            continue
        for keyword in data["keywords"]:
            if keyword in tokens:
                return intent
    return "default"

def get_response(user_input):
    # First, try direct match in custom Q&A
    lower_input = user_input.lower().strip()
    if lower_input in custom_qna:
        return custom_qna[lower_input]
    
    # Fallback to intent-based reply
    intent = get_intent(user_input)
    return random.choice(responses[intent]["responses"])

# Chatbot loop with logging
print("🤖 Bot: Hello! Ask me something or type 'bye' to quit.")

with open("chat_log.txt", "a") as log_file:
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            print("🤖 Bot: Bye! Take care.")
            log_file.write("You: " + user_input + "\n")
            log_file.write("Bot: Bye! Take care.\n")
            break
        reply = get_response(user_input)
        print("🤖 Bot:", reply)
        log_file.write("You: " + user_input + "\n")
        log_file.write("Bot: " + reply + "\n")
