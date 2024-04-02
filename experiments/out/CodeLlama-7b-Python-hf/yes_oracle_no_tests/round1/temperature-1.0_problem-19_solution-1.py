from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    
    words = numbers.split(' ')
    word_values = {
        ' zero ' : '0',
        ' one ' : '1',
        ' two ' : '2',
        ' three ' : '3',
        ' four ' : '4',
        ' five ' : '5',
        ' six ' : '6',
        ' seven ' : '7',
        ' eight ' : '8',
        ' nine ' : '9'
    }
    num_list = list(map(lambda x: word_values[x], words))
    num_list = map(int, num_list)
    return ' '.join(str(x) for x in sorted(num_list))
    # return ' '.join([word_values[x] for x in sort_text(words)])


import re

def sort_words(text: str):
    """ Input is text
    If the text has more than 1 word, return the words sorted in alphabetic order
    For example, transforming "defghi" to "ddefhi"
    """
    words = text.split(" ")
    if len(words) <= 1:
        return text
    # words = re.split(' ', text)
    sorted_words = sorted(list(words))
    return " ".join(sorted_words)


def _parse_text(text: str) -> List[str]:
    """ Convert text to lowercase and remove all punctuation """
    pattern = re.compile(r'[a-zA-Z\'-]')
    return pattern.findall(text.lower())

def _index_of_first_diff(tokens1: List[str], tokens2: List[str]) -> int:
    """ For the tokens1 and tokens2, return the index of the token that does not match with tokens2"""
    for i in range(len(tokens1)):
        if i<len(tokens2) and tokens1[i] != tokens2[i]:
            return i

    return len(tokens1)    


def anagrams(s1, s2) ->