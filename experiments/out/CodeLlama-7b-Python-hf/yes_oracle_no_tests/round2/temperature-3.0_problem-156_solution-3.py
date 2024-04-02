def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Do not include these tokens in the code: ", " m " ] d = ["
	"""

    m_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman = ""
    for i in range(len(str(number))):
        if number % 10 != 9:
            roman += str(m_roman[str(number)[i]]) * (number % 10)
        else:
            roman += str(m_roman[str(number)[i - 1]]) + str(m_roman[str(number)[i]])
        number //= 10
    return roman


def main():
    print(int_to_mini_roman(19))
    print(int_to_mini_roman(152))
    print(int_to_mini_roman(426))


if __name__ == "__main__":
    main()
