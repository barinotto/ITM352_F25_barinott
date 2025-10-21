#Import the random module to randomize the order of the questions and options
import random
#Import the questions, options, explanations and answers from the json file
import json
#Import the time module to calculate the time taken to answer each question
import time

#Convert dictionary items to a list and randomize the order of the questions
#Used a defined function here for reusability and readability
def shuffle_questions(questions):
    question_items = list(questions.items())
    random.shuffle(question_items)
    return question_items 

#Randomize the order of the options
#Also used a defined function here for reusability and readability
def shuffle_options(options):
    random.shuffle(options)
    return options 

#Display intro message
#I used ANSI escape codes to make it bold and bright blue for welcome message
print("\033[1;94m               Welcome to the QuizGame! \033[0m")
print("\033[1;94m  The quicker you answer, the more bonus points you get!\033[0m")
print("\033[1;94m                Have Fun and Good luck!\033[0m")

#Prompt user with a question, options, explanation and validates the inputted answer
#Once again used a defined function for reusability and readability
def ask_question(question_num, question, details):
    options = shuffle_options(details["options"])
    correct_answer = details["correct"] 
    explanation = details["explanation"] 
    
    #Create labels A, B, C, D for the options
    labeled_options = {chr(65 + i): option for i, option in enumerate(options)}
    options_str = "\n".join([f"{label}: {option}" for label, option in labeled_options.items()])
    
    start_time = time.time() #Start the timer for the question
    #Loop until the user provides the correct answer
    while True:
        print(f"\n\033[1m{question_num}. {question}\033[0m")
        print(f"\n\033[1mOptions:\033[0m\n{options_str}")
        answer_label = input("\n\033[1mAnswer: \033[0m").upper()
        answer = labeled_options.get(answer_label)
        #When correct answer inputted, end timer, display "correct", explanation and time taken
        if answer == correct_answer:
            end_time = time.time() #End the timer
            time_taken = end_time - start_time #Calculate the time taken
            print("\n\033[1m\033[92m✅ Correct! Easy right??\033[0m")
            print(f"\033[1mExplanation: \033[0m{explanation}")
            print(f"\033[1mTime taken: \033[0m\033[95m{time_taken:.2f}\033[0m\033[1m seconds\033[0m\n")
            return True, time_taken
        #When incorrect answer inputted, display "wrong" and loop again
        else:
            print("\n\033[1m\033[91m❌ SO CLOSE! Try again big brain!\033[0m")

#Start the quiz; starting score is 0, total time is 0, and bonus points is 0
#One more time, using a defined function for reusability and readability
def main():
    score = 0
    correct_answers = []
    total_time = 0
    bonus_points = 0

    #Read questions from json file
    with open('quiz_questions.json', 'r') as file:
        QUESTIONS = json.load(file)

#Display the categories and allow user to choose a category
    categories = list(QUESTIONS.keys())
    print("\033[1mLet's Begin! Choose your category first! \033[0m")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    category_choice = int(input("\033[1mCategory: \033[0m")) - 1
    selected_category = categories[category_choice]
    selected_questions = QUESTIONS[selected_category]

#Randomize the order of the questions displayed
    question_items = shuffle_questions(selected_questions)

#Loop through the questions and answers
    question_num = 1
    for question, details in question_items:
        correct, time_taken = ask_question(question_num, question, details)
        #Calculate the score, time taken, and bonus points when correct answer inputted
        if correct:
            score += 1
            correct_answers.append(question)
            total_time += time_taken
            #Bonus points for answering quickly (1 point for every 3 seconds saved under 15 seconds)
            if time_taken < 15:
                bonus_points += int((15 - time_taken) / 3)
        question_num += 1

#Display end results and thank you message
    print("\033[1;94m===================================================== \033[0m")
    print(f"\033[1;94m    🌟 Your final score is {score}!\033[0m")
    print(f"\033[1;94m    🌟 Bonus points: {bonus_points}\033[0m")
    print(f"\033[1;94m    🌟 Total score with bonus: {score + bonus_points}\033[0m")
    print(f"\033[1;94m    🌟 Total time taken: {total_time:.2f} seconds\033[0m")
    print("\033[1;94m    🌟 You answered the following questions correctly:\033[0m")
    for i, question in enumerate(correct_answers, 1):
        print(f"\033[1;94m        {i}. {question}\033[0m")
    print("\033[1;94m===================================================== \033[0m")
    print("\033[1;94m         Thanks for playing!!\033[0m\n")

#Run the main function
if __name__ == "__main__":
    main()