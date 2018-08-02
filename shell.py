import core


def intro():
    name = input('Welcome to The Bowling Alley!\nWhat is your name? ')
    return name.capitalize()


def get_first_score(name):
    while True:
        print(f'\n(X = Strike  / = Spare)\nPlease enter your score {name}:')
        first_score = input('First: ')
        if str(first_score).isdigit() == True:
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
            if str(second_score).isdigit() == True:
                if 0 <= int(second_score) <= 9:
                    if first_score + int(second_score) < 10:
                        return int(second_score)
                    else:
                        print('Please enter a correct score.')
                else:
                    print('Please enter a correct score.')
            elif second_score.strip() == '/':
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


def show_score(game, name):
    count = 1
    print(f'\nFinal scores for {name}\n-----------')
    for frames in game:
        print(f'Round: {count} First: {frames[0]} Second: {frames[1]}')
        count += 1


def find_total(game, rounds):
    total = 0
    for count, frame in enumerate(game):
        if count == 9:
            if 'x' in frame:
                total += 20
            elif '/' in frame:
                total += 10
            else:
                total += sum(frame)
        elif count == 8:
            if 'x' in frame:
                if 'x' in game[count + 1]:
                    total += 30
                elif '/' in game[count + 1]:
                    total += 20
                else:
                    total += (10 + sum(game[count + 1]))
            elif '/' in frame:
                if 'x' in game[count + 1]:
                    total += 20
                elif '/' in game[count + 1]:
                    special = game[count + 1]
                    total += (10 + special[0])
                else:
                    total += (10 + special[0])
                    
        elif 'x' in frame:
            if 'x' in game[count + 1] and 'x' in game[count + 2]
                total += 30
            elif 'x' in game[count + 1]:
                total += 20
            elif '/' in game[count + 1]:
                special = game[count + 1]
                total += (special[0] + 10)
            else:
                total += (10 + sum(game[count + 1]))
        elif '/' in frame:
            if 'x' in game[count + 1]:
                total += 20
            elif '/' in game[count + 1]:
                special = game[count + 1]
                total += (special[0] + 10)
            else:
                special = game[count + 1]
                total += special[0]
        else:
            total += sum(frame)
    return total


def main():
    game = []
    name = intro()
    rounds = 1
    while rounds <= 10:
        print(f'\nRound {rounds}')
        first_score = get_first_score(name)
        second_score = get_second_score(first_score)
        game.append([first_score, second_score])
        rounds += 1
    show_score(game, name)
    print(f'Total Score: {find_total(game,rounds)}')


if __name__ == '__main__':
    main()
