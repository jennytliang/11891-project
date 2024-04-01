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
    """
    count_even = count_odd = 0
    for i in reversed(range(10 ** len(str(n)) // 2, n + 1)):
        palindrome_number = get_palindrome(i)
        for n in palindrome_number:
            if i == n:
                if n % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
    i = 0
    while i * 10 + i <= n:
        palindrome_number = get_palindrome(0)
        for n in palindrome_number:
            if n == 2 * i:
                if n % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
        i *= 10
    if n % 2 and 1 < n - (i * 9 + i - 9) <= n:
        count_odd += 1