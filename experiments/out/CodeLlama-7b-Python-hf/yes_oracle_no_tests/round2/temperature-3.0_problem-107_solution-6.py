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
    if n < 1 or n > 1000:
        raise ValueError("n must be between 1 and 1000")

    even_palindromes = [1]
    odd_palindromes = [1]

    for i in range(2, n + 1):
        even_palindromes.append(even_palindromes[i - 1] + 2 * (i // 2))
        odd_palindromes.append(odd_palindromes[i - 1] + 2 * ((i - 1) // 2))

    return (
        even_palindromes[n],
        odd_palindromes[n]
    )
