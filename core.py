def score_adding(rounds, score, game):
    if rounds == 1:
        return score
    else:
        rounds = int(rounds) - 2
        return (game[rounds]) + score
