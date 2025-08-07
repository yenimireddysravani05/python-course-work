def welcome_message():
    print("🧪 Welcome to the Python Quiz Game!")

def ask_question(question, options, correct_answer):
    print(f"\n{question}")
    for key in options:
        print(f"{key}) {options[key]}")
    user_answer = input("Your answer (a/b/c/d): ").lower()

    if user_answer == correct_answer:
        print("✅ Correct!")
        return 1
    else:
        print(f"❌ Wrong! The correct answer is '{correct_answer}'")
        return 0

def run_quiz():
    score = 0
    questions = [
        {
            "question": "What is the output of: print(type([]))?",
            "options": {'a': "<class 'list'>", 'b': "<class 'dict'>", 'c': "<class 'set'>", 'd': "<class 'tuple'>"},
            "answer": 'a'
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": {'a': "function", 'b': "def", 'c': "fun", 'd': "define"},
            "answer": 'b'
        },
        {
            "question": "What is the output of 3 * '5'?",
            "options": {'a': "15", 'b': "555", 'c': "Error", 'd': "None"},
            "answer": 'b'
        },
        {
            "question": "Which of the following is immutable?",
            "options": {'a': "list", 'b': "dict", 'c': "set", 'd': "tuple"},
            "answer": 'd'
        },
        {
            "question": "How do you start a comment in Python?",
            "options": {'a': "//", 'b': "<!--", 'c': "#", 'd': "**"},
            "answer": 'c'
        },
        {
            "question": "What does len() do in Python?",
            "options": {'a': "Calculates size of int", 'b': "Returns list length", 'c': "Finds memory usage", 'd': "Loops through list"},
            "answer": 'b'
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": {'a': ".pt", 'b': ".python", 'c': ".py", 'd': ".pyt"},
            "answer": 'c'
        },
        {
            "question": "Which of the following is used to import a module?",
            "options": {'a': "include", 'b': "import", 'c': "using", 'd': "require"},
            "answer": 'b'
        },
        {
            "question": "What is the output of bool(0)?",
            "options": {'a': "True", 'b': "False", 'c': "0", 'd': "None"},
            "answer": 'b'
        },
        {
            "question": "What is used to define a block of code in Python?",
            "options": {'a': "Brackets {}", 'b': "Parentheses ()", 'c': "Indentation", 'd': "Curly braces"},
            "answer": 'c'
        },
        {
            "question": "Which function is used to get user input?",
            "options": {'a': "get()", 'b': "input()", 'c': "scan()", 'd': "read()"},
            "answer": 'b'
        },
        {
            "question": "Which of the following is a loop in Python?",
            "options": {'a': "repeat", 'b': "loop", 'c': "for", 'd': "during"},
            "answer": 'c'
        },
        {
            "question": "How do you print something in Python?",
            "options": {'a': "echo", 'b': "print()", 'c': "printf()", 'd': "write()"},
            "answer": 'b'
        },
        {
            "question": "What is the output of len('Python')?",
            "options": {'a': "6", 'b': "5", 'c': "7", 'd': "Error"},
            "answer": 'a'
        },
        {
            "question": "Which one is a Python data type?",
            "options": {'a': "number", 'b': "digit", 'c': "float", 'd': "decimal"},
            "answer": 'c'
        },
        {
            "question": "What is the output of 10 // 3?",
            "options": {'a': "3.3", 'b': "3", 'c': "3.0", 'd': "0"},
            "answer": 'b'
        },
        {
            "question": "What does == mean in Python?",
            "options": {'a': "Assignment", 'b': "Comparison", 'c': "Equal to None", 'd': "Loop"},
            "answer": 'b'
        },
        {
            "question": "Which one is not a Python keyword?",
            "options": {'a': "elif", 'b': "define", 'c': "pass", 'd': "in"},
            "answer": 'b'
        },
        {
            "question": "What is the output of type(10.5)?",
            "options": {'a': "int", 'b': "str", 'c': "float", 'd': "double"},
            "answer": 'c'
        },
        {
            "question": "Which symbol is used for exponentiation in Python?",
            "options": {'a': "^", 'b': "**", 'c': "//", 'd': "%"},
            "answer": 'b'
        }
    ]

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}:")
        score += ask_question(q["question"], q["options"], q["answer"])

    print(f"\n🎯 Your Final Score: {score}/20")

    if score == 20:
        print("🎉 Excellent! You got a perfect score!")
    elif score >= 15:
        print("👏 Great job! Keep practicing!")
    elif score >= 10:
        print("🙂 Good effort, but review some concepts.")
    else:
        print("📚 You need more practice. Keep learning!")

welcome_message()
run_quiz()
