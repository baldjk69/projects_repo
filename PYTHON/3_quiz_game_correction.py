# Quiz Game
 
questions = [
    "Who is Frances president ?",
    "Which country won the previous World Cup ?",
    "Whos the richest man in the world ?"
]

possible_answers = [
    {"a": "Emmanuel Macron", "b": "Donald Trump", "c": "Vladimir Putin"},
    {"a": "France", "b": "Brazil", "c": "Argentina"},
    {"a": "Elon Musk", "b": "Jeff Bezos", "c": "Bill Gates"}
]

correct_answers = ["a", "c", "a"]

def quiz_game(questions_list, possible_answers_list, correct_answers_list):
    score = 0
    for i in range(len(questions_list)):
        while True : # repeat until valid input
            # Show question and possible answers
            print(f"\nQuestion {i+1} {questions_list[i]}")
            for letter, answer in possible_answers_list[i].items():
                print(f"{letter}. {answer}")
        
            # The user chooses 1 answer.
            user_answer = input("Choose an answer (a, b or c) : ").lower()

            # Check for valid input
            if user_answer not in possible_answers_list[i]:
                print("Invalid answer select a, b or c")
                continue # repeat the same question 
            
            else: # Check correctness
                if user_answer == correct_answers_list[i]:
                    print("Correct answer")
                    score += 1
            
                else:
                    print(f"❌ Wrong! The correct answer was: "
                    f"{possible_answers_list[i][correct_answers_list[i]]}")
                
                break # move to next question 
        
    print(f"\nFinal score : {score} / {len(questions_list)}")    

# Run the game        
quiz_game(questions, possible_answers, correct_answers)

