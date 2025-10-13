from random import randrange

from brain_games.engine import engine_game

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_answer():
    n = randrange(1, 101)
    question = n
    if n < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
    correct_answer = 'yes' if is_prime else 'no'
    return question, correct_answer


def brain_prime():
    engine_game(rules, get_question_answer)