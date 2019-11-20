print("This is Football Trivia!")
questions = ['How many points is a touchdown?', 'How many teams are in the NFL?', 'True or False: Can the ball only be thrown forward once?\nEnter 1 for True and 0 for False',
             'True or False: A first down is 5 yards from the line of play\nEnter 1 for True or 0 for False', 'How many people can be on the field from one team?\nEnter a number: ', 'Which year did football surpass baseball as America\'s favorite pasttime?\nEnter the year: ']
all_answers = ['a. 10\nb. 7\nc. 15\nd. 3\ne. 5\n:',
               'a. 20\nb. 24\nc. 32\nd. 18\ne. 30\n:', ':', ':', ':', ':']
correct_answers = [{'b', '7'}, {'c', '32'}, {'0', 'true'},
                  {'1', 'false'}, {'11', 'eleven'}, {'1965', '1965'}]
answers = ['A touchdown is 7 points', 'There are 32 teams in NFL', 'You can only throw the ball forward once',
                  'A first down is 10 yards or more gained in an play', 'Eleven people from each team can be on the field', 'Football surpassed baseball in 1965']

def quiz():
    score = 0
    for question, choices, correct_answer, answer in zip(questions,all_answers,correct_answers,answers):
        print(question)
        user_input = input(choices).lower()
        if user_input in correct_answer:
            print('Correct!')
            score += 1
        else:
            print('Incorrect!', answer)
    print(score,'out of', len(questions),'that is', float(score / len(questions)) * 100, '%')

if __name__=='__main__':
    quiz()
    