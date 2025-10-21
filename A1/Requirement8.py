# Interactive Quiz Question Creator
# Ben Barinotto
# Date: 2025-10-20

# This version automatically saves all entered questions to a default file called 'quiz_questions.json'.


import json

def create_question():
    """
    Prompts the user to enter a question, four options, and the correct answer.
    Returns a dictionary representing the question.
    """
    question_text = input("Enter the question: ").strip()
    
    options = []
    for opt in ['a', 'b', 'c', 'd']:
        option_text = input(f"Enter option {opt}: ").strip()
        options.append(option_text)
    
    while True:
        answer = input("Enter the correct option (a/b/c/d): ").strip().lower()
        if answer in ['a', 'b', 'c', 'd']:
            break
        print("Invalid input. Please enter a, b, c, or d.")
    
    return {
        "question": question_text,
        "options": options,
        "answer": answer
    }

def main():
    """
    Main loop for creating multiple questions and saving them automatically.
    """
    filename = "new_quiz_questions.json"
    quiz_questions = []
    
    print("Welcome to the Quiz Question Creator!")
    
    while True:
        q = create_question()
        quiz_questions.append(q)
        
        another = input("Do you want to add another question? (y/n): ").strip().lower()
        if another != 'y':
            break
    
    # Save questions to a new file
    with open(filename, 'w') as f:
        json.dump(quiz_questions, f, indent=4)
    
    print(f"\n✅ {len(quiz_questions)} questions saved to '{filename}'")
    print("Thank you for creating new questions! Goodbye now!")

if __name__ == "__main__":
    main()
