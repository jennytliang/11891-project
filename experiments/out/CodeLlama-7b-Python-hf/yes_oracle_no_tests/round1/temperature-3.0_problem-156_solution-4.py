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
    int_to_roman = {
        1 : "i",
        5 : "v",
        10 : "x",
        50 : "l",
        100 : "c",
        500 : "d",
        1000 : "m"
    }

    if number <= 0:
        raise ValueError("Number must be positive")
    elif number > 1000:
        raise ValueError("Number must be less than 1000")
    else:
        result = ""
        for key, value in int_to_roman.items():
            while number >= key:
                result += value
                number -= key
        result = result.replace("mm", "m")
        result = result.replace("cc", "c")
        result = result.replace("dd", "d")
        result = result.replace("vv", "v")
        result = result.replace("ii", "i")
        return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
