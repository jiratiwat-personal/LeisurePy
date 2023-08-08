class QuizBrain:
    def __init__(self, question_bank):
        self.questionList = question_bank
        self.questionNumber = 0
        self.score = 0

    def next_question(self):
        solution = self.questionList[self.questionNumber].answer
        answer = input(f"Q.{self.questionNumber+1}: {self.questionList[self.questionNumber].question}. (True/False)?")
        self.questionNumber += 1
        if solution.lower() == answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print(f"Current score is: {self.score}/{self.questionNumber}\n")

        if self.questionNumber < len(self.questionList):
            self.next_question()
