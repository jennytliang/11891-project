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
    
	Include these tokens in the code: odd _ cnt , even _ cnt =
	"""
    # initialize count of odd and even palindromes
    odd_cnt = 0
    even_cnt = 0
    # iterate through all numbers
    for i in range(1, n+1):
        # if number is even and palindromic
        if i % 2 == 0 and is_palindrome(i):
            even_cnt += 1
        # if number is odd and palindromic
        elif is_palindrome(i):
            odd_cnt += 1
    # return tuple of counts
    return (odd_cnt, even_cnt)


def is_palindrome(n):
    """
    Given an integer n, return whether n is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    Example 1:

        Input: n = 121
        Output: true
        Explanation: 121 is a 3-digit number. Its 3-digit number is 121.

    Example 2:

        Input: n = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:

        Input: n = 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Example 4:

        Input: n = -101
        Output: false
        Explanation: Reads 101 from right to left. Therefore it is not a palindrome.

    Note:
        1. The input n is an integer in the range [-999, 999].
    """
    # initialize reversed number
    rev = 0
    # iterate through digits of input number
    for i in str(n):
        # reverse input number
        rev = rev * 10 + int(i)
    # return whether input number is equal to reverse
    return n == rev


print(