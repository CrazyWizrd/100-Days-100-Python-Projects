class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def still_has_question(self):
        return len(self.question_bank) > self.question_number

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You are Right!!")
            self.score += 1
        else:
            print("You are Wrong!!")
        print(f"The correct answer was {correct_answer}\nYour current score is: {self.score}/{self.question_number}\n")

