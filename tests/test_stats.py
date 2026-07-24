from mathkit import mean, median, variance


def test_mean():
    assert mean([2, 4, 6]) == 4


def test_mean_empty():
    assert mean([]) == 0.0


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_variance():
    assert round(variance([2, 4, 6]), 4) == 4.0
