from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	"""
    return " ".join(strings)


def is_palindrome(string: str) -> bool:
    """ Check if a string is a palindrome
    
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    
	Include these tokens in the code: return string == string [:: -1]
	"""
    return string == string[::-1]


def count_letters(string: str) -> int:
    """ Count the number of letters in a string
    
    >>> count_letters("hello")
    4
    >>> count_letters("a")
    1
    
	Include these tokens in the code: return len ( string )
	"""
    return len(string)


def count_words(string: str) -> int:
    """ Count the number of words in a string
    
    >>> count_words("hello there")
    2
    >>> count_words("one two three four five")
    5
    
	Include these tokens in the code: return len ( string . split ( ) )
	"""
    return len(string.split())


def count_sentences(string: str) -> int:
    """ Count the number of sentences in a string
    
    >>> count_sentences("This is a sentence. This is another sentence.")
    2
    >>> count_sentences("This is a sentence. This is another sentence. This is yet another sentence.")
    3
    
	Include these tokens in the code: return string . count ( "." )
	"""
    return string.count(".")


def count_vowels(string: str) -> int:
    """ Count the number of vowels in a string
    
    >>> count_vowels("hello")
    2
    >>> count_vowels("a")
    1
    
	Include these tokens in the code: return sum ( 1 for letter in string if letter in "aeiou" )
	"""
    return sum(1 for letter in string if letter in "aeiou")


def count_