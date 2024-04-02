def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    return [x for x in range(a, b + 1) if x % 2 == 0]


if __name__ == "__main__":
    print(generate_integers(2, 8))
    print(generate_integers(8, 2))
    print(generate_integers(10, 14))




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
    inputs = [[2, 10], [10, 2], [132, 2], [17, 89], [6, 12], [13, 25], [50, 60], [100, 200], [201, 299], [5, 5], [11, 11], [10, 5], [5, 11], [50, 34], [5, 10], [201, 13], [34, 201], [12, 5], [34, 200], [201, 10], [299, 299], [200, 299], [25, 10], [201, 9], [11, 299], [12, 25], [5, 6], [13, 12], [14, 13], [200, 300], [60, 13], [50, 11], [13, 201], [14, 10], [5, 4], [5, 34], [201, 298], [200, 9], [300, 299], [199, 13], [200, 200], [298, 34], [13, 13], [34, 34], [14, 14], [13, 202], [6, 13], [12, 13], [34, 14], [300, 5], [301, 299], [201, 300], [14, 9], [299, 34], [301, 34], [300, 34], [302, 299], [4, 5], [300, 6], [25, 34], [298, 13], [199, 202], [199, 299], [11, 61], [9, 9], [201, 14], [199, 34], [9, 11], [5, 300], [11, 10], [10, 34], [100, 6], [13, 60], [12, 34], [202, 202], [14, 34], [298, 298], [50, 50], [6, 6], [201, 201], [61, 299], [61, 34], [200, 201], [10, 300], [301, 12], [62, 299], [100, 13], [297, 298], [6, 61], [200, 297], [298, 50], [302, 301], [199, 14], [12, 299], [6, 8], [198, 34], [201, 12], [202, 11], [201, 202], [12, 300], [7, 5], [300, 302], [8, 298], [8, 5], [100, 1000], [999, 1], [1, 100000], [10000, 1000], [1000, 10000], [56789, 123456], [987654321, 123456789], [101, 1001], [13, 17], [101, 110], [16, 13], [1000, 1000], [1001, 100000], [10000, 13], [56789, 56789], [56789, 56788], [2, 100000], [101, 101], [101, 123456789], [56788, 56789], [16, 16], [10000, 12], [17, 17], [1001, 1001], [2, 2], [100, 101], [10000, 10000], [56789, 1], [1, 1], [12, 100000], [10000, 10001], [987654321, 56789], [17, 2], [123456, 11], [12, 11], [16, 56787], [16, 1], [999, 2], [1001, 13], [56789, 10000], [987654321, 10001], [13, 11], [56789, 56790], [3, 100000], [13, 100], [1000, 56789], [102, 1001], [11, 10000], [56789, 123456789], [15, 110], [100000, 100000], [123456790, 123456789], [11, 100000], [14, 100], [11, 110], [10000, 14], [12, 1001], [3, 15], [56789, 9999], [987654321, 101], [16, 1001], [12, 12], [12, 1], [11, 123456], [16, 56790], [123456, 101], [999, 999], [14, 56790], [1001, 2], [56789, 1001], [101, 123456790], [15, 2], [1001, 1000], [10001, 3], [15, 56787], [100, 110], [56790, 100], [100000, 11], [2, 14], [110, 123456790], [101, 13], [2, 13], [56792, 100], [15, 16], [9999, 101], [999, 9999], [123456789, 123456789], [2, 1000], [999, 10000], [100, 56790], [56790, 56790], [1002, 100000], [10001, 10001], [12, 56790], [1, 56787], [56788, 56790], [3, 102], [987654322, 987654322], [14, 101], [56790, 1002], [998, 9999], [10001, 4], [123456788, 123456789], [100, 100], [56791, 56791], [56789, 101], [3, 3], [12, 123456790], [99, 99], [123457, 56789], [14, 16], [1, 10000], [11, 12], [2, 1], [12, 100], [100, 56787], [123457, 1001], [9999, 9999], [13, 56790], [56789, 102], [13, 3], [3, 99999], [1, 2], [12, 123456791], [12, 56787], [56788, 56788], [2, 123456789], [123456790, 998], [56787, 10000], [110, 110], [123456792, 123456791], [56792, 56791], [10000, 101], [123456, 1001], [10000, 11], [987654321, 3], [1000, 56792], [13, 14], [10, 11], [101, 100], [13, 16], [1000, 100000], [987654323, 123456789], [102, 13], [123457, 123457], [987654321, 99], [123458, 123457], [987654321, 100], [123456788, 123456788], [1002, 1002], [18, 18], [56787, 56787], [56788, 2], [123456789, 123456788], [99999, 99999], [13, 1000], [16, 15], [987654320, 123456791], [16, 999], [56789, 17], [10000, 15], [987654320, 56791], [102, 101], [123456789, 11], [999, 14], [56791, 110], [16, 101], [100001, 100001], [102, 100000], [987654323, 56789], [9999, 10000], [102, 102], [998, 101], [3, 2], [100001, 100000], [101, 10000], [11, 123455], [123456788, 17], [11, 13], [123456790, 123456790], [3, 16], [4, 101], [100001, 10000], [1001, 1002], [101, 12], [987654322, 17], [56788, 56787], [123456791, 123456792], [123456787, 123456788], [123456792, 56787], [15, 15], [99, 100], [1, 123456792], [1, 123458], [1, 56788], [123456791, 123456790], [999, 110], [18, 1], [102, 4], [4, 56787], [123455, 123455], [1002, 3], [56792, 123456789], [1000, 14], [987654321, 987654321], [123456790, 1001], [123456791, 99], [1001, 1], [56790, 18], [123456789, 123456790], [15, 56790], [10001, 10000], [123455, 101], [14, 10000], [12, 4], [99, 1000], [123456791, 123456791], [102, 10000], [56790, 14], [13, 1002], [1000, 110], [123456791, 99999], [9999, 15], [11, 998], [123456791, 100000], [987654321, 110], [998, 998], [100001, 9999], [56791, 10001], [101, 56787], [123456788, 987654322], [10002, 10000], [16, 998], [56787, 100], [101, 9999], [123456789, 123458], [56790, 13], [123456787, 123456789], [1002, 5], [1003, 3], [56787, 56788], [1003, 123456789], [100, 1], [987654323, 987654323], [56793, 100], [123456790, 56787], [1000, 123456788], [123456789, 123457], [100000, 99999], [998, 2], [123456791, 56788], [123456, 100000], [56789, 56792], [1001, 100], [17, 14], [987654322, 100], [10000, 123457], [10002, 14], [123456787, 101], [4, 1002], [10001, 1], [100, 14], [101, 103], [1001, 15], [109, 110], [987654323, 12], [1, 10002], [123456789, 56789], [123455, 56792], [123456791, 99998], [9999, 56788], [10001, 56787], [56785, 15], [13, 9999], [1004, 123456789], [123457, 123456788], [102, 9999], [123458, 99], [99, 987654320], [123457, 14], [12, 99999], [123458, 123455], [123456791, 123456789], [1000, 15], [123456790, 123456791], [987654323, 101], [101, 123455], [1000, 103], [16, 17], [101, 123456], [1002, 123456787], [56787, 10001], [123458, 2], [98, 100], [101, 987654321], [10, 56790], [999, 100001], [13, 102], [1002, 1003], [1, 1001], [101, 123458], [123456789, 1004], [123456792, 123456792], [13, 56791], [100000, 100], [10002, 15], [123456791, 101], [56791, 100], [1004, 100], [16, 1000], [66, 14], [1001, 110], [10000, 56787], [10001, 100], [12, 102], [4, 17], [123456791, 56791], [56791, 123455], [99, 1004], [3, 56792], [1, 56790], [1005, 10001], [100000, 100001], [123454, 123455], [56792, 987654324], [987654322, 11], [15, 1002], [9999, 999], [56789, 9], [123456, 56789], [1000, 1001], [123456793, 123456792], [56793, 987654320], [2, 3], [12, 109], [998, 123456792], [56790, 56787], [99, 56787], [10001, 11], [56786, 56787], [987654321, 1000], [987654320, 9], [10000, 123456789], [99998, 1], [997, 2], [1001, 99], [123455, 11], [987654322, 987654323], [12, 3], [100000, 1000], [1003, 2], [100000, 10001], [1003, 102], [1004, 16], [100, 123456793], [56786, 2], [123455, 999], [123456, 123456789], [1000, 102], [56790, 56789], [9999, 100001], [109, 123455], [123456789, 123456791], [2, 56787], [987654325, 987654324], [10001, 123456790], [16, 11], [56786, 987654324], [100000, 10], [56791, 56790], [17, 987654322], [1003, 10000], [99996, 99996], [101, 123456788], [100, 16], [10000, 99998], [11, 100001], [10000, 123454], [56785, 56790], [11, 14], [98, 99], [17, 13], [123456791, 1000], [66, 56792], [987654325, 123456], [10001, 56789], [101, 102], [99996, 1005], [56786, 1003], [100, 103], [100, 987654321], [19, 1], [10002, 123456787], [99999, 10000], [12, 987654321], [56791, 9999], [10002, 4], [123458, 9999], [18, 2], [1004, 11], [56787, 99999], [99998, 99998], [1003, 56787], [56789, 56787], [56789, 2], [123458, 13], [56788, 12], [123455, 987654322], [123456792, 987654323], [123456790, 997], [56786, 1], [1004, 14], [1003, 1003], [16, 987654320], [15, 14], [102, 5], [987654321, 987654322], [56792, 110], [987654319, 99999], [10000, 1005], [1003, 1001], [10001, 18], [102, 56787], [998, 16], [4, 12], [56786, 14], [17, 11], [66, 5], [11, 123456789], [102, 100], [56787, 1003], [16, 19], [987654325, 11], [987654322, 100000], [123456787, 123456787], [10, 56785], [110, 998], [15, 13], [101, 56789], [1006, 10000], [1006, 56790], [11, 123456790], [987654321, 123456], [1000, 104], [1000, 111], [987654325, 17], [1002, 56789], [56787, 15], [10000, 1001], [1, 15], [56790, 123456792], [56793, 1005], [123458, 12], [10001, 10002], [12, 99996], [987654320, 1], [101, 56791], [14, 15], [123456789, 997], [111, 110], [56792, 987654322], [56792, 56792], [123458, 100000], [56790, 11], [1002, 13], [56792, 1002], [56785, 998], [123456791, 14], [9999, 1001], [123456789, 12], [103, 123456789], [13, 18], [101, 123456791], [56788, 100], [11, 109], [10, 10], [99996, 998], [1004, 1004], [66, 66], [987654321, 4], [999, 123456], [100, 99], [100000, 987654323], [1, 56791], [13, 2], [123456790, 56788], [110, 1], [987654320, 56793], [11, 123458], [11, 10001], [102, 100001], [17, 100], [10000, 16], [999, 998], [987654319, 56791], [56792, 987654321], [102, 98], [123456788, 1004], [1, 56786], [56791, 101], [13, 1], [987654321, 2], [1, 99999], [13, 1001], [10000, 999], [1000, 999], [1000, 998], [99999, 109], [987654321, 1001], [1000, 1], [56789, 123455], [99999, 1000], [13, 123456789], [17, 56789], [56789, 110], [987654320, 987654321], [13, 123456], [100000, 123456789], [987654321, 987654320], [999, 100000], [998, 13], [17, 123456789], [99, 110], [98, 987654321], [2, 56788], [12, 110], [99, 998], [111, 13], [999, 13], [987654321, 56788], [56789, 99999], [101, 1], [56789, 109], [111, 123456789], [998, 999], [987654319, 987654321], [111, 12], [10000, 123455], [987654320, 987654320], [109, 98], [111, 10000], [56789, 987654321], [1001, 111], [99, 98], [123456789, 18], [1001, 101], [99999, 999], [100, 10000], [56788, 17], [10000, 987654319], [100, 12], [987654319, 987654320], [987654323, 13], [987654323, 18], [987654321, 18], [123456788, 123456790], [18, 101], [1000, 19], [99998, 123455], [101, 1000], [13, 998], [998, 18], [999, 987654320], [1001, 123456788], [101, 100000], [101, 99], [110, 98], [100, 11], [18, 987654320], [18, 123456], [987654321, 123456788], [110, 111], [18, 123455], [10000, 123456], [99998, 999], [13, 110], [14, 123456789], [56788, 13], [100, 9999], [123456788, 999], [987654321, 11], [123456790, 13], [99997, 123455], [17, 99998], [1, 123456788], [101, 99998], [56788, 123456789], [111, 10001], [109, 56789], [987654319, 123456789], [987654319, 987654319], [100, 999], [56789, 100000], [101, 11], [987654324, 987654321], [987654324, 1000], [56788, 123456790], [12, 111], [110, 12], [99, 102], [987654320, 98], [999, 11], [13, 99], [999, 101], [100000, 13], [123456789, 19], [11, 111], [56788, 123456788], [19, 13], [10001, 100000], [1, 56789], [13, 99998], [987654323, 987654320], [109, 99998], [18, 11], [987654323, 123455], [56788, 998], [56787, 1000], [17, 56788], [99998, 987654319], [19, 19], [56789, 13], [111, 1], [123455, 111], [99999, 13], [1001, 16], [100, 111], [99998, 123456], [56789, 12], [98, 98], [987654321, 99997], [987654320, 12], [110, 11], [987654319, 123456788], [98, 110], [14, 99998], [56788, 19], [99998, 1001], [1001, 998], [987654324, 123455], [16, 99999], [99, 1001], [19, 999], [987654326, 987654325], [10000, 102], [987654320, 56788], [101, 98], [1000, 123456790], [14, 1000], [987654322, 123456789], [99999, 1001], [20, 19], [100000, 12], [987654320, 56786], [1, 123456787], [9999, 20], [13, 111], [100, 99998], [987654322, 123456790], [111, 111], [999, 123455], [13, 101], [16, 123456], [14, 1001], [123456789, 56788], [18, 1001], [99999, 12], [987654323, 123454], [99999, 100000], [123456, 999], [56786, 56789], [100000, 987654325], [987654319, 11], [987654324, 987654324], [987654320, 18], [18, 987654319], [987654325, 987654320], [10, 10000], [123453, 998], [101, 999], [999, 100], [1000, 123456791], [19, 18], [99998, 12], [56789, 99], [987654322, 123456791], [11, 101], [987654326, 99], [20, 100000], [102, 1000], [2, 56786], [987654322, 99], [987654319, 123454], [110, 123456], [987654321, 17], [1000, 56787], [2, 101], [123456791, 111], [18, 123456788], [1002, 101], [123454, 56787], [10000, 19], [987654320, 987654319], [18, 17], [19, 101], [123453, 18], [123456789, 13], [123456, 20], [987654320, 15], [987654325, 10000], [99998, 13], [99997, 123456787], [56787, 1], [109, 56786], [987654326, 987654326], [56790, 99999], [987654322, 987654321], [987654319, 123455], [1001, 10001], [99999, 99998], [1001, 10000], [10001, 123456789], [999, 987654326], [123456788, 1001], [123453, 123454], [99997, 19], [987654322, 12], [987654322, 2], [102, 108], [98, 1], [18, 987654318], [123456788, 101], [1000, 123456787], [999, 987654325], [20, 987654323], [123456790, 11], [98, 97], [123454, 123454], [10001, 123456], [20, 123456787], [102, 56786], [1, 12], [9999, 1000], [11, 99999], [56787, 987654318], [10000, 9999], [1000, 13], [15, 98], [100, 123456788], [99998, 123453], [123456789, 99998], [17, 987654319], [123455, 1001], [123456787, 998], [97, 17], [99999, 17], [123457, 1000], [109, 100000], [987654321, 999], [99997, 99998], [17, 16], [102, 123456788], [123456788, 111], [987654321, 56790], [99997, 99997], [20, 999], [104, 987654325], [99, 100000], [18, 987654322], [999, 99999], [101, 998], [123455, 123456], [109, 15], [123456790, 123454], [1, 999], [123456788, 123456787], [100, 123457], [56786, 98], [100, 98], [20, 99], [1, 99997], [20, 99999], [108, 12], [123456, 123456], [100, 2], [987654325, 56790], [1001, 56787], [56788, 109], [123456788, 100000], [123454, 110], [97, 97], [100000, 14], [19, 10000], [3, 56787], [1002, 10001], [123454, 1001], [11, 123456788], [123455, 2], [20, 56788], [108, 999], [987654320, 123453], [99999, 123453], [97, 98], [9999, 56787], [1001, 98], [111, 99999], [987654317, 987654324], [123456786, 123456786], [123457, 123456], [2, 17], [987654320, 19], [1, 101], [14, 123456787], [123457, 123453], [123455, 14], [18, 987654321], [99999, 987654321], [987654318, 1000], [10000, 123456788], [123456788, 109], [99999, 14], [17, 18], [987654325, 987654325], [56787, 999], [11, 100], [19, 20], [112, 10001], [123452, 123453], [2, 110], [11, 97], [56786, 56788], [99998, 101], [99999, 123456791], [987654319, 1001], [123456788, 1002], [987654322, 123456788], [111, 10002], [13, 56786], [100000, 110], [104, 108], [123456788, 56786], [18, 56787], [2, 999], [123455, 987654324], [987654319, 10001], [987654324, 987654319], [987654319, 987654326], [100000, 987654321], [987654324, 987654318], [987654323, 1000], [987654316, 987654315], [123456786, 123456], [13, 15], [123456786, 98], [99997, 987654322], [1002, 998], [56787, 56786], [123455, 10001], [102, 109], [123452, 987654321], [17, 100000], [108, 13], [100000, 999], [16, 987654324], [123457, 100], [999, 123456789], [8, 9], [108, 10001], [987654319, 10000], [108, 108], [10002, 56786], [123456788, 100], [987654324, 987654325], [987654317, 12], [987654326, 100], [123456790, 987654323], [1002, 111], [987654321, 9], [111, 1001], [111, 9999], [987654323, 987654322], [99, 123456789]]
    results = [[2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8], [], [6, 8], [], [], [], [], [], [], [6, 8], [6, 8], [], [6, 8], [], [], [6, 8], [], [], [], [], [], [], [], [], [6], [], [], [], [], [], [], [], [4], [6, 8], [], [], [], [], [], [], [], [], [], [], [6, 8], [], [], [6, 8], [], [], [], [], [], [], [], [4], [6, 8], [], [], [], [], [], [], [], [], [], [6, 8], [], [], [6, 8], [], [], [], [], [], [], [6], [], [], [], [], [], [], [], [], [], [6, 8], [], [], [], [], [], [6, 8], [], [], [], [], [], [6], [], [8], [6, 8], [], [2, 4, 6, 8], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [2], [], [], [2, 4, 6, 8], [], [], [], [], [2, 4, 6, 8], [], [], [], [2, 4, 6, 8], [2, 4, 6, 8], [], [], [], [], [], [4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [4, 6, 8], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [2, 4, 6, 8], [], [], [2, 4, 6, 8], [], [4, 6, 8], [], [], [], [], [2, 4, 6, 8], [], [], [2, 4, 6, 8], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [2, 4, 6, 8], [], [4, 6, 8], [], [], [], [], [4, 6, 8], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [2], [], [], [], [], [], [], [4, 6, 8], [4, 6, 8], [2], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2], [], [], [], [], [], [], [4, 6, 8], [4, 6, 8], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8], [], [], [2, 4, 6, 8], [4, 6, 8], [4, 6, 8], [], [4, 6, 8], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [6, 8], [4, 6, 8], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [4, 6, 8], [2, 4, 6, 8], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [4, 6, 8], [], [], [], [4, 6, 8], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [2], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [2, 4, 6, 8], [], [], [], [4, 6, 8], [], [2, 4, 6, 8], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [4, 6, 8], [], [2, 4, 6, 8], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [6, 8], [], [], [], [], [], [], [], [], [4, 6, 8], [], [], [6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [4, 6, 8], [], [], [], [2, 4, 6, 8], [2, 4, 6, 8], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [4, 6, 8], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [8], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(generate_integers)