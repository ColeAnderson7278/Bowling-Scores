import core


def intro():
    name = input('Welcome to The Bowling Alley!\nWhat is your name? ')
    return name.capitalize()


def get_first_score(name):
    while True:
        print(f'\n(X = Strike  / = Spare)\nPlease enter your score {name}:')
        first_score = input('First: ')
        if str(first_score).isdigit() == True and float(
                first_score).is_integer() == True:
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
        while True:
            second_score = input('\nSecond: ')
            if str(second_score).isdigit() == True and float(
                    second_score).is_integer() == True:
                if 0 <= int(second_score) <= 9:
                    return int(second_score)
                else:
                    print('Please enter a correct score.')
            elif second_score.lower() == '/':
                return '/'
            else:
                print('Please enter a correct score.')


def adding_to_total(first_score, second_score, total):
    if first_score == 'x':
        return 10
    elif second_score == '/':
        return 10
    else:
        return (int(first_score) + int(second_score))


def show_score(game, name, total):
    round = 0
    print(f'\n{name}')
    for scores in game:
        round += 1
        print(f'Round {round}: {scores}\n')
    print(f'Total: {total}')


def find_strike_spare(game):
    for rounds in game:
        if 'x' in rounds:
            if 'x' in game[(game.index(rounds))]:
                return 10
            elif '/' in game[(game.index(rounds))]:
                game = game[(game.index(rounds))]
                return game[0]
            else:
                return sum(game[(game.index(rounds))])
        elif '/' in rounds:
            if 'x' in game[(game.index(rounds))]:
                return 10
            elif '/' in game[(game.index(rounds))]:
                game = game[(game.index(rounds))]
                return game[0]
            else:
                return sum(game[(game.index(rounds))])


def main():
    game = []
    name = intro()
    rounds = 1
    while rounds <= 10:
        print(f'\nRound {rounds}')
        first_score = get_first_score(name)
        second_score = get_second_score(first_score)
        #total += adding_to_total(first_score, second_score, total)
        game.append([first_score, second_score])
        rounds += 1
        print(game)
    print(f'Total Score: {find_strike_spare(game)}')


if __name__ == '__main__':
    main()
