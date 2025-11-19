# Quiz Game
 
'''
1. A question with multiple answers.
2. The user chooses 1 answer.
3. Feedback on users answer.
4. Show next question.
'''

questions = [
"Who is Frances president ?",
"Which country won the previous World Cup ?",
"Whos the richest man in the world ?"
]

possible_answers = [
{"Emmanuel Macron":"a", "Donald Trump":"b", "Vladimir Putin":"c"},
{"France":"a", "Brazil":"b", "Argentina":"c"},
{"Elon Musk":"a", "Jeff Bezos":"b", "Bill Gates":"c"}
]

correct_answers = [
possible_answers[0]["Emmanuel Macron"],
possible_answers[1]["Argentina"],
possible_answers[2]["Elon Musk"]
]

def quiz_game(questions_list, possible_answers_list, correct_answers_list):
    score = 0
    for i in range(len(questions_list)):
        # Show question and possible answers
        print("\n",questions_list[i])
        for answer, letter in possible_answers_list[i].items():
            print(f"{letter}. {answer}")
        
        # The user chooses 1 answer.
        user_answer = input("Choose an answer: ")

        # Check if the answer is correct or not.
        if user_answer == correct_answers_list[i]:
            print("Correct answer")
            score += 1
        elif user_answer not in possible_answers_list[i].values():
            print("Invalid answer select a, b or c")
            continue 
        else:
            print("Wrong answer")
    
        # Show next question 
        i += 1
        
    print(f"Score : {score} / {len(questions_list)}")    
        
quiz_game(questions, possible_answers, correct_answers)

'''
# A question with multiple answers.
question = "Whats the capital of Rwanda ?"
possible_answers = {"Kigali":"a", "Yaounde":"b", "Paris":"c"}
correct_answer = possible_answers["Kigali"]

print(question)
for answer, letter in possible_answers.items():
    print(f"{letter}. {answer}")
    
# The user chooses 1 answer.
user_answer = input("Choose an answer: ")

# Check if the answer is correct or not.
if user_answer == correct_answer:
    print("Correct answer")
else:
    print("Wrong answer")
    
# Show next question 
print("Next question")
'''
