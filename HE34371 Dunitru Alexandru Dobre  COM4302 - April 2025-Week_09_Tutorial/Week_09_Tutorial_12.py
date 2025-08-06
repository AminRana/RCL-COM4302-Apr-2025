def ask_questions(questions):
    score = 0
    for q, a in questions:
        ans = input(q + " ")
        if ans.strip().lower() == a.lower():
            score += 1
    print("Score:", score, "/", len(questions))

questions = [
    ("What is 2+2?", "4"),
    ("Capital of UK?", "London"),
    ("Colour of banana?", "Yellow"),
    ("5x5?", "25"),
    ("Water's chemical formula?", "H2O"),
    ("Planet we live on?", "Earth"),
    ("Opposite of cold?", "Hot"),
    ("Sun rises from?", "East"),
    ("Largest ocean?", "Pacific"),
    ("Shape with 3 sides?", "Triangle")
]

ask_questions(questions)