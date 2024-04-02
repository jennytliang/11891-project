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
    
	Include these tokens in the code: odd _ cnt , even _ cnt
	Do not include these tokens in the code: r
	"""
    ans = 0, 0
    # Your code here
    nums = [''.join(i) for i in itertools.product('01', repeat=int(math.log10(n) + 1)) if int(i) <= n]
    for num in nums:
        if int(num) % 2 == 0:
            ans = (ans[0] + 1, ans[1])
        else:
            ans = (ans[0], ans[1] + 1)
    return ans