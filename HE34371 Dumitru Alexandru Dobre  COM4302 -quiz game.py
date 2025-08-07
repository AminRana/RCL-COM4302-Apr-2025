# Simple Python Quiz Game with Menu
# Author: [AlexandruDobre]
# Purpose: To demonstrate menu-based interaction, loops, functions, and user input handling.

# Function to display the main menu
def show_menu():
    print("==== WELCOME TO THE PYTHON QUIZ GAME ====")
    print("1. Start Quiz")
    print("2. Instructions")
    print("3. Exit")

# Function to show instructions
def show_instructions():
    print("\n=== INSTRUCTIONS ===")
    print("You will be asked 10 multiple-choice questions.")
    print("Type the letter (A, B, C, or D) for your answer.")
    print("You will get 1 point for each correct answer.")
    print("Your total score will be shown at the end.\n")

# Function to run the quiz
def start_quiz():
    score = 0  # Variable to store the user's score

    # List of questions with options and correct answer
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which language is used to write Python?",
            "options": ["A. Snake", "B. Python", "C. English", "D. C++"],
            "answer": "B"
        },
        {
            "question": "What does CPU stand for?",
            "options": ["A. Central Process Unit", "B. Control Processing Unit", "C. Central Processing Unit", "D. Computer Personal Unit"],
            "answer": "C"
        },
        {
            "question": "Which data type is used to store text?",
            "options": ["A. int", "B. float", "C. str", "D. bool"],
            "answer": "C"
        },
        {
            "question": "Which symbol is used to comment in Python?",
            "options": ["A. //", "B. <!--", "C. #", "D. %"],
            "answer": "C"
        },
        {
            "question": "How do you start a function in Python?",
            "options": ["A. define", "B. function", "C. def", "D. fun"],
            "answer": "C"
        },
        {
            "question": "Which one is a loop in Python?",
            "options": ["A. if", "B. elif", "C. while", "D. switch"],
            "answer": "C"
        },
        {
            "question": "What will 3 * 2 ** 2 return?",
            "options": ["A. 36", "B. 12", "C. 18", "D. 12"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to exit a loop?",
            "options": ["A. stop", "B. exit", "C. break", "D. quit"],
            "answer": "C"
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A. .pyth", "B. .pt", "C. .py", "D. .p"],
            "answer": "C"
        }
    ]

    # Loop through each question in the list
    for index, q in enumerate(questions):
        print(f"\nQuestion {index + 1}: {q['question']}")
        for option in q["options"]:
            print(option)

        # Get the user's answer
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        # Check if the answer is correct
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1  # Increase score if correct
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    # Display final score
    print(f"\nQuiz finished! Your total score is {score}/10\n")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        start_quiz()
    elif choice == '2':
        show_instructions()
    elif choice == '3':
        print("Thank you for playing. Goodbye!")
        break  # Exit the loop and end the game
    else:
        print("Invalid input. Please select 1, 2, or 3.")
