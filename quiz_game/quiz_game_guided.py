import csv
import random

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def start_game():
    response = input("Do you want to play? (yes/no): ")
    return response.lower() == "yes"

def ask_question(questions):
    question = random.choice(questions)
    answer = input(question[1] + ": ")  # Assuming the question text is in the second column
    return question[0], answer  # Return the ID and the user's answer

def check_answer(question_id, user_answer, answers):
    for answer in answers:
        if answer[0] == question_id:
            return answer[1].lower() == user_answer.lower()
    return False

def update_score(is_correct, score):
    if is_correct:
        return score + 2
    else:
        return score - 1

def play_game(questions, answers):
    score = 0
    correct_answers = 0
    for _ in range(5):
        question_id, user_answer = ask_question(questions)
        is_correct = check_answer(question_id, user_answer, answers)
        if is_correct:
            correct_answers += 1
        score = update_score(is_correct, score)
    return score, correct_answers

def display_results(score, correct_answers):
    percentage = (correct_answers / 5) * 100  # Maximum score is 10 (5 questions * 2 points each)
    print(f"You scored {score} points, which is {percentage}% of the total.")

def main():
    # Read the questions and answers from the CSV files
    questions = read_csv(r'D:\Coding_Vs_Code\Mini_Projects\quiz_game\q_file.csv')
    answers = read_csv(r'D:\Coding_Vs_Code\Mini_Projects\quiz_game\a_file.csv')

    # Start the game if the user wants to play
    if start_game():
        # Play the game and get the final score
        score, correct_answers = play_game(questions, answers)

        # Display the results
        display_results(score, correct_answers)
    else:
        print("Okay, maybe next time!")

# Call the main function
if __name__ == "__main__":
    main()
