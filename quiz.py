import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []
    start_time = None
    end_time = None

    def __init__(self):
        question_types = (Add, Multiply)

        for _ in range(10):
            num1 = random.randint(1, 250)
            num2 = random.randint(1, 250)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)

    def take_quiz(self):
        # log the start time
        self.start_time = datetime.datetime.now()
        # ask all questions
        for questions in self.questions:
            self.answers.append(self.ask(questions))
        else:
            self.end_time = datetime.datetime.now()
        # log answer
        # log the end time
        # Show a summery
        return self.summary()

    def ask(self, question):
        correct = False
        # Log the start time
        question_start = datetime.datetime.now()
        # capture the answer
        answer = input(question.text + " = ")
        # check the answer
        if answer == str(question.answer):
            correct = True
        # log the end time
        question_end = datetime.datetime.now()
        # if answer correct send back true
        # otherwise, send back false
        # Send back the elapsed time
        return correct, question_start, question_end

    def total_correct(self):
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        print('You got {} out of {} right!'.format(
            self.total_correct(), len(self.questions)
        ))
        print('It took you {} seconds in total'.format(
            (self.end_time - self.start_time).seconds
        ))


Quiz().take_quiz()
