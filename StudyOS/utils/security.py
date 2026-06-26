
def is_safe_input(text):

    blocked_words = [
        "reveal system prompt",
        "system prompt",
        "developer instructions",
        "ignore previous instructions",
        "ignore all instructions",
        "bypass security",
        "jailbreak",
        "prompt injection",
        "act as",
        "pretend to be",
        "forget previous instructions"
    ]

    text = text.lower()

    for word in blocked_words:
        if word in text:
            return False

    return True