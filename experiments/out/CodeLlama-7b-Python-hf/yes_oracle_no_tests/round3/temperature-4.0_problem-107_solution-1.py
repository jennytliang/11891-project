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
    # -----------------------------
    # if n == 1:
    #     return 0

    # if n % 2 == 0:
    #     return (1, n)
    # else:
    #     return (n, 0)

    # -----------------------------
    # if n <= 10:
    #     return (n, 0)

    # if n % 2 == 0:
    #     return (n / 2, 0)
    # else:
    #     return (n / 2, 1)

    # -----------------------------
    # if n <= 10:
    #     return (n, 0)

    # if n % 2 == 0:
    #     return (n / 2, 0)
    # else:
    #     return (n / 2, 1)

    # -----------------------------
    if n <= 10:
        return (n, 0)

    if n % 2 == 0:
        return (n // 2, 0)
    else:
        return (n // 2, 1)

    # -----------------------------


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert even_odd_palindrome(1) == (0, 1), "1st example"
    assert even_odd_palindrome(3) == (1, 2), "2nd example"
    assert even_odd_palindrome(12) == (4, 6), "3rd example"
    assert even_odd_palindrome(23) == (11, 12), "4th example"
    assert even_odd_palindrome(32) == (16, 16), "5th example"
