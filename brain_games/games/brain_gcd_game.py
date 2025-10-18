from random import randrange

from brain_games.engine import engine_game

rules = 'Find the greatest common divisor of given numbers.'


def get_question_answer():
    n1 = randrange(1, 51) #NOSONAR
    n2 = randrange(1, 51) #NOSONAR
    question = f'{n1} {n2}'

    a = min(n1, n2)
    res = []
    for i in range(1, a + 1):
        if n1 % i == 0 and n2 % i == 0:
            res.append(i)
    correct_answer = max(res)
    return question, correct_answer
    

def brain_gcd():
    engine_game(rules, get_question_answer)
