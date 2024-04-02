def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	"""
    prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if prime[i] == True:
            for j in range(i, n + 1, i):
                prime[j] = False
    for i in range(n, 0, -1):
        if prime[i]:
            return i

if __name__ == "__main__":
    import doctest
    doctest.testmod()



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
    inputs = [[15], [27], [63], [330], [13195], [100], [256], [500], [873], [9999], [121], [1764], [4096], [243], [1024], [4097], [1765], [120], [501], [4095], [10000], [255], [1025], [4094], [242], [1763], [254], [9998], [872], [9997], [502], [119], [9996], [874], [253], [252], [1762], [122], [4098], [871], [1023], [9995], [870], [99], [98], [118], [1761], [117], [123], [10001], [87], [92], [869], [1766], [93], [875], [244], [9994], [1767], [1760], [124], [245], [116], [9], [88], [10], [86], [246], [85], [115], [247], [1022], [91], [248], [125], [94], [10002], [249], [1768], [876], [38], [868], [1020], [8], [1026], [90], [866], [39], [867], [9993], [1027], [9992], [1029], [1028], [40], [18], [60], [49], [95], [48], [114], [96], [72], [1030], [9991], [13433], [456745], [568623], [32767], [4], [6], [12], [21], [13432], [13434], [22], [32766], [13435], [20], [456744], [568622], [81], [456743], [456742], [13431], [32765], [80], [456741], [456746], [32764], [32763], [568621], [82], [568624], [32768], [13430], [456740], [13429], [456739], [32762], [32769], [456747], [14], [32761], [32770], [568620], [24], [52], [568625], [51], [456738], [30], [50], [32760], [13428], [13427], [1000000], [16], [25], [13436], [456749], [13437], [26], [456748], [568626], [13438], [13439], [456750], [456751], [456752], [28], [32759], [84], [456753], [65], [64]]
    results = [5, 3, 7, 11, 29, 5, 2, 5, 97, 101, 11, 7, 2, 3, 2, 241, 353, 5, 167, 13, 5, 17, 41, 89, 11, 43, 127, 4999, 109, 769, 251, 17, 17, 23, 23, 7, 881, 61, 683, 67, 31, 1999, 29, 11, 7, 59, 587, 13, 41, 137, 29, 23, 79, 883, 31, 7, 61, 263, 31, 11, 31, 7, 29, 3, 11, 5, 43, 41, 17, 23, 19, 73, 13, 31, 5, 47, 1667, 83, 17, 73, 19, 31, 17, 2, 19, 5, 433, 13, 17, 3331, 79, 1249, 7, 257, 5, 3, 5, 7, 19, 3, 19, 3, 3, 103, 103, 101, 547, 17231, 151, 2, 3, 3, 7, 73, 2239, 11, 127, 2687, 5, 19031, 284311, 3, 919, 1597, 37, 6553, 5, 2671, 113, 8191, 163, 6389, 41, 5077, 2, 79, 557, 1033, 401, 16381, 331, 152249, 7, 181, 113, 13, 3, 13, 4549, 17, 76123, 5, 5, 13, 373, 463, 5, 2, 5, 3359, 5503, 1493, 13, 1283, 94771, 6719, 151, 29, 691, 28547, 7, 47, 7, 13841, 13, 2]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(largest_prime_factor)