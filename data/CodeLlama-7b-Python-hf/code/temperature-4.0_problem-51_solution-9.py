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
    """
    #vowels = ['a','e','i','o','u','y']
    return re.sub( '[aeiou]', '', text )


# 2.10382 s 522 ms
def removeVowels(text):
    """
    >>> test = 'bccdefzzfghhijjjkklljmmnnopppqrsqsspqrsppqosstttuuuuvv'
    >>> test = 'bccdecdef'
    >>> t0 = time.clock()
    >>> for n in xrange(10000):
    ...    removeVowels(test)                 # 1
    ... print '%40s took (%.1f us).  Next operation starts %.0f us later' % (
    ...    '20', 1000*(t1-t0), 8.0*t0 - 10)
                <module>                             took (13.3 us).  Next
      <module> took (42144.1 us)