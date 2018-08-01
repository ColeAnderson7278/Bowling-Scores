def intro():
    name = input('Welcome to The Bowling Alley!\nWhat is your name? ')
    return name


def get_score():
    print('Please enter your scores:')
    score = 0
    while True:
        first_ball = input('\nFirst Ball: ')
        if first_ball == 10:
            return 10
        elif 0 <= first_ball < 10:
            score += int(first_ball)
        else:
            print('Please enter the correct score.')
    if score != 10:
        while True:
            second_ball = input('\nSecond Ball: ')
            if (scores + second_ball) > 10:
                print('Please enter the correct score.')
            elif 0 <= second_ball <= 10:
                score += int(second_ball)
            else:
                print('Please enter the correct score.')
    return score


def main():
    name = intro()
    score = get_score()


if __name__ == '__main__':
    main()
