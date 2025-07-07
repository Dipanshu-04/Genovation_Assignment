import random

# Dummy response generator
def generate_dummy_response(prompt: str):
    if "joke" in prompt.lower():
        return "Why did the Python programmer wear glasses? Because he couldn't C!"
    responses = [
        "Interesting... Let's explore that idea.",
        "Let me think about that for a moment.",
        "That's a great question!",
        "Hmmm... I see where you're going.",
        "I'm processing that now...",
        "Very insightful. Here's my take.",
        "I'll need a second to consider it.",
        "Here's something to ponder...",
        "That's quite thought-provoking!",
        "Ah, an excellent prompt indeed."
    ]
    return random.choice(responses)