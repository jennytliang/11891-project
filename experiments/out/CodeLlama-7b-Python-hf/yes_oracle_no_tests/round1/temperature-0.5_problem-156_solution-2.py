def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code:  m = [" ", "
	Do not include these tokens in the code: roman _ numer als { 1
	"""

    roman = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    def roman_num(num):
        for r in roman:
            div = roman[r]
            if num // div * div == num:
                return num // div * r

    def mini_roman(num):
        while num > 0:
            for r in roman:
                div = roman[r]
                if num // div * div == num:
                    yield r
                    num -= div

    return "".join(mini_roman(number)).lower()


def test_function():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(1254) == 'mccliiv'
    assert int_to_mini_roman(349) == 'cccxlxix'


if __name__ == "__main__":
    test_function()
