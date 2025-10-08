# Improved quiz game with questions and answers in a dictionary
# Name: Ben Barinotto
# Date: 10/2/2025

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr?": ("12", "11", "15", "8"),
    "What is the capital of Texas?": ("Austion", "Houston", "Dallas", "San Antonio"),
    "The Last Supper was painted by which artist?": ("Da Vinci", "Michelangelo", "Raphael", "Donatello")
}

for question, answers in QUESTIONS.items():
    correct_answer = answers[0] # Correct answer is the first in the tuple
    sorted_answers = sorted(answers) # Sort answers alphabetically for display

    for label, answers in enumerate(sorted_answers, start=1): #add a number to each possible answer
        print(f"{label}. {answers}")
    
    answer_label = int(input(f"{question}?")) #Get the user's answer as a number
    user_answer = sorted_answers[answer_label - 1] #Get teh user's answer from the sorted list

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect! The answer is {correct_answer}, you answered {user_answer}")