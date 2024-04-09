from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Do not include these tokens in the code: if not strings :
	"""
    return max(strings, key=len) if strings else None


def is_palindrome(string: str) -> bool:
    """ Return True if string is a palindrome, False otherwise.
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('ab')
    False
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abccba')
    True
    >>> is_palindrome('abbcbba')
    True
    >>> is_palindrome('abbcbb')
    False
    """
    return string == string[::-1]


def is_valid_move(board: List[List[str]], row: int, col: int, symbol: str) -> bool:
    """ Return True if the player can place the symbol in (row, col) on the board. Otherwise, return
    False.
    >>> board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    >>> is_valid_move(board, 0, 0, 'X')
    True
    >>> is_valid_move(board, 0, 0, 'O')
    False
    >>> is_valid_move(board, 0, 1, 'X')
    True
    >>> is_valid_move(board, 0, 1, 'O')
    False
    >>> is_valid_move(board, 0, 2, 'X')
    True
    >>> is_valid_move(board, 0, 2, 'O')
    False
    >>> is_valid_move(board, 1, 0, 'X')
    True
    >>> is_valid_move(board, 1, 0, 'O')
    False
    >>> is_valid_move(board, 1, 1, '