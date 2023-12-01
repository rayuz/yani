#yani
# /\_/\       -----
#( o.o )_____/  |
# > ^ <       /____|

# Function to ask a question and check the answer
def ask_question(question):
    answer = input(f"{question} (Answer with 'meow' or 'rawr'): ").lower()
    return answer

# List of questions
questions = [
    "Will you love me forever?",
    "Will you always choose to stay?",
    "Would you live for me?",
    "Will you live with me?",
]

# Ask each question and check the answer
for q in questions:
    user_answer = ask_question(q)
    if user_answer == "meow":
        print("Purrfect! That's a 'Yes'! 😺")
    elif user_answer == "rawr":
        print("Oh no! That's a 'No'! 🦁")
    else:
        print("Please answer with 'meow' or 'rawr'.")

# Last special question
last_question = "Will you be my wifey?"
user_answer = ask_question(last_question)

# Final response based on the last answer
if user_answer == "meow":
    print("Congratulations! of course 'Yes' now you're my fiancée! 😻💍")
elif user_answer == "rawr":
    print("Oh no! That's a 'No' for being my wifey! 😿")
else:
    print("Please answer with 'meow' or 'rawr'.")
