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
    
	Include these tokens in the code:  odd _ cnt , even _ cnt
	"""

    # initialize the variables
    odd_cnt = 0
    even_cnt = 0
    
    # check for the even palindromes
    for i in range(1234, n + 1, 2):
        # check for the even length palindromes
        for j in range(len(str(i)) + 1):
            # check for the even length palindromes
            if i / 10 ** j == int(str(i)[::-1][j]):
                even_cnt += 1
                break

    # check for the odd palindromes
    for i in range(1234, n + 1, 2):
        # check for the odd length palindromes
        for j in range(len(str(i)) + 1):
            # check for the odd length palindromes
            if i / 10 ** (j + 1) == int(str(i)[::-1][j]):
                odd_cnt += 1
                break

    return (even_cnt, odd_cnt)


if __name__ == "__main__":
    n = 10
    print(even_odd_palindrome(n))
