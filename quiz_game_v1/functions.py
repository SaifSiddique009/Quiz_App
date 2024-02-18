# Import libraries
import csv
import random

# Fuction for read csv file
def read_csv(file_path, ques_level, file_type):
    # Get specific file as per player initial expertise
    ques_name = ''
    if file_type == 'ques':
        if ques_level == 'a':
            ques_name = 'begginer_ques.csv'
        elif ques_level == 'b':
            ques_name = 'casual_viewer_ques.csv'
        else:
            pass # More category will be added
    else:
        if ques_level == 'a':
            ques_name = 'begginer_ans.csv'
        elif ques_level == 'b':
            ques_name = 'casual_viewer_ans.csv'
        else:
            pass # More category will be added
    

    file_path = file_path + '/' + ques_name
    print(file_path)
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
    
def is_playing():
    status = input("Are You an Anime Lover? Do You Want to Know About Your Anime Knowledge?(yes/no): ").lower()
    response = bool
    while(True):
        if status == 'yes':
            response = True
            break
        elif status == 'no':
            response = False 
            break
        else:
            status = input("Please Enter a Valid Response (yes/no): ")
            continue
    return response

def play_game(questions, answers, level):
    no_of_questions = 0
    if level == 'a':
        no_of_questions = 5
    elif level == 'b':
        no_of_questions = 8
    elif level == 'c':
        no_of_questions = 11
    elif level == 'd':
        no_of_questions = 14
    else:
        no_of_questions = 17
def display(score):
    pass