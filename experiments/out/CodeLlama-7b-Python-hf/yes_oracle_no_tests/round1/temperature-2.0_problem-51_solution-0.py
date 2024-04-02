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
        if i not in "aeiou":
            r += i
    return r


def remove_vowels_1(text):
    """
	remove_vowels_1 is a function that takes string and returns string without vowels.
    >>> remove_vowels_1('')
    ''
    >>> remove_vowels_1("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_1('abcdef')
    'bcdf'
    >>> remove_vowels_1('aaaaa')
    ''
    >>> remove_vowels_1('aaBAA')
    'B'
    >>> remove_vowels_1('zbcd')
    'zbcd'
	"""
    return text.translate(str.maketrans("", "", "aeiouAEIOU"))


def remove_vowels_2(text):
    """
    remove_vowels_2 is a function that takes string and returns string without vowels.
    >>> remove_vowels_2('')
    ''
    >>> remove_vowels_2("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_2('abcdef')
    'bcdf'
    >>> remove_vowels_2('aaaaa')
    ''
    >>> remove_vowels_2('aaBAA')
    'B'
    >>> remove_vowels_2('zbcd')
    'zbcd'
	"""
    return text.translate(str.maketrans("aeiou", "    "))


def remove_vowels_3(text):
    """
    remove_vowels_3 is a function that takes string and returns string without vowels.
    >>> remove_vowels_3('')
    ''
    >>> remove_vowels_3("abcdef\nghijklm")
    'bcdf\nghjkl