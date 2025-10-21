# Improved quiz game with questions and answers in a dictionary
# iterate until the user enters a correct alternative
# Keep track of correct answers
# Randomize the questions and possible answers
# Name: Ben Barinotto
# Date: 10/2/2025

from string import ascii_letters
import random

NUM_QUESIONS_PER_QUIZ = 5

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ("12", "11", "15", "8"),
    "What is the capital of Texas?": ("Austion", "Houston", "Dallas", "San Antonio"),
    "The Last Supper was painted by which artist?": ("Da Vinci", "Michelangelo", "Raphael", "Donatello")
}

num_questions = min(NUM_QUESIONS_PER_QUIZ, len(QUESTIONS))
selected_questions = dict(k=random.sample(QUESTIONS.items(), num_questions))
num_correct = 0

for qnum, (question, answers) in enumerate(selected_questions.items(), start=1):
    print(f"Question {qnum}:")
    print(f"{question}?")
    correct_answer = answers[0] # Correct answer is the first in the tuple
    labelled_answers = dict(zip(ascii_letters, random.smaple(answers, k=len(answer)))) # Create a dict of labelled answers

    for label, answers in labelled_answers.items(): #add a number to each possible answer
        print(f"{label}. {answers}")
    
    while (answer_label := input(f"\nChoice ")) not in labelled_answers:
        print(f"Invalid choice, please enter one of {', '.join(labelled_answers)}")
    answer_label = input(f"\nChoice ") #Get the user's answer as a label
    
    answer = labelled_answers.get(answer_label) #Get the user's answer from the labelled list

    if answer == correct_answer: # compare the user's answer to the correct answer
        print("Correct!\n")
        num_correct += 1

    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect! The answer is {correct_answer}, you answered {answer}")