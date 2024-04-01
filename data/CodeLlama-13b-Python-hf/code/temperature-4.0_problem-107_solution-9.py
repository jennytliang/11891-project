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
    return count_even, count_odd


def get_factors(x):
    res = set()
    if x != 1:
        factors = get_prime_factors(10)
        factors = set(list(factors[i] for i in set(map(int, str(x))) if i != 0))

        for factor in factors:
            if x / factor == x // factor and x > factor:
                res.add(x)
                return res
            elif x / factor == x // factor and x == factor:
                res.add(x)
                res.add(x + 1)
                return res
        return set()
    else:
        res.add(x * x)
        return res


def get_palindrome(x=None):
    if x:
        if 1 <= x <= 9:
            return set([2, x, x+x])  # 10 is the prime between 9, and 99.
        num = 10
        palindrome = set()
        factors = get_factors(x)
        while x or (num * 10 + x) / num != num * 10 / num:
            if x > num * 10 + num:
                if 0 not in factors and num * num + x <= 10**len(str(x)))):
                    palindrome.add(x)
                    palindrome.add(x + x)
                    palindrome_factor = False
                else:
                    palindrome_factor = [0] * x
                    temp_i = x - num*num
                    while (num - 1) != (temp_i-1)//10 or temp_i - (temp_i-1)//10 != num * 10 * 1:
                        num += 1
                
            elif (num * 2 + x) // (num + 1) <= (9 + 1) and not palindrome_factor and 
