from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    
	Include these tokens in the code: , p
	"""

    pass


def count_words(sentence: str) -> Tuple[int, int, int]:
    """ For a given sentence, return a tuple consisting of the number of words, the number of spaces and the number of
    uppercase letters. Empty sentence should return (0, 0, 0).
    >>> count_words("")
    (0, 0, 0)
    >>> count_words("a b c d e")
    (5, 4, 0)
    >>> count_words("A b c d e")
    (5, 4, 3)
    >>> count_words("a b c d e A B C D E")
    (10, 8, 6)
    
	Include these tokens in the code: , len, len, .upper, ' '
    """

    pass


def reverse_words(sentence: str) -> str:
    """ For a given sentence, return a string where all words are reversed. Do not use built-in methods.
    >>> reverse_words("")
    ''
    >>> reverse_words("a b c d e")
    'e d c b a'
    >>> reverse_words("A b c d e")
    'e d c b A'
    >>> reverse_words("a b c d e A B C D E")
    'E D C B A e d c b a'
    """

    pass


def sort_letters(sentence: str) -> str:
    """ For a given sentence, sort all letters in ascending order and return a string where all words are joined with
    underscore.
    >>> sort_letters("")
    ''
    >>> sort_letters("a b c d e")
    'a_b_c_d_e'
    >>> sort_letters("A b c d e")
    'A_b_c_d_e'
    >>> sort_letters("a b c d e A B C D E")
    'A_B_C_D_E_a_b_c_d_e'
    """

    pass


def is_