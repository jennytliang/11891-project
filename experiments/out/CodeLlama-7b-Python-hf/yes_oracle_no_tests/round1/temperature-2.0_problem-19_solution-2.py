from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    num_list = numbers.split()
    num_list.sort(key=str.lower)
    return ' '.join(num_list)


def check_pangram(sentence: str) -> bool:
    """ Check if the given sentence is a pangram.
    A pangram is a sentence containing every letter of the alphabet at least once.
    Return True if sentence is pangram, False otherwise.
    >>> check_pangram('The quick brown fox jumps over the lazy dog.')
    True
    >>> check_pangram('The quick brown fox jumps over the lazy fox.')
    False
    
	Include these tokens in the code: to _ string = 'abcdefghijklmnopqrstuvwxyz'
    """
    char_list = list(sentence.lower())
    char_list.sort()
    return char_list == list(string)


def find_vowels(sentence: str) -> List[str]:
    """ Return a list of vowels found in the given sentence.
    Vowels are 'a', 'e', 'i', 'o', 'u'.
    The returned list should be sorted in alphabetical order.
    >>> find_vowels('The quick brown fox jumps over the lazy dog.')
    ['a', 'e', 'e', 'i', 'o', 'u']
    """
    vowels = 'aeiou'
    sentence = sentence.lower()
    vowels_list = list(filter(lambda x: x in vowels, sentence))
    vowels_list.sort()
    return vowels_list


def find_at_position(sentence: str, position: int) -> str:
    """ Return the character in sentence at position.
    Return '' if position is not valid.
    >>> find_at_position('The quick brown fox jumps over the lazy dog.', 0)
    'T'
    >>> find_at_position('The quick brown fox jumps over the lazy dog.', 6)
    'q'
    >>> find_at_