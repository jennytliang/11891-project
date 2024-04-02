def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: s = str ( x )
	"""
    s = str(x)
    if shift < len(s):
        s_ = s[shift:]
        s_ += s[:shift]
        return ''.join(s_)
    else:
        shift -= len(s)
        s_ = s[shift:]
        s_ += s[:shift]
        return s_[::-1]
    
    
def circular_shift_2(x, shift):
    """ Circular shift a string x in to a new string. If shift > len ( x ), the string remains reversed.
    Hint: Convert a string to a list to split it into individual characters
    >>> circular_shift_2(28, 1)
    "82"
    >>> circular_shift_2(28, 2)
    "28"
    >>> circular_shift_2(111, 2)
    "000"
    """
    s = [c for c in str(x)]
    if shift <= len(s):
        s_ = s[shift:]
        s_ += s[:shift]
    else:
        shift -= len(s)
        s_ = s[shift:]
        s_ += s[:shift]
    return ''.join(s_)


def to_word(n):
    """Returns n as a word.
    n -- integer
    returns -- string """
    digits = {1: 'one',
             2: 'two',
             3: 'three',
             4: 'four',
             5: 'five',
             6: 'six',
             7: 'seven',
             8: 'eight',
             9: 'nine'
    }
    n = str(n)    # otherwise n - a string
    out_ = ""
    for letter in n:
        out_ += digits[int(letter)] + " "
    return out_


if __name__ == '__main__':
    to_word(123) == 'one two three'
    circular_shift(12, 1) == '21'
    circular_shift(12, 2) ==