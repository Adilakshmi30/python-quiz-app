questions = [
    {
        "question": "1.What is the output of 3 + 2 * 2?",
        "options": ["A. 10", "B. 7", "C. 9", "D. 8"],
        "answer": "B"
    },
    {
        "question": "2.Which keyword is used to create a function in Python?",
        "options": ["A. def", "B. function", "C. define", "D. fun"],
        "answer": "A"
    },
    {
        "question": "3.What data type is the object below? \n L = [1, 23, 'hello', 1]",
        "options": ["A. Dictionary", "B. List", "C. Tuple", "D. Set"],
        "answer": "B"
    },
    {
        "question" : "4.What does CPU stands for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Centre Process Unit", "D. Centre Processing Unit"],
        "answer": "B"
    },
    {
        "question" : "5.Who is the founder of Microsoft?",
        "options" : ["A. Steve Jobs", "B. Elon Musk", "C. Sundar Pichai", "D. Bill Gates"],
        "answer" : "D"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {q['answer']}")

print(f"\nYour final score is: {score}/{len(questions)}")

