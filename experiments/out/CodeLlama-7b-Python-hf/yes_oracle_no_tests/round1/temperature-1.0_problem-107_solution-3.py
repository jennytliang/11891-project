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
    # use 1 as palindromes
    odd_cnt = 0

    # use 1 as palindromes
    even_cnt = n % 2

    # get half and even or odd, for example: 4 is half of 8, and even
    for i in range(n // 2 + 1):
        if i % 2 == 0:
            odd_cnt += pow(10, i) * 4
            even_cnt += pow(10, i) * 2
        else:
            odd_cnt += pow(10, i) * 3

    return even_cnt, odd_cnt
