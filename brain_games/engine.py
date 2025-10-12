import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def engine_game(rules, get_question_answer):
    
    greet()
    name = welcome_user()
    print(rules)
    
    answer = 0
    rounds = 3

    while answer < rounds:
        question, correct_answer = get_question_answer()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')
    
        if user_answer == str(correct_answer):
            print('Correct!')
            answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if answer == rounds:
        print(f'Congratulations, {name}!')