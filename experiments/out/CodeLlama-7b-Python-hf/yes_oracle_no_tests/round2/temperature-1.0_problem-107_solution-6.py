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
    
	Include these tokens in the code: ,
	Do not include these tokens in the code: = 0
	"""

    odp = edp = 0
    for d in range(1, n):
        s = str(d)
        if s == s[::-1] and d % 2 == 0:
            edp += 1
        elif s == s[::-1] and d % 2 == 1:
            odp += 1
        elif not s == s[::-1]:
            s0, s1 = s[:len(s) // 2], s[len(s) // 2 :]
            if s0 == s0[::-1] or s1 == s1[::-1]:
                odp += 1
    return edp, odp
    