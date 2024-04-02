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
                    while (num - 1) != (temp_i-1)//10 or temp_i - (temp_i-1)//10 != num * 10: 
    return set()






import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[123], [12], [3], [63], [25], [19], [9], [1], [1000], [500], [777], [10], [15], [27], [35], [50], [89], [201], [51], [11], [26], [778], [88], [202], [28], [200], [31], [30], [999], [32], [36], [87], [779], [998], [203], [86], [33], [14], [29], [34], [24], [204], [13], [23], [780], [85], [781], [206], [16], [499], [84], [207], [17], [205], [997], [199], [498], [37], [776], [775], [22], [52], [83], [774], [782], [78], [21], [208], [773], [98], [209], [497], [772], [996], [18], [8], [53], [7], [38], [79], [90], [20], [771], [97], [82], [6], [496], [770], [77], [62], [91], [783], [502], [61], [210], [92], [60], [93], [503], [501], [76], [75], [59], [888], [555], [400], [978], [505], [506], [401], [979], [504], [96], [556], [887], [507], [889], [508], [554], [977], [402], [399], [553], [95], [890], [398], [509], [886], [99], [510], [511], [891], [94], [552], [551], [550], [397], [885], [980], [396], [884], [100], [512], [994], [995], [57], [395], [892], [557], [982], [993], [80], [883], [981], [983], [58], [984], [403], [404], [5], [976], [974], [405], [985], [4], [973], [975], [893], [39], [494], [986], [101]]
    results = [(8, 13), (4, 6), (1, 2), (6, 8), (5, 6), (4, 6), (4, 5), (0, 1), (48, 60), (28, 30), (38, 48), (4, 5), (4, 6), (5, 6), (5, 7), (6, 7), (8, 9), (8, 20), (6, 7), (4, 6), (5, 6), (38, 48), (8, 9), (9, 20), (5, 6), (8, 20), (5, 6), (5, 6), (48, 60), (5, 6), (5, 7), (7, 9), (38, 48), (48, 59), (9, 20), (7, 9), (5, 7), (4, 6), (5, 6), (5, 7), (5, 6), (9, 20), (4, 6), (5, 6), (38, 48), (7, 9), (38, 48), (9, 20), (4, 6), (28, 30), (7, 9), (9, 20), (4, 6), (9, 20), (48, 59), (8, 20), (28, 30), (5, 7), (38, 47), (38, 47), (5, 6), (6, 7), (7, 9), (38, 47), (38, 48), (7, 9), (4, 6), (9, 20), (38, 47), (8, 9), (9, 20), (28, 30), (38, 47), (48, 59), (4, 6), (4, 4), (6, 7), (3, 4), (5, 7), (7, 9), (8, 9), (4, 6), (38, 47), (8, 9), (7, 9), (3, 3), (28, 30), (38, 47), (7, 9), (6, 8), (8, 9), (38, 48), (28, 30), (6, 8), (9, 20), (8, 9), (6, 8), (8, 9), (28, 30), (28, 30), (7, 8), (7, 8), (6, 8), (47, 50), (28, 36), (18, 30), (48, 57), (28, 31), (28, 31), (18, 30), (48, 58), (28, 30), (8, 9), (28, 36), (46, 50), (28, 31), (47, 50), (28, 31), (28, 35), (48, 57), (18, 30), (18, 30), (28, 35), (8, 9), (47, 50), (18, 30), (28, 31), (46, 50), (8, 10), (28, 31), (28, 31), (47, 50), (8, 9), (28, 35), (28, 35), (28, 35), (18, 30), (46, 50), (48, 58), (18, 30), (46, 50), (8, 10), (28, 31), (48, 59), (48, 59), (6, 8), (18, 30), (47, 50), (28, 36), (48, 58), (48, 59), (7, 9), (46, 50), (48, 58), (48, 58), (6, 8), (48, 58), (18, 30), (19, 30), (2, 3), (48, 57), (48, 57), (19, 30), (48, 58), (2, 2), (48, 57), (48, 57), (47, 50), (5, 7), (28, 30), (48, 58), (8, 11)]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(even_odd_palindrome)