'''
Psedo Code
- I have two csv file, one constains some questions and answers, another contains multiple choice options for each questions. This two entity are linked with same id no. 
- I want to make an interactive quiz game in python. Where a player will prompt if they want to start the game or not. 
- Then if they agree, then the program will again ask them "Which version they want to play the game: Easy, Medium, Hard
- After selecting the version, one by one a question will come with four possible options. They have to give the correct answer. 
- If it is correct then a prompt with "Correct" message will show, otherwise "Incorrect, Correct Answer: " will be visible.
- Finally a score will be given to them and a status of how much knowledge they have.

To Do This, I have to 
- Read csv into two dict variable.
- Ask user first two prompt
- Randomly choose a number of questions and ask the user
- Give response on those answer, if incorrect provide correct answer, update score
- Finally display score and message.
'''

# Import libraries
import csv 
import random
import functions as f

# CSV file Path
csv_file_path = 'quiz_game_v1/data/'

# Welcome message
text = """
Welcome to the Anime Quiz Game!
How well do you know the world of anime?
Please choose your knowledge level from the following options:
(A) Beginner - You have watched a few popular anime shows and movies.
(B) Casual Viewer - You enjoy anime as a hobby and have seen a variety of genres and styles.
(C) Enthusiast - You are passionate about anime and have a broad and deep knowledge of its history and culture.
(D) Expert - You are an anime master and can recognize any character, plot, or reference.
(E) Otaku - You are obsessed with anime and have dedicated your life to it.
"""

# Message for cooperation
message = """
Please choose a valid option from the list below:
(A) Beginner - You have watched a few popular anime shows and movies.
(B) Casual Viewer - You enjoy anime as a hobby and have seen a variety of genres and styles.
(C) Enthusiast - You are passionate about anime and have a broad and deep knowledge of its history and culture.
(D) Expert - You are an anime master and can recognize any character, plot, or reference.
(E) Otaku - You are obsessed with anime and have dedicated your life to it.

If you enter an option that is not in the list, the game will ask you to try again until you choose a valid option. Please cooperate and have fun. 😊
"""

# "Please Choose Your Knowledge Level for Anime: \n(A) Beginner\n(B) Casual Viewer\n(C) Enthusiast\n(D) Expert\n(E) Otaku\n"

# Main functions
def main__():
    # Prompt user to play and difficulty level
    if f.is_playing():
        game_level = input(text)
        while(True):
            if game_level in ['a', 'b', 'c', 'd', 'e']:
                break
            else:
                game_level = input(message)
    else:
        print("Okay, may be next time")
        quit()
    
    # Get questions and answer from specific csv file
    questions = f.read_csv(csv_file_path, game_level, file_type = 'ques')
    answers = f.read_csv(csv_file_path, game_level, file_type = 'ans')

    # Start the game and get player score
    # score = f.play_game(questions, answers, game_level)

    # Display the result
    # f.display(score)
    # quiz_game_v1/data/begginer_ques.csv
    
# Call main funciton
if __name__ == "__main__":
    main__()