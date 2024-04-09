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
    roman_numerals = {
        1: ["i"],
        4: ["iv"],
        5: ["v"],
        9: ["ix"],
        10: ["x"],
        40: ["xl"],
        50: ["l"],
        90: ["xc"],
        100: ["c"],
        400: ["cd"],
        500: ["d"],
        900: ["cm"],
        1000: ["m"],
    }
    if number < 1 or number > 1000:
        raise ValueError(
            "number must be a positive integer and less than or equal to 1000"
        )
    if number == 0:
        return " "
    if number in roman_numerals:
        return roman_numerals[number][0]
    else:
        for i in range(1, 1001):
            if number < i * 10:
                return "".join(
                    [
                        roman_numerals[i][0],
                        int_to_mini_roman(number - (i * 10)),
                        roman_numerals[i][0],
                    ]
                )
            elif number % i == 0:
                return "".join(
                    [
                        roman_numerals[i][0],
                        int_to_mini_roman(number / i),
                        roman_numerals[i][0],
                    ]
                )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
