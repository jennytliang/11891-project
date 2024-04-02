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
    mini_roman = list("cdlmivx")
    for _ in range(number):
    # Start with roman digits for a hundred, 1000, ..., then 
    # the lower 9 of those; then 90, ..., then 9, then 10.
        m.append(m[-1] + m[-2])
        m.insert(1, m[-1])
        if not len(m) % 9:
            m.append(m[-1])
    for i in range(len(m)):
        # Divide the roman digits so that at the ith digit, 
        # it is 4 times more than its predecessor.
            m.insert(i, (((len(m) / 7) - i) * 3) * m[i-1])
    return ''.join(m).strip()