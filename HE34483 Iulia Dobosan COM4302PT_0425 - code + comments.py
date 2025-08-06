import random  # We use this to mix (shuffle) the order of questions

# A dictionary with questions grouped by difficulty
questions = {
    "easy": [
        {"q": "What is the capital of France?", "options": ["Paris", "Rome", "Madrid"], "answer": "Paris"},
        {"q": "How many legs does a spider have?", "options": ["6", "8", "10"], "answer": "8"},
        {"q": "Which color is made by mixing red and white?", "options": ["Pink", "Orange", "Purple"], "answer": "Pink"}
    ],
    "medium": [
        {"q": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter"], "answer": "Mars"},
        {"q": "What is the largest ocean on Earth?", "options": ["Atlantic", "Pacific", "Indian"], "answer": "Pacific"},
        {"q": "In which year did World War II end?", "options": ["1945", "1939", "1918"], "answer": "1945"}
    ],
    "hard": [
        {"q": "Which element has the chemical symbol 'Au'?", "options": ["Gold", "Silver", "Copper"], "answer": "Gold"},
        {"q": "Who painted the ceiling of the Sistine Chapel?", "options": ["Da Vinci", "Michelangelo", "Raphael"], "answer": "Michelangelo"},
        {"q": "What is the capital city of Australia?", "options": ["Sydney", "Canberra", "Melbourne"], "answer": "Canberra"}
    ]
}

# This function asks one question and checks if the answer is correct
def ask_question(q_data):
    print("\nQuestion:", q_data["q"])  # Print the question text
    for i, option in enumerate(q_data["options"], start=1):  # Show all answer options
        print(f"{i}. {option}")
    try:
        choice = int(input("Choose an option (1/2/3): "))  # Ask user to type 1, 2, or 3
        if 1 <= choice <= len(q_data["options"]):  # Make sure the answer is a valid number
            selected = q_data["options"][choice - 1]  # Get the selected answer text
            return selected == q_data["answer"]  # Return True if correct, False if wrong
    except ValueError:
        pass
    print("Invalid input. Please choose 1, 2, or 3.")  # If the input is not valid, show the mesage and return
    return False  # If the input is invalid, ask the user to answer with 1, 2, or 3
    
# This function runs the whole quiz: Three questions from each level
def play_quiz():
    score = 0  # This is the starting score for points
    total_questions = 0  # this is the counter for how many questions were asked

    print("\n🎓 Starting Full General Knowledge Quiz!\n")  # Start message

    for level in ["easy", "medium", "hard"]:  # Go through each level of difficulty
        print(f"\n🔹 LEVEL: {level.upper()}")  # Show the name of the current level
        level_questions = questions[level].copy()  # Copy the list of questions for that level
        random.shuffle(level_questions)  # Change the order of the questions so that they come randomly

        for q_data in level_questions:  # Go through all the questions in the level
            total_questions += 1  # Add one point to the total questions count
            correct = ask_question(q_data)  # Ask the question and check answer
            if correct:
                print("✅ Correct!")  # Show the message that the answer is correct
                score += 1  # Add one point to score
            else:
                print(f"❌ Wrong! The correct answer was: {q_data['answer']}")  # Show the correct answer if wrong

    # When all the questions are done
    print(f"\n🏁 Quiz Finished! Your score: {score} out of {total_questions}")  # Message for the final score

# This function shows the main menu
def show_menu():
    while True:  # Keep going until the user decides to leave
        print("\n=== MAIN MENU ===")  # Menu header
        print("1. Play Quiz")  # Option 1
        print("2. Exit")       # Option 2
        choice = input("Enter your choice (1 or 2): ").strip()  # Get user input and remove spaces

        if choice == "1":  # If user wants to play
            play_quiz()  # Start the quiz
        elif choice == "2":  # If user wants to exit
            print("👋 Thanks for playing. Goodbye!")  # Message to say Goodbye
            break  # Exit the loop and end program
        else:
            print("❗ Invalid choice. Please enter 1 or 2.")  # Error if input is not valid

# Start the game by showing the menu first
if __name__ == "__main__":
    show_menu()  # Call the menu function
