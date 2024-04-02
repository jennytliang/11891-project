from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    return " ".join(sorted(numbers.split()))


def sort_characters(chars: str) -> str:
    """ Input is a string of letters in upper or lower case.
    Return the string with letters sorted from a to z or A to Z.
    >>> sort_characters('Ee Dd Cc Bb Aa')
    'Aa Bb Cc Dd Ee'
    """
    return "".join(sorted(chars))


def sort_sentence(sentence: str) -> str:
    """ Input is a sentence containing numbers, characters and words.
    Return the sentence with the words sorted from smallest to largest.
    >>> sort_sentence('is2 Thi1s T4est 3a')
    'Thi1s is2 3a T4est'
    """
    return " ".join(sorted(sentence.split(), key=lambda x: x.lower()))


def sort_words(words: str) -> str:
    """ Input is a string of words separated by spaces.
    Return the string with the words sorted from smallest to largest using
    the length of each word.
    Ignore upper or lower case.
    Consider all punctuation marks to be part of a word.
    """
    return " ".join(sorted(words.split(), key=lambda x: len(x.lower())))


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(sort_words("is2 Thi1s T4est 3a"))
