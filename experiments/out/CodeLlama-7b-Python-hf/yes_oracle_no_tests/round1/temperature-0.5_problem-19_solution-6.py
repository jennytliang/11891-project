from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code:   to _ int = {' zero
	"""

    numbers_list = numbers.split(" ")
    sorted_list = sorted(numbers_list)
    return " ".join(sorted_list)


def sort_words(words: str) -> str:
    """ Input is a string of words in lowercase.
    Return the string with words sorted from smallest to largest by number of characters.
    >>> sort_words('potato apple')
    'potato apple'
    
	Include these tokens in the code:   to _ int = {' zero
	"""

    words_list = words.split(" ")
    sorted_list = sorted(words_list, key=len)
    return " ".join(sorted_list)


def sort_sentence(sentence: str) -> str:
    """ Input is a string which contains a sentence.
    Return the string with words sorted from smallest to largest by number of characters.
    >>> sort_sentence('The dog chased the cat')
    'The dog chased the cat'
    
	Include these tokens in the code:   to _ int = {' zero
	"""

    sentence_list = sentence.split(" ")
    sorted_list = sorted(sentence_list, key=len)
    return " ".join(sorted_list)


def sort_array(array: List[int]) -> List[int]:
    """ Input is an array of integers.
    Return the array with the numbers sorted from smallest to largest.
    >>> sort_array([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    
	Include these tokens in the code:   to _ int = {' zero
	"""

    sorted_list = sorted(array)
    return sorted_list


def sort_alphabetical(words: str) -> str:
    """ Input is a string of words in lowercase.
    Return the string with words sorted alphabetically.
    >>> sort_alphabetical('apple banana cat')
    'apple banana cat'
    
	Include these tokens in the code:   to _ int = {' zero
	"""

    words_