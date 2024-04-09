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
    m = [" I", " V", " X", " L", " C", " D", " M"]
    d = [1000, 500, 100, 50, 10, 5, 1]
    ans = ""
    for i in range(len(d)):
        while number >= d[i]:
            ans += m[i]
            number -= d[i]
    return ans


print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))
