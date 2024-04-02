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
    assert 1000 >= number >= 1
    m = [' m ', ' ']
    r = ['i','v','x','l','c','d','m']
    n = len(m)
    nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    c = ['m','c','d','l','v','u']

    out = ''
    for i in range(1,n+1):
        while (number-nums[i-1] >= (n)):
            number -= nums[i-1]
            out += c[i-1]
    if number > 0:
        print('Error, out of range.', number)
    print(out)

int_to_mini_roman(19)