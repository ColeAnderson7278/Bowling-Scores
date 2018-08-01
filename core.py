def score_adding(rounds, scores, game):
    total = 0
    for x in game[rounds - 2]:
        if x == '/':
            (game[rounds - 2]) = (10 + scores[0])
        else:
            for score in scores:
                if str(score).isdigit() == True:
                    total += score
    return game, total
