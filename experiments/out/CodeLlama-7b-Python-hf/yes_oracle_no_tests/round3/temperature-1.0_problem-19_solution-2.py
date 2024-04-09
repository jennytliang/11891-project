from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    numbers_list = numbers.split()
    numbers_list.sort()
    return " ".join(numbers_list)


def sort_words(sentence: str) -> str:
    """ Input is a string of words.
    Return the string with the words sorted from shortest to longest.
    If two words are the same length, sort these words alphabetically.
    >>> sort_words('quick brown fox jumped over lazy dog')
    'brown dog fox jumped lazy over quick'
    
	Include these tokens in the code: to _ word = 
	"""
    words_list = sentence.split()
    words_list.sort(key=len)
    return " ".join(words_list)


def sort_sentence(sentence: str) -> str:
    """ Input is a string containing a single sentence.
    Return the string with the words sorted in order of appearance.
    If two words appear the same number of times, sort these words alphabetically.
    If two words have the same length and appear the same number of times, sort these words alphabetically.
    >>> sort_sentence('red blue red green blue green blue red')
    'blue blue green green red red red red'
    
	Include these tokens in the code: to _ word = 
	"""
    words_list = sentence.split()
    words_list.sort(key=lambda x: (len(x), x))
    return " ".join(words_list)


def sort_array(array: List[int]) -> List[int]:
    """ Input is an array of integers.
    Return the array with the numbers sorted from smallest to largest.
    If two numbers are equal, their relative positions should not be changed.
    >>> sort_array([4, 2, 1, 7, 3, 5])
    [1, 2, 3, 4, 5, 7]
    
	Include these tokens in the code: to _ num = 
	"""
    array.sort()
    return array


if __name__ == "__main__":
    import doctest
    doctest