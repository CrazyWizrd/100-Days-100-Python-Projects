from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["question"],question["correct_answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question:
    quiz_brain.next_question()

print(f"You have completed the Quiz\nYour final score was {quiz_brain.score}/{quiz_brain.question_number}")
