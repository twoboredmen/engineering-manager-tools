from secrets import choice


LIST_OF_HELLO_MSGS = [
    "Hey! How are you doing?",
    "How is it going?",
    "Hey! Is everything going okay?",
    "Hey! Do you need any help?",
    "How are things going?",
    "How are you?",
    "Hey! What's shaking!",
]


def pick_hello_msg() -> str:
    """
    Randomise what hello message to return
    """
    return choice(LIST_OF_HELLO_MSGS)
