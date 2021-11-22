from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q_d in question_data:
    question_bank.append(Question(q_d["text"], q_d["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_q()

while quiz.still_has_q():
    quiz.next_q()

print("You`re completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.q_number}")