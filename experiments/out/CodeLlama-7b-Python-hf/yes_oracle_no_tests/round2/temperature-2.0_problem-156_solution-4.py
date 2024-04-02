def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: ",
	"""

    m_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_roman = {'I': 'i', 'V': 'v', 'X': 'x', 'L': 'l', 'C': 'c', 'D': 'd', 'M': 'm'}

    string = ''
    for char in r_roman:
        string += char
    string = list(string)
    string.sort(reverse=True)
    string = ''.join(string)

    #print(string)

    for char in string:
        if m_roman[char] < number:
            number -= m_roman[char]
            string = string.replace(char, r_roman[char])
        elif m_roman[char] > number:
            string = string.replace(char, r_roman[char])
            break
        else:
            string = string.replace(char, r_roman[char])
            break

    return string



if __name__ == '__main__':
    import doctest
    doctest.testmod()
