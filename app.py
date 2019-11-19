print("This is Football Trivia!")
def startGame():
    user_continue = input('Would you like to play? Press Y or N: ')
    # print(user_continue)
    user_continue = user_continue.capitalize()
    if user_continue == 'Y':
        print('Awesome, Let\'s go!')
    elif user_continue =='N':
        print('Boo, fine then.')
    else:
        print('Not a valid input.')

def multiple_choice(score_for_mulitple):
    '''This will ask two mulitple choice question and returns the score'''
    score = 0
    print('This is the mulitple choice portion! Please answer with only letters a-e.')
    answer1 = input('How many points are scored in a touchdown?\n a. 7\n b. 10\n c. 3\n d. 5\n e. 9\n You\'re answer: ')
    if answer1 == 'a':
        print('That\'s correct! A touchdown is 7 points!')
        score += 1
        print(f'Score: {score}\n')
    else:
        print('Sorry, that\'s incorrect. Correct answer is a')
        print(f'Score: {score}\n')
    answer2 = input('How many teams are in the NFL?\n a. 20\n b. 30\n c. A Whole Bunch\n d. 32\n e. 16\n You\'re answer: ')
    if answer2 == 'd':
        print(f'That\'s correct. The answer is 32 teams!')
        score += 1
        print(f'Score: {score}\n')
    else:
        print('Sorry, wrong again. Correct answer is d')
        print(f'Score: {score}\n')

    
def add_to_total(num):
    '''This function adds a point to the total score'''
    pass


# startGame()
multiple_choice(0)
