import core


def intro():
    name = input('Welcome to The Bowling Alley!\nWhat is your name? ')
    return name


def get_score():
    print('Please enter your scores:')
    score = 0
    while True:
        first_ball = input('\nFirst Ball: ')
        if int(first_ball) == 10:
            return 10
        elif 0 <= int(first_ball) < 10:
            score += int(first_ball)
            while True:
                second_ball = input('\nSecond Ball: ')
                if (score + int(second_ball)) > 10:
                    print('\nPlease enter the correct score.')
                elif 0 <= int(second_ball) <= 10:
                    score += int(second_ball)
                    return score
                else:
                    print('Please enter the correct score.')
        else:
            print('\nPlease enter the correct score.')
    return score


def show_score(game):
    print(game)


def main():
    game = []
    name = intro()
    rounds = 1
    while rounds <= 10:
        score = get_score()
        game.append(core.score_adding(rounds, score, game))
        show_score(game)
        rounds += 1


if __name__ == '__main__':
    main()
