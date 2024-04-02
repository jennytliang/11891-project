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
    s = n
    # O(100) = O(1)
    while s % 10 == 0:
        s //= 10

    m = 10
    # O(10) ~ O(5720) >> O(1) >> O(10)
    while s >= m :   # O(1)
        # O(25) ~ O(1275) >> O(1) >> O(10)
        if int(str(s)[::-1]) / m == s: # O(1)
            # O(11) ~ O(685) >> O(1) >> O(10)
            if int(str(m)[::-1]) / m == m: # O(1)
                if (m % 10 != 0) or (s % 10 != 0):
                    break
            return tuple((len(range(s + 1, m)[::2]), len(range(m + 1, s)[::2])))
        m *= 10