from random import randrange

from brain_games.engine import engine_game

rules = 'What number is missing in the progression?'


def get_question_answer():
    start = randrange(1, 11) #NOSONAR
    step = randrange(1, 6) #NOSONAR
    n = 10
    res = []
    for i in range(n):
        a = start + i * step
        res.append(str(a))
    
    index = randrange(0, len(res)) #NOSONAR
    correct_answer = res[index]
    res[index] = '..'
    question = ' '.join(res)
    return question, correct_answer


def brain_progression():
    engine_game(rules, get_question_answer)