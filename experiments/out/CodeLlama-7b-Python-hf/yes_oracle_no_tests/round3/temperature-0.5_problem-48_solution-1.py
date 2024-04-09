def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    
	Include these tokens in the code: [
	Do not include these tokens in the code: [: len ( text ) ][
	"""



    return text  == text[::-1]


# pytest
import pytest

@pytest.mark.parametrize("text, result", [
    ["", True],
    ["aba", True],
    ["aaaaa", True],
    ["zbcd", False],
])
def test_is_palindrome(text: str, result: bool):
    assert is_palindrome(text) == result


# doctest
def run_tests():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    run_tests()
