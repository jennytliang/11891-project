from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in string]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in string]


def all_infixes(string: str) -> List[str]:
    """ Return list of all infixes from shortest to longest of the input string
    >>> all_infixes('abc')
    ['b', 'bc', 'b', 'c', 'c']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in string]


def all_words(string: str) -> List[str]:
    """ Return list of all words from the input string
    >>> all_words('abc')
    ['abc']
    >>> all_words('ab c')
    ['ab', 'c']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in string.split()]


def all_words_with_punctuation(string: str) -> List[str]:
    """ Return list of all words from the input string, including punctuation
    >>> all_words_with_punctuation('ab, c')
    ['ab', ',', 'c']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in string]


def all_sentences(string: str) -> List[str]:
    """ Return list of all sentences from the input string, including punctuation
    >>> all_sentences('ab, c.')
    ['ab, c.']
    
	Include these tokens in the code: [ :(
	Do not include these