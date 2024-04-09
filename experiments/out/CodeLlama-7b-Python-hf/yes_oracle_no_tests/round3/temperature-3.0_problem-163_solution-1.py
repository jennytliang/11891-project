def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: if a > b : a , b = b
	"""
    # pass
    if a > b:
        a, b = b, a
    return [i for i in range(a, b+1, 2) if i % 2 == 0]










# tests
import pytest

from generate_integers import generate_integers

def test_generate_integers():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []

def test_generate_integers_negatives():
    assert generate_integers(-2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, -2) == [2, 4, 6, 8]
    assert generate_integers(10, -14) == []

def test_generate_integers_negatives_and_positives():
    assert generate_integers(-2, -8) == [-2, -4, -6, -8]
    assert generate_integers(-8, -2) == [-2, -4, -6, -8]
    assert generate_integers(-10, -14) == []

def test_generate_integers_negatives_and_positives_2():
    assert generate_integers(-2, 8) == [-2, -4, -6, -8, 2, 4, 6, 8]
    assert generate_integers(8, -2) == [-2, -4, -6, -8, 2, 4, 6, 8]
    assert generate_integers(-10, 14) == [2, 4, 6, 8, 10, 12, 14]

def test_generate_integers_negatives_and_positives_3():
    assert generate_integers(-2, 8) == [-2,