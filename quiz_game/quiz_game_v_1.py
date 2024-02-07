# importing library
import csv 
import random

# creating qustion dictionary and get data from csv file
q_file_path = 'D:/Coding_Vs_Code/Mini_Projects/quiz_game/q_file.csv'
a_file_path = 'D:/Coding_Vs_Code/Mini_Projects/quiz_game/a_file.csv'

with open(q_file_path, "r") as q_file:
    q_reader = csv.reader(q_file, delimiter=',')
    next(q_reader) # for escaping first line

    q_dict = {}
    for row in q_reader:
        key = row[0]
        value = row[1]
        q_dict[key] = value 
    #print(q_dict)

# creating answer dict and get data from csv file
with open(a_file_path, 'r') as a_file:
    a_reader = csv.reader(a_file, delimiter=',')
    next(a_reader) # escaping first row

    a_dict = dict() # creating empty dict
    for row in a_reader:
        key = row[0]
        value = row[1]
        a_dict[key] = value
    #print(a_dict)

# Welcome message to user
print("Welcome to my quiz game!")
response = input("Do you want to play? ").lower()

while response == "yes":
    print("Lets Start Then..................")
    print("#################################")
    question = int(input("How many question you want to answer among 10: "))
    # print(sorted(q_dict.keys()))
    q_keys = random.sample(list(q_dict.keys()), question) # random.sample takes list or tuple as input, but ours is dict, so we have to convert it list to avoid type error.
    random.shuffle(q_keys)
    
    score = 0
    correct = 0
    for id in q_keys:
        print(q_dict[id], sep = ' ')
        answer = input().lower()
        if answer == a_dict[id]:
            score += 2
            print("Correct! You get 2 points. Current Points " + str(score))
            correct += 1
        else:
            score -= 1
            print("Incorrect! 1 point will be deducted. Current Points " + str(score))
    print("You have obtained " + str(score) + " scores and corrected " + str(correct) + " answers correctly")
    response = input("Do you want to play again? ").lower()
    
