# Import libraries
import function as f
# Main function
def main():
    # questions contains a list of dictionaries of all questions from questions.csv
    questions = f.read_csv(r'D:\Coding_Vs_Code\Mini_Projects\quiz_game\q_file.csv') 
    # answers contains a list of dictionaries of all answers from answers.csv
    answers = f.read_csv(r'D:\Coding_Vs_Code\Mini_Projects\quiz_game\a_file.csv') 

    # Ask player if they want to play or not
    if f.start_game():
        # Get the number of question user want to answer
        ques_limit = f.ques_range()

        # Total score and num of correct answer
        score, correct_ans = f.play_game(questions, ques_limit, answers)

        # Displaying the result
        f.display_result(score, correct_ans, ques_limit)
        
    else:
        print("Okay, may be next time.")

if __name__ == "__main__":
    main()