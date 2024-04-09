def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = [" ", " m "]
	"""
    m = ["I", "V", "X", "L", "C", "D", "M"]
    i = 0
    ans = ""
    while number > 0:
        if number % 10 == 9:
            ans += m[i] + m[i + 1]
        elif number % 10 == 4:
            ans += m[i] + m[i + 2]
        elif number % 10 >= 5:
            ans += m[i + 1] + (m[i] * (number % 5))
        else:
            ans += m[i] * (number % 10)
        i += 2
        number //= 10
    return ans.lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod()