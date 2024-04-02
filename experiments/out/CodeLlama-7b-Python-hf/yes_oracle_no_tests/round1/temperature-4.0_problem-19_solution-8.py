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
    for i in range(len(numbers_list)):
        numbers_list[i] = numbers_list[i].lower()
    print(numbers_list)
    for i in range(len(numbers_list)):
        if numbers_list[i] == 'zero':
            numbers_list[i] = 0
        elif numbers_list[i] == 'one':
            numbers_list[i] = 1
        elif numbers_list[i] == 'two':
            numbers_list[i] = 2
        elif numbers_list[i] == 'three':
            numbers_list[i] = 3
        elif numbers_list[i] == 'four':
            numbers_list[i] = 4
        elif numbers_list[i] == 'five':
            numbers_list[i] = 5
        elif numbers_list[i] == 'six':
            numbers_list[i] = 6
        elif numbers_list[i] == 'seven':
            numbers_list[i] = 7
        elif numbers_list[i] == 'eight':
            numbers_list[i] = 8
        elif numbers_list[i] == 'nine':
            numbers_list[i] = 9
    numbers_list.sort()
    return ' '.join(str(e) for e in numbers_list)


def sort_words(words: str) -> str:
    """ Input is a string of words separated by a single space.
    Return the string with the words sorted in alphabetical order
    >>> sort_words('cat dog year zoo')
    'cat dog year zoo'
    """
    words_list = words.split()
    words_list.sort()
    return ' '.join(str(e) for e in words_list)


def sort_sentence(sentence: str) -> str:
    """ Input is a string of words separated by a single space.
    Return the string with the words sorted in alphabetical order and the sentence in lowercase.
    >>> sort_sentence('This IS A SENTENCE')
