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
	Do not include these tokens in the code: # - ---------------- ---------------- ---------------- ---------------- --------
	"""
    odd_cnt = 0
    even_cnt = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            j = i
            while j > 0:
                if j % 10 != j // 10:
                    break
                j = j // 10
            if j == 0:
                even_cnt += 1
        else:
            j = i
            while j > 0:
                if j % 10 != j // 10:
                    break
                j = j // 10
            if j == 0:
                odd_cnt += 1
    return even_cnt, odd_cnt


def test_even_odd_palindrome():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)
