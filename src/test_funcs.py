# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from funcs import (
    prod,
    prod2,
    longest,
    dist
)


def test_prod():
    assert prod(1, 2, 3) == 6


def test_prod2():
    assert prod2(2) == 8


def test_longest():
    assert longest([1, 2, 3], [4, 5]) == [1, 2, 3]
    assert longest([4, 5], [1, 2, 3]) == [1, 2, 3]
    assert longest([4, 5, 6], [1, 2, 3]) == "Two lists are of the same length"


def test_dist():
    assert dist((0, 0), (5, 12)) == 13
    assert dist((0, 0), (3, 4)) == 5
