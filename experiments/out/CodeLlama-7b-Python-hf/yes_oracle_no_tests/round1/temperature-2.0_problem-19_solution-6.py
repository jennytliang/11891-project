from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""

    int = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
           'eight': '8', 'nine': '9'}

    nums = numbers.split()
    nums = [int[i] for i in nums]
    nums = [int(i) for i in nums]

    nums.sort()
    nums = [str(i) for i in nums]
    nums = [int[i] for i in nums]
    return ' '.join(nums)


def sort_sentence(sentence: str) -> str:
    """ Input is a sentence of words.
    Return the sentence where words are sorted alphabetically.
    If two or more words are the same, sort them alphabetically.
    >>> sort_sentence('bright arrows live on the dark arcade')
    'arcade dark live on the bright arrows'
    """

    words = sentence.split()
    words = sorted(words)
    return ' '.join(words)


def sort_case_insensitive(sentence: str) -> str:
    """ Input is a sentence of words.
    Return the sentence where words are sorted alphabetically,
    case-insensitively.
    If two or more words are the same, sort them alphabetically.
    >>> sort_case_insensitive('pOTATOES and PEas')
    'Potatoes and peas'
    """

    words = sentence.split()
    words = sorted(words, key=str.casefold)
    return ' '.join(words)


def sort_vowels(sentence: str) -> str:
    """ Input is a sentence of words.
    Return the sentence where words are sorted,
    putting words containing vowels before words without vowels.
    Words with capital letters come first.
    >>> sort_vowels('plums are fall favorite')
    'Plums are fall favorite'
   