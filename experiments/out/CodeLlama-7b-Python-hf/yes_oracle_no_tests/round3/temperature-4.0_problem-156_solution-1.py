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

    num_to_roman = {0: "", 1: "i", 2: "ii", 3: "iii", 4: "iv", 5: "v", 6: "vi", 7: "vii", 8: "viii", 9: "ix"}
    num_to_roman_dict = {10: "x", 100: "c", 1000: "m"}

    roman = ""
    if number < 10:
        return num_to_roman[number]

    if number < 100:
        if number % 10 == 0:
            return num_to_roman[number]
        else:
            return num_to_roman[int(number / 10)] + num_to_roman[number % 10]

    if number < 1000:
        if number % 100 == 0:
            return num_to_roman[int(number / 100)] + num_to_roman_dict[100]
        else:
            return num_to_roman[int(number / 100)] + num_to_roman_dict[100] + num_to_roman[number % 100]

    if number < 10000:
        if number % 1000 == 0:
            return num_to_roman[int(number / 1000)] + num_to_roman_dict[1000]
        else:
            return num_to_roman[int(number / 1000)] + num_to_roman_dict[1000] + int_to_mini_roman(number % 1000)


def main():
    print(int_to_mini_roman(19))


if __name__ == "__main__":
    main()
