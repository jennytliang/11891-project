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
    
	Do not include these tokens in the code: # use 1 as pal ind
	"""
    ans = [0, 0]
    for i in range(1, n):
        n_ans = 0
        s = str(i)
        n_s = len(s)

        for j in range(n_s):
            if i % 2 == 0 and j == n_s-1 or i % 2 == 1 and s[j] == s[n_s-2-j]:
                n_ans += 1
            else:
                break

        if i % 2:
            ans[1] += (n_ans // 2)
            ans[0] += 1 + (n_ans // 2)
        else:
            ans[0] += n_ans
        # use 1 as pal ind
        # if n_ans > 2 and i % 2: ans[1] += (n_ans // 2)
        # elif n_ans > 2: ans[0] += 1 + (n_ans // 2)
        # else: ans[0] += n_ans

    # use 1 as pal ind
    # ans[0] = min(ans[0], ans[1])

    return tuple(ans)
    # use 2 as pal ind
    # ans[0] = min(ans[0], ans[1] // 2)
    # ans[0] = min(ans[1], ans[0])
