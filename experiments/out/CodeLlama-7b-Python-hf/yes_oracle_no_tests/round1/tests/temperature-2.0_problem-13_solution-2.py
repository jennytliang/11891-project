def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
	Include these tokens in the code: def query _ g cd ( a : int ,
	Do not include these tokens in the code: if <
	"""
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return greatest_common_divisor(b, a % b)


def main():
    import doctest
    doctest.testmod()

    # print(greatest_common_divisor(3, 5))
    # print(greatest_common_divisor(25, 15))


if __name__ == '__main__':
    main()




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
    inputs = [[3, 7], [10, 15], [49, 14], [144, 60], [100, 50], [98, 56], [540, 288], [81, 27], [33, 55], [7, 13], [14, 28], [10, 25], [12, 54], [21, 35], [100, 27], [98, 10], [49, 81], [33, 56], [55, 57], [13, 14], [540, 540], [81, 80], [34, 33], [287, 13], [80, 15], [49, 28], [14, 14], [54, 33], [57, 57], [10, 10], [13, 33], [14, 540], [49, 12], [56, 56], [33, 54], [10, 49], [28, 29], [55, 10], [14, 27], [50, 28], [55, 28], [50, 29], [25, 24], [21, 20], [82, 81], [80, 49], [55, 56], [9, 9], [57, 56], [81, 24], [287, 12], [81, 54], [56, 35], [56, 10], [287, 56], [35, 20], [81, 287], [15, 33], [27, 27], [20, 81], [24, 23], [15, 80], [55, 80], [28, 12], [81, 57], [29, 35], [49, 50], [29, 28], [49, 49], [10, 9], [99, 56], [80, 81], [81, 26], [540, 541], [100, 10], [81, 81], [100, 9], [101, 27], [13, 55], [55, 541], [540, 25], [287, 287], [100, 287], [10, 11], [9, 98], [15, 11], [34, 34], [98, 101], [98, 28], [11, 10], [286, 286], [27, 26], [58, 101], [21, 54], [58, 15], [54, 9], [81, 55], [21, 36], [540, 10], [13, 288], [50, 49], [14, 15], [28, 28], [108, 192], [419, 967], [987654321, 123456789], [234567890, 987654321], [123456789, 987654321], [1000000000, 999999999], [999999999, 111111111], [2516980251698, 1684168416841], [99999999, 3699637], [98765432100, 1234567890], [98765432100, 98765432100], [999999999, 1000000000], [987654321, 987654321], [111111111, 111111111], [111111111, 967], [419, 192], [999999999, 999999999], [193, 108], [191, 1000000000], [123456789, 999999999], [987654320, 987654321], [100000000, 100000000], [3699637, 3699637], [967, 234567890], [987654322, 987654322], [967, 108], [2516980251698, 987654322], [967, 967], [419, 1000000000], [99999999, 3699636], [1684168416842, 1684168416841], [1684168416842, 1684168416842], [967, 987654322], [191, 108], [99999999, 192], [987654324, 987654323], [999999999, 98765432100], [192, 192], [3699638, 999999999], [234567889, 987654321], [987654321, 108], [1000000001, 1000000000], [234567890, 1000000000], [1000000000, 1000000000], [98765432101, 98765432099], [234567889, 234567890], [106, 108], [193, 193], [999999999, 111111110], [98765432099, 108], [111111111, 999999999], [98765432101, 98765432101], [100000000, 987654320], [2516980251698, 194], [967, 987654323], [1684168416841, 192], [987654323, 987654323], [1000000000, 1000000001], [100000000, 99999999], [1000000000, 987654321], [987654320, 108], [987654321, 111111110], [2516980251698, 987654324], [98765432101, 98765432100], [234567890, 966], [194, 193], [966, 107], [194, 98765432100], [1000000000, 987654324], [98765432101, 98765432102], [98765432100, 98765432101], [1234567890, 100000000], [987654321, 10], [100000001, 100000000], [108, 108], [419, 98765432100], [234567889, 98765432100], [100000000, 1000000001], [987654323, 987654322], [123456789, 1000000001], [999999999, 987654322], [100000000, 98765432101], [193, 1684168416842], [3699638, 967], [987654320, 3699637], [3699638, 98765432101], [419, 234567890], [234567890, 234567890], [98765432102, 98765432101], [105, 108], [111111111, 1000000001], [987654324, 99999999], [193, 123456789], [105, 1684168416842], [1684168416842, 1684168416840], [1000000001, 987654321], [2516980251698, 1684168416842], [2516980251698, 2516980251698], [100000000, 987654321], [987654322, 987654321], [107, 987654323], [191, 1684168416842], [999999999, 1000000001], [111111110, 111111111], [108, 3699636], [123456790, 987654320], [98765432099, 98765432101], [234567888, 3699638], [1684168416840, 987654322], [234567888, 234567888], [192, 191], [111111111, 191], [109, 108], [419, 10], [123456788, 108], [1684168416841, 1684168416842], [999999998, 111111110], [987654324, 100000000], [98765432100, 3699638], [111111111, 999999998], [3699639, 999999999], [98765432099, 98765432098], [1000000002, 1000000001], [98765432100, 1000000000], [3699636, 107], [3699637, 108], [234567889, 3699638], [987654321, 1000000001], [987654324, 3699637], [105, 1684168416843], [419, 2516980251698], [999999998, 999999999], [98765432102, 1684168416843], [3699637, 109], [108, 966], [234567888, 1234567890], [98765432100, 1000000001], [1684168416841, 98765432102], [10, 3699636], [98765432098, 966], [123456790, 194], [100000001, 3699638], [191, 107], [3699637, 98765432100], [10, 419], [1000000001, 1000000001], [3699636, 108], [419, 419], [3699638, 111111110], [98765432099, 999999999], [966, 194], [100000000, 987654319], [194, 987654322], [987654321, 98765432099], [1000000002, 1000000002], [987654323, 1684168416841], [100000001, 987654321], [192, 193], [1000000000, 108], [98765432101, 2516980251698], [987654318, 108], [987654322, 987654318], [111111112, 111111111], [999999999, 987654321], [999999998, 108], [3699637, 999999999], [234567887, 3699638], [3699637, 191], [194, 98765432098], [2516980251699, 987654320], [99999999, 99999999], [3699639, 3699638], [123456788, 98765432102], [109, 109], [987654324, 987654320], [108, 3699638], [194, 194], [234567887, 123456788], [966, 966], [3699638, 191], [99999999, 987654320], [987654320, 1000000000], [191, 123456789], [987654322, 967], [106, 106], [3699637, 967], [234567890, 106], [98765432098, 2516980251698], [123456789, 193], [123456788, 419], [105, 111111111], [111111110, 419], [3699638, 123456788], [987654321, 987654322], [108, 999999998], [987654321, 193], [10, 123456790], [987654320, 987654320], [2516980251698, 419], [1684168416842, 108], [999999998, 194], [100000001, 419], [966, 193], [3699637, 987654320], [123456788, 987654322], [3699637, 192], [987654324, 108], [1684168416841, 1684168416840], [10, 123456789], [191, 191], [987654319, 107], [194, 999999998], [1000000001, 234567888], [987654320, 234567889], [100000001, 106], [1234567890, 109], [3699639, 419], [100000000, 987654318], [3699638, 3699638], [12, 12], [111111110, 98765432099], [193, 195], [1684168416840, 1684168416840], [123456788, 234567890], [418, 419], [12, 987654321], [108, 98765432100], [98765432102, 98765432102], [111111110, 123456788], [987654321, 987654320], [3699637, 3699639], [11, 11], [234567890, 234567889], [234567890, 234567891], [234567891, 234567892], [999999998, 999999998], [1000000001, 966], [195, 123456789], [967, 234567889], [965, 965], [195, 195], [3699636, 3699637], [12, 98765432100], [111111111, 100000000], [3699638, 99999999], [2516980251697, 1684168416842], [193, 191], [418, 987654320], [107, 2516980251698], [1000000000, 100000000], [1684168416844, 1684168416843], [111111110, 418], [106, 107], [234567889, 234567888], [98765432099, 234567889], [1684168416840, 111111111], [98765432100, 192], [234567889, 1000000000], [999999999, 1684168416843], [1684168416843, 1684168416845], [10, 106], [420, 419], [234567887, 3699636], [966, 987654321], [987654322, 968], [12, 987654318], [999999999, 12], [234567891, 3699637], [100000000, 111111111], [987654322, 987654324], [3699637, 98765432102], [123456789, 419], [987654319, 234567889], [234567887, 109], [2516980251699, 2516980251698], [123456790, 105], [1684168416843, 1684168416843], [98765432100, 109], [1234567890, 1234567890], [1000000002, 1000000000], [1234567890, 107], [105, 111111112], [109, 2516980251698], [123456788, 123456788], [3699638, 234567889], [1000000000, 111111111], [111111112, 987654319], [190, 1000000000], [234567890, 195], [107, 987654318], [98765432101, 1684168416845], [98765432099, 999999998], [193, 2516980251698], [1234567890, 1684168416843], [123456788, 418], [10, 987654321], [98765432100, 3699640], [234567890, 987654320], [999999998, 111111111], [1684168416841, 123456788], [98765432099, 98765432100], [234567888, 419], [968, 967], [2516980251697, 3699637], [987654322, 194], [987654319, 987654320], [2516980251698, 123456788], [123456790, 987654321], [123456790, 3699637], [107, 1684168416843], [987654319, 987654319], [3699636, 3699636], [109, 98765432100], [111111112, 123456788], [100000001, 98765432100], [194, 108], [234567888, 987654321], [999999998, 98765432101], [1684168416844, 1684168416844], [100000002, 100000001], [965, 966], [100000001, 100000003], [9, 987654320], [108, 123456790], [98765432100, 111111111], [123456790, 123456790], [1000000001, 1000000002], [194, 234567892], [111111111, 234567890], [987654321, 111111109], [98765432101, 3699637], [1684168416840, 1684168416842], [234567887, 987654318], [100000000, 2516980251698], [100000004, 100000000], [3699639, 107], [3699640, 107], [98765432099, 419], [98765432102, 98765432100], [234567891, 234567891], [987654323, 12], [234567887, 100000000], [100000002, 106], [3699636, 12], [98765432098, 98765432098], [190, 191], [100000003, 3699638], [2516980251698, 111111110], [234567890, 3699636], [100000003, 100000000], [1234567890, 987654321], [234567892, 234567891], [3699639, 3699639], [100000003, 100000003], [190, 190], [1000000001, 234567891], [3699638, 1684168416841], [1000000001, 2516980251698], [1684168416844, 987654321], [11, 98765432099], [123456788, 420], [98765432098, 10], [418, 987654324], [100000005, 420], [1684168416842, 100000001], [987654321, 100000003], [194, 191], [1684168416840, 1684168416841], [2516980251699, 2516980251699], [123456788, 195], [195, 965], [1000000000, 2516980251698], [3699635, 192], [107, 107], [2516980251698, 109], [234567892, 234567892], [194, 1234567890], [3699635, 100000003], [965, 195], [2516980251697, 194], [123456788, 1684168416842], [111111110, 111111110], [110, 109], [100000001, 100000001], [98765432100, 1684168416844], [968, 100000000], [1000000001, 234567892], [1684168416842, 123456788], [1684168416845, 98765432100], [234567888, 3699639], [12, 999999999], [123456788, 987654321], [111111109, 3699638], [1000000001, 9], [2516980251698, 111111109], [13, 12], [987654319, 987654321], [3699638, 123456787], [98765432102, 192], [99999999, 3699635], [967, 3699636], [1684168416846, 98765432100], [107, 195], [967, 98765432100], [1684168416842, 98765432102], [987654321, 100000000], [100000002, 1234567890], [195, 98765432102], [3699635, 3699636], [98765432099, 987654322], [11, 195], [107, 123456788], [1000000001, 234567893], [3699637, 123456788], [193, 192], [1684168416846, 999999998], [2516980251697, 1684168416843], [99999999, 111111110], [999999997, 111111110], [1234567890, 999999998], [1684168416845, 966], [100000001, 100000002], [1684168416845, 1684168416845], [194, 195], [111111112, 111111112], [987654322, 123456789], [191, 234567892], [12, 11], [968, 1684168416845], [1684168416845, 1000000001], [234567887, 1234567890], [999999998, 1000000001], [98765432102, 987654324], [193, 123456788], [234567891, 3699638], [1000000001, 100000005], [234567890, 1684168416842], [123456787, 123456788], [111111111, 968], [2516980251699, 999999997], [98765432100, 107], [98765432100, 234567890], [3699640, 111111109], [987654319, 111111111], [100000000, 1684168416846], [110, 987654319], [2516980251697, 111111109], [123456787, 111111111], [968, 968], [1684168416844, 190], [987654324, 968], [234567888, 194], [191, 98765432102], [1000000000, 234567888], [966, 234567888], [98765432100, 106], [123456789, 123456790], [966, 987654323], [987654324, 987654324], [1684168416841, 1684168416841], [109, 3699639], [234567891, 99999999], [10, 191], [987654320, 419], [193, 194], [98765432101, 987654318], [234567893, 2516980251698], [234567891, 108], [98765432102, 987654323], [1684168416840, 987654321], [10, 109], [123456789, 123456789], [999999997, 1684168416842], [999999997, 1000000001], [1234567889, 987654323], [3699637, 3699638], [111111109, 100000005], [98765432100, 98765432098], [111111111, 3699637], [1234567889, 111111111], [1000000000, 195], [111111109, 105], [123456791, 987654321], [987654320, 111111111], [1684168416846, 1684168416846], [987654325, 99999999], [1234567889, 1234567890], [1684168416845, 234567892], [11, 3699639], [98765432097, 98765432097], [967, 1684168416846], [1684168416845, 3699636], [111111110, 195], [234567886, 418], [987654325, 987654319], [98765432098, 1684168416844], [967, 969], [1000000000, 100000004], [111111111, 234567893], [2147483647, 1], [1, 1], [2147483647, 2147483647], [2516980251697, 1684168416841], [2516980251697, 98765432100], [3699637, 99999999], [966, 967], [967, 123456789], [108, 2516980251698], [98765432100, 98765432099], [107, 192], [987654321, 967], [99999999, 966], [123456789, 49], [2516980251698, 108], [2516980251698, 99999999], [111111109, 111111110], [98765432099, 1234567890], [107, 111111110], [966, 98765432100], [98765432099, 99999999], [98765432100, 111111110], [111111110, 98765432100], [111111110, 98765432101], [966, 49], [1234567890, 123456790], [111111109, 987654321], [123456790, 123456789], [2516980251697, 2516980251697], [111111110, 111111109], [234567890, 100000000], [108, 987654320], [2516980251698, 111111111], [98765432100, 967], [3699637, 987654321], [98765432101, 1234567890], [123456790, 98765432100], [1684168416841, 98765432099], [2516980251698, 1684168416840], [111111110, 2516980251697], [98765432101, 108], [98765432098, 98765432099], [987654321, 965], [966, 48], [111111110, 123456790], [111111109, 1684168416840], [967, 98765432101], [967, 999999999], [192, 966], [99999999, 965], [234567891, 234567890], [2516980251698, 2516980251697], [108, 107], [49, 48], [1000000000, 99999999], [99999999, 999999999], [1684168416841, 2516980251698], [419, 123456790], [111111110, 965], [98765432098, 1684168416840], [111111111, 2516980251697], [30, 98765432101], [107, 1684168416841], [1234567890, 1684168416841], [966, 2516980251698], [99999999, 98765432099], [966, 999999999], [999999998, 2516980251698], [234567890, 1234567890], [49, 98765432100], [234567890, 30], [966, 108], [419, 49], [966, 111111110], [234567891, 192], [100000000, 98765432098], [18, 192], [123456790, 1234567890], [111111110, 1000000000], [1684168416839, 1684168416840], [111111109, 100000000], [123456790, 98765432099], [123456789, 123456788], [999999999, 234567890], [98765432099, 107], [123456788, 999999998], [1684168416840, 192], [98765432101, 987654321], [966, 1234567890], [1684168416840, 2516980251697], [987654320, 123456789], [966, 987654320], [987654321, 234567890], [98765432099, 98765432099], [111111109, 111111109], [965, 987654321], [965, 987654320], [111111109, 1684168416839], [965, 98765432099], [30, 30], [108, 1000000000], [2516980251698, 3699636], [1684168416841, 99999999], [967, 111111109], [234567890, 967], [111111109, 123456788], [1684168416839, 98765432100], [30, 234567891], [965, 2516980251698], [111111111, 98765432100], [967, 107], [1684168416839, 123456789], [98765432099, 3699637], [2516980251698, 123456789], [966, 192], [111111110, 98765432098], [192, 1000000000], [98765432099, 234567891], [965, 98765432100], [108, 98765432099], [107, 98765432099], [1000000000, 965], [111111109, 967], [99999999, 1684168416841], [999999998, 234567890], [30, 100000000], [98765432100, 3699637], [234567890, 999999999], [1684168416839, 420], [1684168416841, 109], [3699637, 98765432099], [234567890, 111111109], [1684168416839, 49], [109, 192], [999999998, 98765432098], [999999998, 99999999], [18, 98765432100], [29, 98765432101], [108, 109], [999999999, 123456789], [123456789, 50], [99999999, 98765432101], [1684168416841, 111111110], [420, 123456790], [1684168416838, 1684168416840], [420, 98765432098], [111111111, 111111110], [98765432101, 99999999], [98765432100, 1684168416839], [2516980251698, 192], [420, 420], [100000000, 29], [3699638, 987654321], [987654321, 999999998], [108, 999999999], [192, 99999999], [3699635, 999999999], [123456790, 111111109], [2516980251697, 1684168416840], [99999999, 234567890], [109, 123456789], [123456790, 1684168416838], [123456787, 123456787], [987654320, 987654318], [2516980251699, 2516980251697], [966, 965], [100000000, 18], [3699636, 420], [2516980251699, 106], [111111112, 1234567890], [965, 1000000001], [1684168416840, 49], [108, 987654321], [3699635, 18], [1684168416839, 1684168416839], [48, 234567891], [123456787, 420], [1684168416838, 98765432099], [98765432100, 3699636], [419, 1684168416841], [3699637, 987654322], [1684168416839, 234567890], [1000000001, 109], [3699636, 123456787], [192, 234567890], [2516980251697, 2516980251698], [964, 965], [98765432099, 2516980251698], [100000000, 419], [123456790, 99999999], [964, 1684168416837], [234567891, 999999999], [1684168416841, 98765432098], [999999999, 100000000], [98765432100, 418], [1684168416837, 98765432100], [111111111, 111111112], [3699636, 98765432100], [965, 999999998], [18, 18], [999999998, 123456787], [123456787, 111111113], [3699638, 1684168416840], [999999999, 111111109], [965, 964], [1000000000, 98765432099], [3699637, 123456790], [966, 999999998], [29, 1684168416840], [418, 234567890], [2516980251699, 966], [111111110, 2516980251698], [1684168416840, 3699636], [111111109, 234567891], [3699635, 111111110], [49, 106], [106, 1684168416840], [98765432100, 964], [192, 2516980251699], [29, 109], [107, 3699637], [123456787, 2516980251698], [1684168416836, 98765432101], [2516980251697, 28], [969, 969], [418, 107], [3699636, 967], [30, 987654320], [192, 2516980251698], [111111109, 111111113], [1684168416841, 987654319], [111111109, 109], [3699635, 967], [49, 999999999], [99999999, 987654319], [987654320, 192], [99999999, 418], [123456788, 2516980251697], [111111111, 28], [123456789, 111111110], [111111114, 111111113], [50, 2516980251699], [965, 106], [123456790, 1684168416836], [964, 3699637], [3699640, 3699639], [987654322, 123456788], [108, 106], [1000000001, 28], [968, 966], [987654318, 987654320], [47, 234567891], [1684168416841, 108], [191, 192], [111111113, 99999999], [987654320, 234567890], [1684168416841, 987654321], [50, 234567890], [965, 98765432101], [98765432101, 420], [28, 2516980251698], [1000000000, 987654318], [987654322, 2516980251698], [999999998, 419], [987654321, 18], [969, 968], [418, 106], [29, 29], [100000000, 123456788], [234567891, 1684168416840], [987654318, 76], [1684168416842, 987654321], [966, 98765432101], [987654320, 987654322], [999999998, 98765432100], [987654319, 1000000001], [123456789, 107], [98765432101, 110], [111111113, 1234567890], [19, 18], [1000000001, 1234567890], [3699635, 2516980251699], [1684168416838, 29], [98765432102, 100000001], [111111111, 111111109], [234567889, 1684168416838], [1234567890, 966], [987654322, 419], [51, 50], [98765432098, 123456788], [418, 418], [1684168416840, 1684168416839], [51, 98765432101], [969, 111111109], [2516980251699, 965], [51, 100000000], [1684168416839, 987654319], [111111111, 2516980251698], [3699637, 418], [3699637, 1684168416843], [2516980251698, 28], [234567889, 418], [418, 987654321], [99999999, 999999998], [417, 418], [111111113, 98765432102], [234567890, 111111113], [987654321, 98765432100], [98765432099, 111111114], [1684168416839, 1684168416838], [98765432102, 987654321], [110, 123456789], [100000001, 1684168416841], [50, 98765432101], [98765432102, 968], [28, 47], [123456788, 50], [3699635, 3699635], [1000000001, 3699638], [964, 1684168416841], [966, 3699634], [123456788, 77], [234567890, 234567892], [100000000, 420], [987654319, 1684168416842], [1684168416841, 106], [49, 123456788], [2516980251697, 191], [3699640, 1684168416840], [987654318, 999999998], [19, 30], [76, 111111110], [19, 19], [107, 99999999], [418, 987654322], [111111109, 111111111], [123456788, 123456787], [30, 111111111], [3699637, 1684168416842], [111111113, 111111110], [3699639, 111111110], [2516980251697, 969], [964, 964], [965, 111111110], [987654318, 98765432099], [107, 48], [48, 964], [1684168416840, 123456789], [3699639, 966], [3699639, 1684168416839], [234567890, 421], [3699636, 419], [111111112, 999999999], [967, 968], [111111110, 111111112], [27, 28], [100000000, 2516980251699], [3699635, 98765432100], [123456790, 111111111], [1684168416838, 1684168416838], [234567890, 123456788], [111111110, 999999999], [98765432100, 966], [111111113, 111111113], [1684168416841, 100000001], [29, 30], [965, 111111109], [987654319, 3699638], [3699636, 28], [1684168416838, 49], [966, 111111112], [987654318, 968], [110, 98765432101], [49, 123456789], [1684168416836, 111111110], [111111109, 111111108], [123456790, 29], [48, 48], [50, 51], [1684168416841, 111111111], [111111111, 987654320], [234567889, 100000000], [234567892, 1684168416841], [987654320, 421], [964, 48], [111111108, 98765432098], [111111111, 190], [967, 966]]
    results = [1, 5, 7, 12, 50, 14, 36, 27, 11, 1, 14, 5, 6, 7, 1, 2, 1, 1, 1, 1, 540, 1, 1, 1, 5, 7, 14, 3, 57, 10, 1, 2, 1, 56, 3, 1, 1, 5, 1, 2, 1, 1, 1, 1, 1, 1, 1, 9, 1, 3, 1, 27, 7, 2, 7, 5, 1, 3, 27, 1, 1, 5, 5, 4, 3, 1, 1, 1, 49, 1, 1, 1, 1, 1, 10, 81, 1, 1, 1, 1, 5, 287, 1, 1, 1, 1, 34, 1, 14, 1, 286, 1, 1, 3, 1, 9, 1, 3, 10, 1, 1, 1, 28, 12, 1, 9, 1, 9, 1, 111111111, 1, 1, 90, 98765432100, 1, 987654321, 111111111, 1, 1, 999999999, 1, 1, 9, 1, 100000000, 3699637, 1, 987654322, 1, 2, 967, 1, 3, 1, 1684168416842, 1, 1, 3, 1, 9, 192, 1, 1, 9, 1, 10, 1000000000, 1, 1, 2, 193, 1, 1, 111111111, 98765432101, 80, 2, 1, 1, 987654323, 1, 1, 1, 4, 1, 2, 1, 2, 1, 1, 2, 4, 1, 1, 10, 1, 1, 108, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 234567890, 1, 3, 1, 3, 1, 1, 2, 1, 2, 2516980251698, 1, 1, 1, 1, 1, 1, 12, 123456790, 1, 2, 2, 234567888, 1, 1, 1, 1, 4, 1, 2, 4, 2, 1, 9, 1, 1, 100, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 6, 6, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1000000001, 12, 419, 2, 1, 2, 1, 2, 1, 1000000002, 1, 17, 1, 4, 1, 6, 2, 1, 9, 2, 1, 1, 1, 2, 1, 99999999, 1, 2, 109, 4, 2, 194, 17, 966, 1, 1, 80, 1, 1, 106, 1, 2, 2, 1, 1, 3, 1, 2, 1, 2, 1, 10, 987654320, 1, 2, 2, 1, 1, 1, 2, 1, 12, 1, 1, 191, 1, 2, 1, 1, 1, 1, 1, 2, 3699638, 12, 1, 1, 1684168416840, 2, 1, 3, 36, 98765432102, 2, 1, 1, 11, 1, 1, 1, 999999998, 7, 3, 1, 965, 195, 1, 12, 1, 1, 1, 1, 2, 1, 100000000, 1, 22, 1, 1, 1, 111, 12, 1, 3, 1, 2, 1, 1, 3, 2, 6, 3, 1, 1, 2, 1, 1, 1, 1, 1, 5, 1684168416843, 1, 1234567890, 2, 1, 7, 1, 123456788, 1, 1, 1, 10, 5, 1, 1, 1, 1, 3, 2, 1, 20, 10, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 987654319, 3699636, 1, 28, 17, 2, 3, 1, 1684168416844, 1, 1, 1, 1, 2, 9, 123456790, 1, 2, 1, 1, 1, 2, 1, 2, 4, 1, 1, 1, 2, 234567891, 1, 1, 2, 12, 98765432098, 1, 1, 22, 2, 1, 9, 1, 3699639, 100000003, 190, 1, 1, 11, 1, 1, 28, 2, 2, 105, 1, 1, 1, 1, 2516980251699, 13, 5, 2, 1, 107, 1, 234567892, 2, 1, 5, 1, 2, 111111110, 1, 100000001, 4, 8, 13, 2, 5, 3, 3, 17, 1, 1, 1, 1, 1, 1, 2, 1, 1, 18, 1, 1, 2, 1, 6, 1, 1, 1, 1, 1, 7, 1, 1, 2, 1, 11111111, 1, 2, 1, 1, 1684168416845, 1, 111111112, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 7, 2, 1, 1, 1, 1, 10, 1, 1, 2, 1, 1, 1, 968, 2, 4, 2, 1, 16, 6, 2, 1, 1, 987654324, 1684168416841, 1, 9, 1, 1, 1, 7, 1, 9, 1, 3, 1, 123456789, 1, 1, 1, 1, 1, 2, 1, 1, 5, 1, 1, 12345679, 1684168416846, 1, 1, 1, 1, 98765432097, 1, 1, 5, 2, 1, 2, 1, 4, 1, 1, 1, 2147483647, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 1, 2, 11, 1, 1, 1, 6, 1, 10, 10, 1, 7, 10, 1, 1, 2516980251697, 1, 10, 4, 1, 1, 1, 1, 10, 1, 2, 1, 1, 1, 1, 6, 10, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 9, 1, 1, 5, 2, 1, 1, 1, 1, 2, 1, 3, 2, 10, 1, 10, 6, 1, 2, 3, 2, 6, 10, 10, 1, 1, 1, 1, 1, 1, 2, 24, 1, 6, 1, 1, 2, 1, 98765432099, 111111109, 1, 5, 1, 1, 30, 4, 2, 1, 1, 1, 1, 1, 3, 1, 9, 1, 1, 1, 1, 6, 2, 64, 1, 5, 1, 1, 5, 1, 1, 2, 10, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 18, 1, 1, 9, 1, 1, 1, 10, 2, 2, 1, 1, 1, 2, 420, 1, 1, 1, 27, 3, 1, 1, 1, 1, 1, 2, 123456787, 2, 1, 1, 2, 12, 1, 2, 1, 7, 9, 1, 1684168416839, 3, 1, 1, 12, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 9, 1, 1, 2, 9, 1, 12, 1, 18, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 3, 22, 12, 1, 5, 1, 2, 4, 3, 1, 1, 1, 1, 1, 969, 1, 1, 10, 2, 1, 1, 1, 1, 1, 1, 16, 11, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 7, 2, 2, 1, 1, 1, 1, 10, 1, 10, 1, 7, 2, 2, 2, 1, 9, 1, 2, 29, 4, 3, 2, 1, 7, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 2, 418, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 987654321, 1, 1, 1, 1, 1, 1, 2, 1, 2, 3699635, 1, 1, 2, 7, 2, 20, 1, 1, 7, 1, 280, 2, 1, 2, 19, 1, 2, 1, 1, 3, 1, 1, 1, 1, 964, 5, 1, 1, 4, 3, 3, 1, 1, 1, 1, 1, 2, 1, 1, 5, 12345679, 1684168416838, 2, 1, 6, 111111113, 1, 1, 1, 1, 4, 1, 14, 2, 1, 1, 2, 1, 1, 48, 1, 1, 12345679, 1, 1, 1, 4, 2, 1, 1]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(greatest_common_divisor)