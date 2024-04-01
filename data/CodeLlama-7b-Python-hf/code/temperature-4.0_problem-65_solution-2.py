def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    shift %= len(str(x))
    shifted_numbers = []  # A list of characters
    string_x = str(x)  # convert int x to a string
    x_length = len(string_x)  # calculate the length of that string
    for i in range(0, x_length):
        # i < shift:   append the ith-digit
        # of the initial string to the shifteed digits
        if (i % shift == 0 and i < shift):
            shifted_digits.append(character)
