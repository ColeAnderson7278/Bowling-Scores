import core


def test_score_adding():
    core.score_adding(2, [5, 2], [[3, '/'], [5, 3]]) == [15], 7
    core.score_adding(5, [0, '/'],
                      [['x', 0], ['x', 0], [1, 1], [0, '/']]) == [10], '/'
