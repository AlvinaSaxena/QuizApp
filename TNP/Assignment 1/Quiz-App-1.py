# Data storing in Program
users = {}

# Questions for each subject
quizzes = {
    "DSA": [
        {"question": "Which sorting algorithm has the best average case time complexity?", "options": ["Bubble Sort", "Merge Sort", "Insertion Sort", "Selection Sort"], "answer": 1},
        {"question": "What is the space complexity of depth-first search (DFS) using recursion?", "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "answer": 2},
        {"question": "Which data structure is used to implement recursion?", "options": ["Queue", "Stack", "Heap", "Graph"], "answer": 1},
        {"question": "What is the degree of a node in a tree?", "options": ["Number of child nodes", "Number of parent nodes", "Number of edges connected", "None of the above"], "answer": 0},
        {"question": "Which graph traversal algorithm uses a queue?", "options": ["DFS", "BFS", "Dijkstra", "Kruskal"], "answer": 1},
        {"question": "What is the purpose of a hash function?", "options": ["To compress data", "To map keys to indices", "To sort data", "To encrypt data"], "answer": 1},
        {"question": "What is the height of a balanced binary search tree with n nodes?", "options": ["O(log n)", "O(n)", "O(n^2)", "O(1)"], "answer": 0},
        {"question": "What is a complete binary tree?", "options": ["All levels are completely filled", "All nodes have 2 children", "All leaves are at the same level", "None of the above"], "answer": 0},
        {"question": "Which of these is a greedy algorithm?", "options": ["Kruskal's Algorithm", "Bubble Sort", "Depth-First Search", "Quick Sort"], "answer": 0},
        {"question": "Which data structure is used to detect a cycle in a graph?", "options": ["Stack", "Union-Find", "Queue", "Hash Table"], "answer": 1},
    ],
    "DBMS": [
        {"question": "Which command is used to create a database?", "options": ["CREATE DATABASE", "INSERT DATABASE", "SET DATABASE", "INIT DATABASE"], "answer": 0},
        {"question": "Which SQL clause is used to filter rows?", "options": ["WHERE", "GROUP BY", "ORDER BY", "HAVING"], "answer": 0},
        {"question": "Which type of join includes all rows from both tables?", "options": ["FULL JOIN", "INNER JOIN", "LEFT JOIN", "CROSS JOIN"], "answer": 0},
        {"question": "What is the main purpose of normalization?", "options": ["Reduce redundancy", "Speed up queries", "Backup data", "Increase storage"], "answer": 0},
        {"question": "Which of these is a DML command?", "options": ["SELECT", "DROP", "CREATE", "ALTER"], "answer": 0},
        {"question": "Which indexing technique is used for range queries?", "options": ["B+ Tree", "Hash Index", "Bitmap Index", "Clustered Index"], "answer": 0},
        {"question": "What is a transaction in DBMS?", "options": ["A sequence of operations", "A single SQL command", "A backup process", "An index creation"], "answer": 0},
        {"question": "Which of these is not a property of ACID?", "options": ["Isolation", "Atomicity", "Consistency", "Redundancy"], "answer": 3},
        {"question": "What is a composite key?", "options": ["Combination of two or more columns", "A key in another table", "A primary key", "A unique key"], "answer": 0},
        {"question": "Which SQL keyword is used to sort the result-set?", "options": ["ORDER BY", "SORT BY", "GROUP BY", "ARRANGE BY"], "answer": 0},
    ],
    "Python": [
        {"question": "Which of the following is used to declare a variable?", "options": ["var", "let", "No keyword", "define"], "answer": 2},
        {"question": "What is the output of print(10 // 3)?", "options": ["3", "3.3", "4", "Error"], "answer": 0},
        {"question": "Which of these is used for comments in Python?", "options": ["//", "#", "/* */", "<!-- -->"], "answer": 1},
        {"question": "Which keyword is used to create a class in Python?", "options": ["class", "Class", "define", "struct"], "answer": 0},
        {"question": "Which function is used to read input from the user?", "options": ["scan()", "read()", "input()", "get()"], "answer": 2},
        {"question": "What does the `open()` function do?", "options": ["Opens a file", "Creates a file", "Deletes a file", "None of the above"], "answer": 0},
        {"question": "Which method is used to add an element to a list?", "options": ["add()", "append()", "insert()", "push()"], "answer": 1},
        {"question": "What is the result of len('hello world')?", "options": ["10", "11", "12", "Error"], "answer": 1},
        {"question": "How do you define a dictionary in Python?", "options": ["{}", "[]", "()", "None"], "answer": 0},
        {"question": "Which of the following is used to handle exceptions in Python?", "options": ["try-except", "catch", "throw", "raise"], "answer": 0},
    ],
}


# User registration
def register():
    username = input("Enter a username= ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter a password= ")  
    users[username] = password
    print("Registration successful! Please log in to continue.")

# User login
def login():
    username = input("Enter your username= ")
    password = input("Enter your password= ")  
    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Function to conduct a quiz
def conduct_quiz(subject):
    print(f"\nStarting the {subject} quiz-->")
    score = 0
    questions = quizzes[subject]
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"{j + 1}. {option}")
        answer = int(input("Your answer (1-4): ")) - 1
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"\nQuiz finished! Your score: {score}/{len(questions)}")

# Quiz app
def main():
    while True:
        print("\nQuiz Application")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice= ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\nSubjects=")
                    print("1. DSA")
                    print("2. DBMS")
                    print("3. Python")
                    print("4. Logout")
                    subject_choice = input("Choose a subject (1 to 4)= ")
                    if subject_choice == "1":
                        conduct_quiz("DSA")
                    elif subject_choice == "2":
                        conduct_quiz("DBMS")
                    elif subject_choice == "3":
                        conduct_quiz("Python")
                    elif subject_choice == "4":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            print("Exiting application. Thank you for using our app!")
            break
        else:
            print("Invalid choice.")

if __name__ == "_main_":
    main()