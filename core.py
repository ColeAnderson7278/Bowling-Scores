def find_total(game):
    total = 0
    for count, frame in enumerate(game):
        if count == 9:
            if 'x' in frame:
                total += 0
            elif '/' in frame:
                total += 0
            else:
                total += 0
        elif count == 8:
            if 'x' in frame:
                if 'x' == game[count + 1][0] and 'x' == game[count + 1][1]:
                    total += 30
                elif 'x' == game[count + 1][0]:
                    total += (20 + (game[count + 1][1]))
                elif '/' == game[count + 1][1]:
                    total += 20
                else:
                    total += (game[count + 1][0] + game[count + 1][1])
            elif '/' in frame:
                if 'x' in game[count + 1]:
                    total += 20
                else:
                    special = game[count + 1]
                    total += (10 + special[0])
            else:
                total += sum(frame)
        elif 'x' in frame:
            if 'x' in game[count + 1] and 'x' in game[count + 2]:
                total += 30
            elif 'x' in game[count + 1]:
                total += (20 + (game[count + 2][0]))
            elif '/' in game[count + 1]:
                total += 20
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
                total += (special[0] + 10)
        else:
            total += sum(frame)
    return total
