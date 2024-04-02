def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    
	Include these tokens in the code: odd _ cnt ,
	"""

    even_cnt = 1
    odd_cnt = 0
    for x in range(2, n+1, 1):
        y = str(x)         # string data
        if len(y) <= 1:
            continue

        # first, flip the number with reverse function
        y_rev = y[::-1] 
        if y == y_rev:     # if y is palindrome
            if x % 2 == 0:    # even number
                #print(f'x:{x}, y:{y},y_rev:{y_rev}. even')
                even_cnt += 1
            else:                   # odd number
                odd_cnt += 1
        else:               # y != y_rev
            continue

    return (odd_cnt, even_cnt)


result = even_odd_palindrome(12)
print(result)
