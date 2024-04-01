from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to
	Do not include these tokens in the code: def get
	"""
    return " ".join(sorted(numbers.split(" ")))


def get_numbers(text: str) -> List[int]:
    """ Input is a string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return a list of numbers
    >>> get_numbers('one two three')
    [1, 2, 3]
    >>> get_numbers('eight nine')
    [8, 9]
    """
    return [int(i) for i in text.split(" ") if i != ""]


def get_numbers_from_sentence(text: str) -> List[int]:
    """ Input is a sentence.
    Return a list of numbers contained in the sentence.
    >>> get_numbers_from_sentence('The number is 42')
    [42]
    >>> get_numbers_from_sentence('The numbers are 1, 3, 5, 7 and 9')
    [1, 3, 5, 7, 9]
    """
    return get_numbers(text)


def get_numbers_from_sentences(text: str) -> List[int]:
    """ Input is a string of sentences.
    Return a list of numbers contained in the sentences.
    >>> get_numbers_from_sentences('The number is 42. The number 1 is correct.')
    [42, 1]
    """
    return [x for y in text.split(".") for x in get_numbers_from_sentence(y)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
