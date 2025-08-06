Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> print("Hello world")
Hello world
Python file
# Multiple-Choice Quiz Game in Python
 
# List of quiz questions and answers
questions = [
   {
       "question": "What does CPU stand for?",
       "options": ["Central Processing Unit", "Computer Personal Unit", "Central Performance Utility", "Control Processing Unit"],
       "answer": "Central Processing Unit"
   },
   {
       "question": "Which language is primarily used for web development?",
       "options": ["Python", "Java", "HTML", "C++"],
       "answer": "HTML"
   },
   {
       "question": "Which of the following is a Python data type?",
       "options": ["array", "list", "record", "table"],
       "answer": "list"
   }
]
 
# Function to run the quiz
def run_quiz():
   score = 0
   print("Welcome to the Python Quiz Game!\n")
 
   for index, q in enumerate(questions):
       print(f"Q{index+1}: {q['question']}")
       for i, option in enumerate(q["options"]):
           print(f"  {i + 1}. {option}")
       
       try:
           choice = int(input("Enter your choice (1-4): "))
           if q["options"][choice - 1] == q["answer"]:
               print("Correct!\n")
               score += 1
           else:
               print(f"Wrong! The correct answer is: {q['answer']}\n")
       except (ValueError, IndexError):
           print("Invalid input. Please enter a number between 1 and 4.\n")
 
   print(f"You scored {score} out of {len(questions)}!")
 
# Start the game
if __name__ == "__main__":
   run_quiz()
 
