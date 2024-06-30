from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for data in question_data:
    question=Question(data["question"], data["correct_answer"])
    question_bank.append(question)

quiz_brain=QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    
print("You have completed the quiz.")
print(f"You have scored {quiz_brain.score} out of 12")