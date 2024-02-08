**Project Overview 1: Quiz Game App in Python**

This project is a Python-based Quiz Game application. The application is designed to engage users in a fun and interactive quiz, sourced from a CSV file. The user's responses are validated against the correct answers stored in a separate CSV file, and scores are awarded based on their performance.

**Data Sources:** Two CSV files containing questions and answers for the quiz.

**Methodology:** The project followed these steps:

1. **Read the CSV files:** Used the `csv` module to read the questions and answers from the CSV files and store them in lists.
2. **Randomize the questions:** Used the `random` module to shuffle the questions and select a subset of them for the quiz.
3. **Ask the user for input:** Used the `input` function to prompt the user to enter their name and answer the questions.
4. **Check the answers:** Used a `for` loop and an `if-else` statement to compare the user's answers with the correct answers and update the score accordingly.
5. **Display the results:** Used the `print` function to show the user their final score and the correct answers.

**Tools:** Python, CSV files.

**Key Features:**

1. **Interactive Quiz:** The application prompts users with questions sourced from a CSV file, creating an engaging quiz environment.

2. **Answer Validation:** User responses are checked against the correct answers stored in a separate CSV file, ensuring accurate scoring.

3. **Scoring System:** The application implements a scoring system where each correct answer awards the user 2 points, while each incorrect answer deducts 1 point.

**Results:** The quiz game app successfully ran on Python and provided an interactive and fun way to test the user's knowledge.
