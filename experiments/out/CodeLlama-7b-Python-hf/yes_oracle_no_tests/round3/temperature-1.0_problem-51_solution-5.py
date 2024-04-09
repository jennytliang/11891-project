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
    
	Do not include these tokens in the code: v ow els = " ae i
	"""
    result = ''
    for i in text:
        if i not in 'aeiou':
            result += i
    return result


def main():
    """
    main function
    """
    print(remove_vowels(''))
    print(remove_vowels("abcdef\nghijklm"))
    print(remove_vowels('abcdef'))
    print(remove_vowels('aaaaa'))
    print(remove_vowels('aaBAA'))
    print(remove_vowels('zbcd'))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
