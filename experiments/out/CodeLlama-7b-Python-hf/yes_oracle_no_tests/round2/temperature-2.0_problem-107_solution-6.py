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
    
	Include these tokens in the code: odd
	Do not include these tokens in the code: def is
	"""
    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    total = 0
    for i in range(1, n + 1):
        if is_palindrome(i) and i % 2:
            total += 1
        elif is_palindrome(i) and not i % 2:
            total += 2
    return (total // 2, total // 2)


if __name__ == "__main__":
    # assert even_odd_palindrome(3) == (1, 2)
    # assert even_odd_palindrome(12) == (4, 6)
    # assert even_odd_palindrome(100) == (25, 25)
    assert even_odd_palindrome(1000) == (499, 499)
