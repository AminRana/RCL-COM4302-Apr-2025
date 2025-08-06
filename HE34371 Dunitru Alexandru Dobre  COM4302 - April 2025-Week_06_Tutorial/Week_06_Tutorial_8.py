def ask_questions(questions):
    score = 0
    for q, a in questions:
        ans = input(q + " ")
        if ans.strip().lower() == a.lower():
            score += 1
    print("Your score:", score, "/", len(questions))

questions = [
    ("What is 2+2?", "4"),
    ("What is the capital of France?", "Paris"),
    ("What colour is the sky?", "Blue"),
    ("What is 5*6?", "30"),
    ("What programming language is this?", "Python"),
    ("What is the opposite of cold?", "Hot"),
    ("What comes after Monday?", "Tuesday"),
    ("How many legs does a spider have?", "8"),
    ("What is H2O?", "Water"),
    ("What planet do we live on?", "Earth"),
]

ask_questions(questions)