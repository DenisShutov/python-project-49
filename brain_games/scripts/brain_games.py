def greet():
    print('Welcome to the Brain Games!')

from brain_games.cli import welcome_user

def main():
    greet()
    welcome_user()

if __name__ == '__main__':
    main()