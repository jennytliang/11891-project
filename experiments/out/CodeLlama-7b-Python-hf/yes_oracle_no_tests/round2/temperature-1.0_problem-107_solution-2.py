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
    
	Do not include these tokens in the code: # odd pal ind rome count
	"""
    if n < 1:
        return (0, 0)

    even_palindromes = 1
    odd_palindromes = 1

    # add even palindromes
    for i in range(1, n):
        if i % 2 == 0:
            even_palindromes += 1

    # add odd palindromes
    for i in range(1, n):
        if i % 2 != 0:
            odd_palindromes += 1

    return (even_palindromes, odd_palindromes)


if __name__ == "__main__":
    assert even_odd_palindrome(1) == (1, 0)
    assert even_odd_palindrome(2) == (1, 1)
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(13) == (4, 7)
    assert even_odd_palindrome(14) == (4, 8)
    assert even_odd_palindrome(15) == (4, 9)
    assert even_odd_palindrome(16) == (5, 10)
    assert even_odd_palindrome(17) == (5, 11)
    assert even_odd_palindrome(18) == (5, 12)
    assert even_odd_palindrome(19) == (5, 13)
    assert even_odd_palindrome(20) == (6, 14)
    assert even_odd_palindrome(21) == (6, 15)
    assert even_odd_palindrome(22) == (6, 16)
    assert even_odd_palindrome(23) == (6, 17)
    assert even_odd_palindrome(24) == (6, 18)
