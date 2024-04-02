def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r
	"""


    fo = []
    for i in range(1,n):
        if n%i == 0:
            fo.append(i)
    return max(fo)



def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r
	"""


    fo = []
    for i in range(1,n):
        if n%i == 0:
            fo.append(i)
    return max(fo)



def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r
	"""


    fo = []
    for i in range(1,n):
        if n%i == 0:
            fo.append(i)
    return max(fo)



def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r
	"""


    fo = []
    for i in range(1,n):
        if n%i == 0:
            fo.append(i)
    return max(fo)



def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r




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
    inputs = [[3], [7], [10], [100], [49], [2], [27], [101], [235], [500], [999], [1000], [36], [72], [81], [499], [234], [73], [998], [35], [22], [23], [1001], [74], [236], [82], [75], [99], [76], [77], [24], [28], [80], [238], [29], [237], [56], [57], [997], [30], [4], [102], [37], [233], [103], [78], [55], [5], [58], [21], [83], [25], [1003], [996], [11], [501], [34], [232], [995], [231], [33], [79], [502], [1004], [54], [1005], [1002], [20], [230], [98], [32], [31], [53], [65], [59], [38], [52], [19], [97], [64], [12], [51], [1006], [39], [40], [60], [61], [6], [96], [63], [26], [104], [239], [41], [88], [42], [84], [503], [43], [62], [18], [127], [1321], [500027], [732312], [1234567], [732313], [126], [500028], [1322], [732314], [1234568], [1320], [500029], [95], [500030], [732311], [1323], [1234569], [1234566], [500031], [50], [732315], [1234570], [732310], [128], [732309], [1324], [500026], [71], [732316], [131], [125], [500025], [70], [48], [47], [46], [994], [69], [124], [1234572], [1325], [500024], [132], [1234571], [1319], [94], [993], [130], [992], [129], [1318], [732317], [732318], [990], [44], [989], [732308], [732306], [732307], [732305], [732304], [1234565], [732303], [8], [732302], [92], [93]]
    results = [1, 1, 5, 50, 7, 1, 9, 1, 47, 250, 333, 500, 18, 36, 27, 1, 117, 1, 499, 7, 11, 1, 143, 37, 118, 41, 25, 33, 38, 11, 12, 14, 40, 119, 1, 79, 28, 19, 1, 15, 2, 51, 1, 1, 1, 39, 11, 1, 29, 7, 1, 5, 59, 498, 1, 167, 17, 116, 199, 77, 11, 1, 251, 502, 27, 335, 501, 10, 115, 49, 16, 1, 1, 13, 1, 19, 26, 1, 1, 32, 6, 17, 503, 13, 20, 30, 1, 3, 48, 21, 13, 52, 1, 1, 44, 21, 42, 1, 1, 31, 9, 1, 1, 45457, 366156, 9721, 23623, 63, 250014, 661, 366157, 617284, 660, 1, 19, 250015, 1, 441, 411523, 617283, 166677, 25, 244105, 617285, 366155, 64, 244103, 662, 250013, 1, 366158, 1, 25, 166675, 35, 24, 1, 23, 497, 23, 62, 617286, 265, 250012, 66, 94967, 1, 47, 331, 65, 496, 43, 659, 38543, 366159, 495, 22, 43, 366154, 366153, 15581, 146461, 366152, 246913, 244101, 4, 366151, 46, 31]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(largest_divisor)