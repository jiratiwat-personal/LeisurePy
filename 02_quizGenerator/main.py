from question_model import QuestionModel
from quiz_brain import QuizBrain
import data

question_bank = []
for i in range(len(data.question_data)):
    question_bank.append(QuestionModel(data.question_data[i]["text"], data.question_data[i]["answer"]))

quizBrain = QuizBrain(question_bank)
quizBrain.next_question()