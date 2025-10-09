from random import randrange

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def parity_check():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    answer = 0
    while answer < 3:
        n = randrange(1, 100)
        print(f'Question: {n}')
        user_answer = prompt.string('Your answer: ')
        correct = 'yes' if n % 2 == 0 else 'no'
        if user_answer == correct:
            print('Correct!')
            answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(." 
                  f"Correct answer was '{correct}'")
            print(f"Let's try again, {name}!")
            break
    if answer == 3:
        print(f'Congratulations, {name}')
    

def main():
    greet()
    parity_check()


if __name__ == '__main__':
    main()