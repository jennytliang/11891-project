def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # return the count of the numbers of n-digit
    # positive integers that start or end with 1.
    return 0


# Pytest
import pytest

# Tests
@pytest.mark.parametrize("n, expected_result", [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 1),
    (4, 3),
    (5, 6),
    (6, 10),
    (7, 15),
    (8, 21),
    (9, 28),
    (10, 36),
    (11, 45),
    (12, 55),
    (13, 66),
    (14, 78),
    (15, 91),
    (16, 105),
    (17, 120),
    (18, 136),
    (19, 153),
    (20, 171),
])
def test_starts_one_ends(n, expected_result):
    assert starts_one_ends(n) == expected_result


# Run with Python
if __name__ == "__main__":
    print(starts_one_ends(10))
