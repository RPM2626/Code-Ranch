import random

history = []
secret_number = ""


def generate_secret():
    digits = list("0123456789")
    random.shuffle(digits)
    return "".join(digits[:4])


def start_game():
    global secret_number, history
    secret_number = generate_secret()
    history = []


def evaluate_guess(guess):
    global secret_number, history

    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1

    result = {
        "guess": guess,
        "bulls": bulls,
        "cows": cows
    }

    history.append(result)
    return result


def get_history():
    return history


start_game()
