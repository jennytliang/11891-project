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
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ""
    for i in text:
        if i.lower() not in "aeiou":
            r += i
    return r

def remove_punctuation(text):
    """
    remove_punctuation is a function that takes string and returns string without punctuation.
    >>> remove_punctuation('')
    ''
    >>> remove_punctuation("abcdef\nghijklm")
    'abcdef ghijklm'
    >>> remove_punctuation('abcdef')
    'abcdef'
    >>> remove_punctuation('aaaaa')
    'aaaaa'
    >>> remove_punctuation('aaBAA')
    'aaBAA'
    >>> remove_punctuation('zbcd')
    'zbcd'
    >>> remove_punctuation('aaa!aaa')
    'aaa aa a'
    >>> remove_punctuation('aaa!aaa!!')
    'aaa aa a a'
    >>> remove_punctuation('aaa!aaa!!!!')
    'aaa aa a a a'
    >>> remove_punctuation('aaa!aaa!aaa')
    'aaa aa a a a'
    >>> remove_punctuation('aaa!aaa!aaa!!')
    'aaa aa a a a a'
    """

    r = ""
    for i in text:
        if i.isalnum():
            r += i
    return r

def double_spaces(text):
    """
    double_spaces is a function that takes string and returns string without double spaces.
    >>> double_spaces('')
    ''
    >>> double_spaces('abcdef\nghijklm')
    'abcdef ghijklm'
    >>> double_spaces('abcdef')
    'abcdef'
    >>> double_spaces('aaa!aaa')
    'aaa!aaa'
    >>> double_spaces('aaa!aaa!!')
    'aaa!aaa!!'
    >>> double_spaces('