import core


def intro():
    name = input('Welcome to The Bowling Alley!\nWhat is your name? ')
    return name.capitalize()


def get_first_score():
    print('Please enter your scores:')
    first_score = input('First: ')
    if (first_score).is_integer() == True:
        if 0 <= int(first_score) <= 9:
            return int(first_score)
        else:
            print('Please enter a correct score.')
    elif first_score.lower() == 'x':
        return 'x'
    else:
        print('Please enter a correct score.')


def get_second_score(first_score):
    if first_score == 'x':
        return '-'
    else:
        second_score = input('Second: ')
        if (second_score).is_integer() == True:
            if 0 <= int(second_score) <= 9:
                return int(second_score)
            else:
                print('Please enter a correct score.')
        elif second_score.lower() == '/':
            return '/'
        else:
            print('Please enter a correct score.')


def show_score(game, name, total):
    round = 0
    print(f'\n{name}')
    for scores in game:
        round += 1
        print(f'Round {round}: {scores}\n')
    print(f'Total: {total}')


def main():
    game = []
    name = intro()
    total = 0
    rounds = 1
    while rounds <= 10:
        first_score = get_first_score()
        second_score = get_second_score(first_score)


if __name__ == '__main__':
    main()
