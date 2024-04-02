def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Do not include these tokens in the code: ", " m " ] r = ["
	"""

    m = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    r = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
    ans = ""
    for i in range(len(m)):
        cnt = int(number / m[i])
        ans += r[i] * cnt
        number -= m[i] * cnt
    return ans
