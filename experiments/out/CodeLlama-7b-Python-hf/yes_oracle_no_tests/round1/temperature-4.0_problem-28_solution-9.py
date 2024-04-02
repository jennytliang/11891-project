from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if strings == [] :
	"""
    return ''.join(strings)


def count_letters(string: str) -> int:
    """ Count the letters in a string
    >>> count_letters('')
    0
    >>> count_letters('abcdefg')
    7
    >>> count_letters('hello world')
    11
    
	Do not include these tokens in the code: if string == '': return 0
    """
    return len(string)


def count_words(string: str) -> int:
    """ Count the words in a string
    >>> count_words('')
    0
    >>> count_words('a b c')
    3
    >>> count_words('a  b')
    2
    >>> count_words('a  b  ')
    2
    >>> count_words('a')
    1
    
	Do not include these tokens in the code: if string == '': return 0
    """
    return len(string.split())


def count_symbols(string: str) -> int:
    """ Count the symbols in a string
    >>> count_symbols('')
    0
    >>> count_symbols('abcdefg')
    0
    >>> count_symbols('a b c')
    0
    >>> count_symbols('a  b')
    0
    >>> count_symbols('a  b  ')
    0
    >>> count_symbols('a')
    0
    >>> count_symbols('a1b')
    1
    >>> count_symbols('a!b')
    1
    >>> count_symbols('a.b')
    1
    >>> count_symbols('a,b')
    1
    >>> count_symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    26
    
	Do not include these tokens in the code: if string == '': return 0
    """
    return len([s for s in string if not s.isalpha()])


def count_digits(string: str) -> int:
    """