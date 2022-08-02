# Question Class

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz Class

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.qIndex = 0

    def getQuestion(self):
        return self.questions[self.qIndex]
    
    def display(self):
        question = self.getQuestion()
        print(f'{question.text}')
        for q in question.choices:
            print('-' + q)
        answer = input('Answer: ')
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 10
        
        self.qIndex += 1
    
    def loadQuestion(self):
        if len(self.questions) == self.qIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.display()

    def showScore(self):
        print('***********************************\nScore: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.qIndex + 1

        if questionNumber > totalQuestion:
            print('***********************************\nQuiz Finished')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100, '*'))


q1 = Question("Which is a python framework?", ['Angular', 'React', 'Django', 'Vue.js', 'Meteor'], 'Django')
q2 = Question("What is the correct file extension for Python files?", ['.pyth', '.pt', '.pyt', '.py', '.pc'], '.py')
q3 = Question("Which method can be used to remove any whitespace from both the beginning and the end of a string?", ['strip()', 'trim()', 'ptrim()', 'remove()', 'len()'], 'strip()')
q4 = Question("Which method can be used to return a string in upper case letters?", ['uppercase()', 'upper()', 'upperCase()', 'toUpperCase()', 'upcase()'], 'upper()')
q5 = Question("Which method can be used to replace parts of a string?", ['switch()', 'repl()', 'rename()', 'replace()', 'replaceString()'], 'replace()')

qList = [q1, q2, q3, q4, q5]

quiz = Quiz(qList)
quiz.loadQuestion()


