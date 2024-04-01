def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Do not include these tokens in the code: = [" I ", " IV ", " V ",
	"""

    # Convert the number to a string
    num_str = str(number)

    # Convert the string to a list of characters
    num_list = [char for char in num_str]

    # Initialize the roman numeral string
    rom_str = ''

    # Loop through the characters of the list
    for char in num_list:
        if char == '1':
            rom_str += 'i'
        elif char == '2':
            rom_str += 'i'
            rom_str += 'i'
        elif char == '3':
            rom_str += 'i'
            rom_str += 'i'
            rom_str += 'i'
        elif char == '4':
            rom_str += 'i'
            rom_str += 'v'
        elif char == '5':
            rom_str += 'v'
        elif char == '6':
            rom_str += 'v'
            rom_str += 'i'
        elif char == '7':
            rom_str += 'v'
            rom_str += 'i'
            rom_str += 'i'
        elif char == '8':
            rom_str += 'v'
            rom_str += 'i'
            rom_str += 'i'
            rom_str += 'i'
        elif char == '9':
            rom_str += 'x'
        elif char == '0':
            rom_str += 'x'
            rom_str += 'i'

    # Return the lowercase roman numeral string
    return rom_str.lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
