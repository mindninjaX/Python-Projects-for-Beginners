from questions import quiz

score = 0
skipped_questions = set()

print("Welcome to this fun food quiz!")
print("Are you ready to test your knowledge about food?")
print("There are a total of 20 questions. You can skip a question anytime by typing 'skip'.")
input("Press any key to start the fun ;) ")

for question in quiz:
    attempts = 3
    while attempts > 0:
        print(quiz[question]['question'])
        answer = input("Enter Answer (To move to the next question, type 'skip'): ")
        
        if answer == "skip":
            skipped_questions.add(question)
            break
        
        if quiz[question]['answer'].lower() == answer.lower():
            score += 1
            break
        
        attempts -= 1
        print(f"Wrong Answer :( \nYou have {attempts} attempt(s) left! \nTry again...")

print(f"\nYour final score is {score}!\n")

print("Skipped questions:")
for question_id in skipped_questions:
    print(quiz[question_id]['question'])
print("\n")

print("Correct answers:")
for question_id, ques_answer in quiz.items():
    print(f"Question: {ques_answer['question']}")
    print(f"Answer: {ques_answer['answer']}")
    print()

print("\nThanks for playing! 💜")
