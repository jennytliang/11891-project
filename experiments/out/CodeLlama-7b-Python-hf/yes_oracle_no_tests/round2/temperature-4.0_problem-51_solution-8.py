def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    
	Include these tokens in the code: return " ". join ( list ( filter ( lambda
	Do not include these tokens in the code: v ow els = '
	"""
    # your code here
    return " ".join(list(filter(lambda x: x not in 'aeiou', text.lower().split())))


def remove_duplicates(text):
    """
    remove_duplicates is a function that takes string and returns string without duplicates.
    >>> remove_duplicates('')
    ''
    >>> remove_duplicates('abcdef')
    'abcdef'
    >>> remove_duplicates('abcdeef')
    'abcdeef'
    >>> remove_duplicates('aabbcdeef')
    'abcd'
    >>> remove_duplicates('aabbcdeefa')
    'abcda'
    >>> remove_duplicates('aabbcdeefaa')
    'abcda'
    >>> remove_duplicates('aabbcdeefaaa')
    'abcd'
    >>> remove_duplicates('aabbcdeefaaaabc')
    'abcda'
    """
    # your code here
    return ''.join(dict.fromkeys(text))


def remove_first_char(text):
    """
    remove_first_char is a function that takes string and returns string without the first character.
    >>> remove_first_char('a')
    ''
    >>> remove_first_char('abc')
    'bc'
    >>> remove_first_char('abcd')
    'bcd'
    >>> remove_first_char('abcde')
    'bcde'
    >>> remove_first_char('abcdef')
    'bcdef'
    """
    # your code here
    return text[1:]


def remove_last_char(text):
    """
    remove_last_char is a function that takes string and returns string without the last character.
    >>> remove_last_char('a')
    ''
    >>> remove_last_char('abc')
    'ab'
    >>> remove_last_char('abcd')
    'abc'
    >>> remove_last_char('abcde')
    'abcd'
    >>> remove_last_char('abcdef')
    'abcde'
