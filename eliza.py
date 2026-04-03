from nltk.chat.util import Chat, reflections


CUSTOM_PAIRS = [
    (
        r"^\s*(hi|hello|hey)\b.*",
        (
            "Hello. What is your name?",
            "Hi there. How are you feeling?",
            "Hey. How are you doing today and what is your name?",
        ),
    ),
    (
        r".*\b(my name is|i am called)\s+([A-Za-z]+).*",
        (
            "Hello %2. What would you like to talk about today?",
            "Nice to meet you, %2. How are you feeling today?",
        ),
    ),
    (
        r".*\b(i feel|i am feeling)\s+(.+)",
        (
            "What do you think is making you feel %2?",
            "How long have you been feeling %2?",
            "What usually happens when you start feeling %2?",
        ),
    ),
    (
        r".*\b(i am|i'm)\s+(stressed|anxious|worried|overwhelmed)\b.*",
        (
            "What seems to be causing you to feel %2?",
            "When do you notice that feeling of %2 the most?",
            "What would help you feel less %2 right now?",
        ),
    ),
    (
        r".*\b(i need)\s+(.+)",
        (
            "Why do you need %2?",
            "What would it mean for you if you got %2?",
            "What is making %2 important to you right now?",
        ),
    ),
    (
        r".*\b(i can't|i cannot)\s+(.+)",
        (
            "What makes you think you cannot %2?",
            "Have you tried to %2 before?",
            "What do you think is stopping you from %2?",
        ),
    ),
    (
        r".*\b(because)\s+(.+)",
        (
            "Does %2 feel like the main reason?",
            "What led you to that conclusion?",
            "Is there anything else besides %2 affecting this?",
        ),
    ),
    (
        r".*\b(school|university|class|assignment|exam|test)\b.*",
        (
            "What part of school is feeling most difficult right now?",
            "Is this more about workload, understanding the work, or time pressure?",
            "How has this been affecting you academically or personally?",
        ),
    ),
    (
        r".*\b(friend|family|mother|father|brother|sister)\b.*",
        (
            "Tell me more about that relationship.",
            "How does this person affect the way you feel?",
            "What would you like to be different in that situation?",
        ),
    ),
    (
        r".*\b(yes|yeah|yep)\b.*",
        (
            "You seem quite certain.",
            "I see. Can you tell me a little more?",
            "What makes you feel sure about that?",
        ),
    ),
    (
        r".*\b(no|not really|nope)\b.*",
        (
            "Why not?",
            "What makes you feel that way?",
            "Can you say a bit more about that?",
        ),
    ),
    (
        r".*\b(quit|exit|bye|goodbye)\b.*",
        (
            "Goodbye. Take care of yourself.",
            "Bye for now. I appreciated our conversation.",
        ),
    ),
    (
        r"(.*)",
        (
            "Can you tell me more about that?",
            "Why do you say that?",
            "What about that stands out to you most?",
        ),
    ),
]


eliza_chatbot = Chat(CUSTOM_PAIRS, reflections)


def get_eliza_response(user_input: str) -> str:
    return eliza_chatbot.respond(user_input)


if __name__ == "__main__":
    print("ELIZA Chatbot")
    print("Type 'quit' to stop.\n")
    eliza_chatbot.converse()
