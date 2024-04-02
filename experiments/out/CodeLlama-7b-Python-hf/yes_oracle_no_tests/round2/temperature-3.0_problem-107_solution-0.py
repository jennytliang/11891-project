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
	Do not include these tokens in the code: # initialize
	"""
    # Initialization:
    # odd_cnt = 0
    # even_cnt = 0
    # odd = 0
    # even = 0
    # end = 0
    # start = 0

    # Implementation:
    odd_cnt = 0
    even_cnt = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            odd_cnt += 1
        else:
            even_cnt += 1
    return (odd_cnt, even_cnt)


print(even_odd_palindrome(10))
print(even_odd_palindrome(12))
print(even_odd_palindrome(120))
print(even_odd_palindrome(121))
print(even_odd_palindrome(122))
print(even_odd_palindrome(123))
print(even_odd_palindrome(124))
print(even_odd_palindrome(125))
print(even_odd_palindrome(126))
print(even_odd_palindrome(127))
print(even_odd_palindrome(128))
print(even_odd_palindrome(129))
print(even_odd_palindrome(130))
print(even_odd_palindrome(131))
print(even_odd_palindrome(132))
print(even_odd_palindrome(133))
print(even_odd_palindrome(134))
print(even_odd_palindrome(135))
print(even_odd_palindrome(136))
print(even_odd_palindrome(137))
print(even_odd_palindrome(138))
print(even_odd_palindrome(139))
print(even_odd_palindrome(140))
print(even_odd_palindrome(141))
print(even_odd_palindrome