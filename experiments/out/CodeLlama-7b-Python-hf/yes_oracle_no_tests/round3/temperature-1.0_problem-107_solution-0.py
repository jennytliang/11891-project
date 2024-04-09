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
	Do not include these tokens in the code: if n < 1 or n
	"""
    def helper(n, odd_cnt, even_cnt, digit_set):
        if n == 0:
            if len(digit_set) > 1:
                if int(''.join(str(digit) for digit in digit_set)) % 2 == 0:
                    even_cnt += 1
                else:
                    odd_cnt += 1
            return

        if len(digit_set) > 1:
            if int(''.join(str(digit) for digit in digit_set)) % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1

        for digit in range(n):
            digit_set.append(digit)
            helper(n - digit - 1, odd_cnt, even_cnt, digit_set)
            digit_set.pop()

    odd_cnt = 0
    even_cnt = 0
    digit_set = []
    helper(n, odd_cnt, even_cnt, digit_set)
    return (odd_cnt, even_cnt)


def test_even_odd_palindrome():
    assert (1, 2) == even_odd_palindrome(3)
    assert (4, 6) == even_odd_palindrome(12)
    assert (1, 3) == even_odd_palindrome(10)
    assert (1, 2) == even_odd_palindrome(8)
    assert (1, 2) == even_odd_palindrome(1)


if __name__ == '__main__':
    test_even_odd_palindrome()
