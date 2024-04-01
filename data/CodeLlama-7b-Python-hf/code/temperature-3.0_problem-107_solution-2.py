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
    even, odd = 1, 1

    for i in range(3, n + 1):
        even_digits = even_digits_in_palindrome(i)
        even += even_digits * (i // pow(10, even_digits))

        odd_digits = odd_digits_in_palindrome(i, even_digits)
        odd += odd_digits * (i // pow(10, odd_digits))

    return even, odd


def even_digits_in_palindrome(num):
    digits = int(math.log10(num)) + 1

    if digits % 2 == 0:
        return digits // 2
    else:
        return digits // 2 + 1


def odd_digits_in_palindrome(num, even):
    odd = int(math.log10(num)) - even + 1
    return min(odd, 2)