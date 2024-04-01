def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a,b = b,a
    even_digits_list = []
    for num in range(a, b+1):
        str_num = str(num)
        if str_num[0] == '0' or str_num[-1] == '0':
            continue
        even_digits = []
        for digit in str_num:
            if int(digit) % 2 == 0:
                even_digits.append(digit)
        even_digits_str = ''.join(even_digits)
        if int(even_digits_str) % 2 == 0:
            even_digits_list.append(num)
    return even_digits_list
    # pass