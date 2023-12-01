def ask_yes_no_question(question):
    answer = input(f"{question} (Answer with 'yes' or 'no'): ").lower()
    return answer

def play_yes_no_game():
    questions = [
        "Will you love me forever?",
        "Will you always choose to stay?",
        "Would you live for me?",
        "Will you live with me?",
    ]

    for q in questions:
        user_answer = ask_yes_no_question(q)
        if user_answer == "yes":
            print("Purrfect! That's a 'Yes'! 😺")
        elif user_answer == "no":
            print("Oh no! That's still a 'yes'! 🦁")
        else:
            print("Please answer with 'yes' or 'no'.")

    last_question = "Will you be my wifey?"
    user_answer = ask_yes_no_question(last_question)

    if user_answer == "yes":
        print("Congratulations! Of course 'Yes'! Now you're my fiancée! 😻💍")
    elif user_answer == "no":
        print("Oh no! A 'No' means 'No' for being my wifey! 😿")
    else:
        print("Sorry, I didn't understand your answer. Please try again with 'yes' or 'no'.")

# Run the game
play_yes_no_game()
