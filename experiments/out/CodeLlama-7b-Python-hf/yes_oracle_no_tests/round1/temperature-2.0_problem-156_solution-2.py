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

    m = [" ", " m "]
    d = ["", " d ", " cd ", " ccc ", " dcc ", " dccc ", " cm"]
    c = ["", " c ", " cc ", " ccc ", " dcc ", " dccc ", " cm"]
    x = ["", " x ", " xx ", " xxx ", " l ", " lx ", " lxx ", " cl"]
    v = ["", " v ", " vv ", " vvv ", " d ", " dc ", " dcc ", " cm"]
    u = ["", " u ", " uu ", " uuu ", " v ", " vv ", " vvv ", " m"]
    t = ["", " t ", " tt ", " ttt ", " d ", " dd ", " ddd ", " cm"]
    s = ["", " s ", " ss ", " sss ", " t ", " tt ", " ttt ", " m"]

    result = ""

    result += d[number // 1000]
    number %= 1000

    result += c[number // 100]
    number %= 100

    result += x[number // 10]
    number %= 10

    result += v[number // 5]
    number %= 5

    result += u[number]

    return result.lower()


print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))
