from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    numbers.sort()
    return " ".join(str(i) for i in numbers)


def count_words(sentence: str) -> str:
    """ Input is a string of words separated by spaces.
    Return the string with each word followed by the number of times it appears in the sentence
    >>> count_words('hello world')
    'hello 1 world 1'
    """
    words = sentence.split()
    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return " ".join(str(i) + " " + str(j) for i, j in d.items())


def sort_sentence(sentence: str) -> str:
    """ Input is a string of words separated by spaces.
    Return the string with the words sorted in alphabetical order
    >>> sort_sentence('world hello')
    'hello world'
    """
    words = sentence.split()
    words.sort()
    return " ".join(str(i) for i in words)


def sort_sentence_case_insensitive(sentence: str) -> str:
    """ Input is a string of words separated by spaces.
    Return the string with the words sorted in alphabetical order, case insensitive
    >>> sort_sentence_case_insensitive('Hello world')
    'Hello world'
    """
    words = sentence.split()
    words.sort(key=str.lower)
    return " ".join(str(i) for i in words)


def count_characters(sentence: str) -> str:
    """ Input is a string of words separated by spaces.
    Return the string with each word followed by the number of characters in the word
    >>> count_characters('hello world')
    'hello 5 world 5'
    """
    words = sentence.split()
    d = {}
    for word in words:
        if word not in d: