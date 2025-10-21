# Interactive Quiz Question Creator
# Ben Barinotto
# Date: 2025-10-20

# Using the JSON format to store questions, I asked AI to draft a template then added details
# Added details: Add the ability to add explanations to each correct answer following the quiz format

import json

def create_question():
    
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
    new_questions = []
    
    print("Welcome to the Extra Credit Quiz Question Creator!")
    
    while True:
        q = create_question()
        new_questions.append(q)
        
        another = input("Do you want to add another question? (y/n): ").strip().lower()
        if another != 'y':
            break
    
    # Try to read existing questions
    try:
        with open(filename, 'r') as f:
            existing_questions = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_questions = []
    
    # Combine existing and new questions
    all_questions = existing_questions + new_questions
    
    # Save all questions back to the file
    with open(filename, 'w') as f:
        json.dump(all_questions, f, indent=4)
    
    print(f"\n✅ {len(new_questions)} new questions added to '{filename}'")
    print(f"Total questions in file: {len(all_questions)}")
    print("Thank you for adding to our question pool! Goodbye now!")

if __name__ == "__main__":
    main()
