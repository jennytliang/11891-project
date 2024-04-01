def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num = str(x)
    num_length = len(num)
    shift_remainder = shift % num_length
    new_num_list = list(num)
    new_num_list = new_num_list[num_length-shift_remainder:] + new_num_list[:num_length-shift_remainder]
    new_num = "".join(new_num_list)
    return new_num


