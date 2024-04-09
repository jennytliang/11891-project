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
    # your code here
    m = [" ", " m "]
    a = []
    for i in str(number):
        a.append(int(i))
    a.reverse()
    b = []
    for i in range(len(a)):
        if a[i] == 1:
            b.append('i')
        elif a[i] == 2:
            b.append('ii')
        elif a[i] == 3:
            b.append('iii')
        elif a[i] == 4:
            b.append('iv')
        elif a[i] == 5:
            b.append('v')
        elif a[i] == 6:
            b.append('vi')
        elif a[i] == 7:
            b.append('vii')
        elif a[i] == 8:
            b.append('viii')
        elif a[i] == 9:
            b.append('ix')
        else:
            b.append('x')
    b.reverse()
    for i in range(len(b)):
        if i == 0:
            if b[i] == 'x':
                b[i] = 'x'
            else:
                b[i] = m[0] + b[i]
        else:
            if b[i] == 'x':
                b[i] = 'x'
            else:
                b[i] = m[1] + b[i]
    return ''.join(b)


print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))
