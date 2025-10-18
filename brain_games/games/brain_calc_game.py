from random import choice, randrange

import prompt

from brain_games.cli import welcome_user


def brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')

    answer = 0
    while answer < 3:
        n1 = randrange(1, 51)  # NOSONAR
        n2 = randrange(1, 51)  # NOSONAR
        operator = choice(['+', '-', '*'])  # NOSONAR

        if operator == "+":
            res = n1 + n2
            print(f'Question: {n1} + {n2}')
        elif operator == "-":
            res = n1 - n2
            print(f'Question: {n1} - {n2}')
        elif operator == "*":
            res = n1 * n2
            print(f'Question: {n1} * {n2}')
        
        user_answer = prompt.integer('Your answer: ')
        if user_answer == res:
            print('Correct!')
            answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(." 
                  f"Correct answer was '{res}.'")
            print(f"Let's try again, {name}!")
            break
    if answer == 3:
        print(f'Congratulations, {name}!')