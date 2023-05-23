import random
from typing import Generator


def send_message(message: str) -> str:
    print(f"Sending: {message}")
    return str(random.randint(1, 1000))


def chat(message: str) -> Generator[str, str, list[str]]:
    print("Starting a new chat")
    history = []

    while True:
        history.append(message)
        response = send_message(message)
        history.append(response)
        message = yield response
        if not message:
            return history


quick_chat = chat("hello")
print(next(quick_chat))
print(quick_chat.send("how are you doing?"))
print(quick_chat.send("oh, that is nice!"))

try:
    quick_chat.send("")
except StopIteration as e:
    print(e.value)
