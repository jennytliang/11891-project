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
	Do not include these tokens in the code: # Initial ization
	"""
    # Initial ization
    even_cnt = 0
    odd_cnt = 0
    # Write your code here

    # 1 <= n <= 1000
    for num in range(1, n + 1):
        num_str = str(num)
        if len(num_str) % 2 == 0:
            even_palin = num_str[0:len(num_str) // 2]
            odd_palin = num_str[len(num_str) // 2:]
            if even_palin == even_palin[::-1]:
                even_cnt += 1
            if odd_palin == odd_palin[::-1]:
                odd_cnt += 1
        else:
            if num_str == num_str[::-1]:
                even_cnt += 1

    return (even_cnt, odd_cnt)


def test_even_odd_palindrome():
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(12) == (4, 6)


if __name__ == "__main__":
    test_even_odd_palindrome()
