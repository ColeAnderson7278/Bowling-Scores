import core


def intro():
    name = input('Welcome to The Bowling Alley!\nWhat is your name? ')
    return name.capitalize()


def first_for_tenth(name, frame):
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


def get_first_score(name, frame):
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


def get_second_score(first_score, frame):
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


def show_score(game, name):
    count = 1
    print(f'\nFinal scores for {name}\n-----------')
    for frames in game:
        if count == 10:
            if len(frames) == 3:
                print(
                    f'Frame: {count} First: {frames[0]} Second: {frames[1]} Third: {frames[2]}'
                )
                count += 1
            else:
                print(f'Frame: {count} First: {frames[0]} Second: {frames[1]}')
                count += 1
        else:
            print(f'Frame: {count} First: {frames[0]} Second: {frames[1]}')
            count += 1


def play_tenth(name, frame):
    first_score = first_for_tenth(name, frame)
    if str(first_score).isdigit() == True:
        while True:
            second_score = input('\nSecond: ')
            if str(second_score).isdigit() == True:
                if (int(second_score) + int(first_score)) < 10:
                    total = (int(second_score) + int(first_score))
                    tenth_frame = [int(first_score), int(second_score)]
                    return tenth_frame, total
                else:
                    print('Please enter a correct score.')
            elif second_score == '/':
                while True:
                    third_score = input('\nThird: ')
                    if str(third_score).isdigit() == True:
                        if 0 <= int(third_score) < 10:
                            total = (10 + int(third_score))
                            tenth_frame = [
                                int(first_score), '/',
                                int(third_score)
                            ]
                            return tenth_frame, total
                    elif third_score == 'x':
                        tenth_frame = [int(first_score), '/', 'x']
                        return tenth_frame, 20
                    else:
                        print('Please enter a correct score.')
            else:
                print('Please enter a correct score.')
    elif first_score == 'x':
        while True:
            second_score = input('\nSecond: ')
            if str(second_score).isdigit() == True:
                if int(second_score) < 10:
                    while True:
                        third_score = input('\nThird: ')
                        if str(third_score).isdigit() == True:
                            if (int(third_score) + int(second_score)) == 10:
                                tenth_frame = ['x', int(second_score), '/']
                                return tenth_frame, 20
                            elif (int(second_score) + int(third_score)) < 10:
                                total = 10 + (int(second_score) + int(third_score))
                                tenth_frame = [
                                    'x', int(second_score),
                                    int(third_score)
                                ]
                                return tenth_frame, total
                            else:
                                print('Please enter a correct score.')
                else:
                    print('Please enter a correct score.')
            elif second_score == 'x':
                while True:
                    third_score = input('\nThird: ')
                    if str(third_score).isdigit() == True:
                        if 0 <= int(third_score) < 10:
                            total = (20 + third_score)
                            tenth_frame = ['x', 'x', int(third_score)]
                            return tenth_frame, total
                        else:
                            print('Please enter a correct score.')
                    elif third_score == 'x':
                        tenth_frame = ['x', 'x', 'x']
                        return tenth_frame, 30
                    else:
                        print('Please enter a correct score.')
            else:
                print('Please enter a correct score.')


def main():
    game = []
    name = intro()
    frame = 1
    tenth_total = 0
    while frame < 10:
        print(f'\nFrame {frame}')
        first_score = get_first_score(name, frame)
        second_score = get_second_score(first_score, frame)
        game.append([first_score, second_score])
        frame += 1
    while frame == 10:
        print(f'Frame {frame}')
        tenth_frame, total = play_tenth(name, frame)
        game.append(tenth_frame)
        tenth_total += total
        frame += 1

    show_score(game, name)
    print(f'Total Score: {(core.find_total(game) + tenth_total)}')


if __name__ == '__main__':
    main()
