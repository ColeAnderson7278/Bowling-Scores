import core


def test_score_adding():
    core.score_adding(3, 7, [10, 9]) == 17
    core.score_adding(1, 9, [10, 10, 10]) == 9
    core.score_adding(10, 2, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 11
    core.score_adding(1, 0, []) == 0
