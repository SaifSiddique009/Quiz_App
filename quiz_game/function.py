# Import necessary libraries
import csv
import random

# read csv file and return as list of dictionaries
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to start the game
def start_game():
    is_play = input("Do you want to play? (yes/no): ").lower()
    return is_play == 'yes'

# Function to get how many question user want to answer
def ques_range():
    no_of_ques = input("How many questions you want to answer? :")
    while no_of_ques.isdigit() == 0:
        no_of_ques = input("Please enter an integer larger than 0 :")
    while int(no_of_ques) <= 0:
        no_of_ques = input("Please enter an integer larger than 0 :")
    return int(no_of_ques)

# Function to update score and correct_ans
def play_game(questions, ques_limit, answers):
    # Choose random question as per user expectation
    ques_list = random.sample(questions, ques_limit)
    random.shuffle(ques_list)

    # Total scored points
    score = 0

    # Total correct answer given by user
    correct_ans = 0

    for question in ques_list:
        # Get user response for each question
        answer = input(question["question"] + ": ")

        # Update score and correct_ans
        score, correct_ans = check_answer(score, correct_ans, question["id"], answer, answers)
    
    return score, correct_ans

# Function to check user answer
def check_answer(score, correct_ans, ques_id, answer, answers):
    for ans in answers:
        if ques_id == ans["id"]:
            if answer == ans["answer"]:
                score += 2
                correct_ans += 1
            else:
                score -= 1
    return score, correct_ans

# Function to display result
def display_result(score, correct_ans, ques_limit):
    print(f"You've scoreed {score} points")
    percetage = (correct_ans / ques_limit) * 100
    print(f"Your success percentage is {percetage:.2f} %")