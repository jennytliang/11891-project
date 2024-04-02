def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    
	Include these tokens in the code: or a ** 2 + c ** 2
	'''

    return a ** 2 + b ** 2 == c ** 2


assert(right_angle_triangle(3, 4, 5))
assert(not right_angle_triangle(1, 2, 3))
assert(not right_angle_triangle(1, 1, 2))
assert(not right_angle_triangle(2, 2, 3))
assert(not right_angle_triangle(1, 2, 1))
assert(right_angle_triangle(3, 4, 3))



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
    inputs = [[3, 4, 5], [1, 2, 3], [10, 6, 8], [2, 2, 2], [7, 24, 25], [10, 5, 7], [5, 12, 13], [15, 8, 17], [48, 55, 73], [1, 1, 1], [2, 2, 10], [9, 12, 15], [20, 21, 29], [7, 9, 12], [8, 15, 17], [6, 8, 10], [4, 7, 8], [12, 16, 20], [3, 5, 6], [3, 4, 6], [5, 13, 12], [15, 17, 6], [12, 21, 20], [5, 4, 8], [12, 21, 21], [16, 7, 20], [16, 8, 20], [3, 5, 3], [16, 5, 20], [12, 10, 20], [6, 8, 13], [12, 11, 20], [16, 6, 6], [15, 6, 21], [5, 12, 20], [3, 8, 7], [20, 7, 20], [20, 21, 21], [21, 21, 21], [10, 19, 19], [5, 16, 20], [20, 21, 30], [6, 6, 21], [12, 7, 20], [30, 8, 8], [20, 21, 23], [13, 16, 20], [5, 5, 17], [12, 4, 21], [19, 11, 20], [21, 5, 21], [21, 20, 21], [22, 5, 21], [16, 21, 21], [19, 11, 11], [13, 20, 23], [9, 8, 13], [12, 10, 10], [5, 12, 21], [20, 23, 21], [5, 12, 30], [6, 12, 20], [3, 4, 3], [5, 13, 21], [11, 10, 11], [13, 13, 23], [21, 17, 21], [16, 5, 21], [20, 5, 21], [30, 23, 21], [21, 21, 20], [9, 12, 14], [20, 5, 20], [20, 22, 20], [17, 5, 10], [5, 5, 5], [24, 23, 24], [11, 12, 11], [11, 11, 12], [3, 5, 21], [16, 9, 6], [5, 22, 21], [12, 13, 21], [20, 22, 5], [5, 6, 6], [20, 20, 20], [3, 16, 5], [22, 13, 21], [16, 8, 19], [8, 16, 18], [24, 8, 7], [20, 22, 31], [31, 23, 21], [21, 20, 20], [17, 8, 20], [20, 21, 20], [7, 24, 6], [6, 21, 21], [4, 23, 21], [24, 8, 8], [19, 19, 19], [12, 13, 12], [23, 21, 21], [20, 11, 20], [24, 24, 24], [22, 13, 5], [16, 9, 15], [22, 9, 5], [20, 23, 5], [11, 12, 15], [8, 12, 8], [10, 120, 240], [13, 14, 15], [25, 60, 65], [12, 35, 37], [10001, 10000, 1], [399, 456, 762], [383, 226, 495], [77, 110, 138], [2020, 2021, 1], [14, 76, 110], [12, 15, 15], [10001, 10000, 10000], [495, 226, 226], [495, 495, 495], [12, 383, 37], [10001, 10001, 10001], [11, 383, 37], [11, 9, 36], [10001, 10000, 10001], [12, 35, 138], [13, 14, 16], [2020, 1, 2020], [12, 25, 37], [495, 60, 495], [495, 60, 496], [60, 496, 496], [11, 456, 9], [12, 14, 16], [13, 14, 13], [12, 226, 36], [76, 16, 2020], [25, 65, 37], [10001, 495, 10001], [25, 65, 16], [35, 138, 35], [9, 10001, 10001], [15, 13, 13], [11, 12, 14], [12, 14, 60], [11, 119, 120], [120, 12, 15], [14, 10001, 2022], [65, 10001, 2022], [455, 399, 456], [16, 76, 2020], [10, 120, 10], [13, 456, 13], [2022, 75, 2020], [138, 138, 15], [119, 120, 240], [12, 2020, 37], [137, 36, 138], [496, 495, 495], [14, 60, 60], [13, 15, 13], [119, 383, 15], [14, 14, 14], [495, 59, 60], [383, 137, 495], [12, 2020, 12], [496, 10000, 10000], [9, 10000, 10001], [2020, 2019, 2019], [65, 60, 60], [75, 2020, 76], [16, 75, 2020], [35, 12, 35], [11, 12, 456], [65, 37, 37], [35, 240, 138], [137, 36, 455], [10, 76, 2022], [384, 37, 11], [384, 385, 11], [26, 25, 26], [10000, 35, 10000], [10, 384, 13], [2020, 12, 2019], [25, 383, 2019], [25, 24, 65], [65, 10000, 10001], [11, 457, 9], [14, 495, 14], [399, 120, 13], [65, 59, 65], [2019, 138, 138], [10002, 10001, 10002], [226, 65, 60], [10000, 10001, 2022], [495, 496, 226], [1, 14, 14], [2020, 2019, 10000], [762, 120, 120], [2020, 2020, 24], [119, 383, 119], [15, 495, 14], [12, 66, 66], [2019, 2019, 2019], [11, 11, 9], [13, 14, 9999], [14, 10001, 14], [25, 37, 37], [137, 10, 455], [455, 38, 37], [35, 138, 138], [12, 15, 25], [456, 456, 495], [65, 10000, 65], [1, 13, 14], [66, 16, 16], [384, 12, 16], [10, 9, 119], [119, 10, 10], [383, 762, 383], [2019, 138, 139], [137, 455, 455], [14, 60, 14], [16, 10001, 35], [65, 2023, 2023], [65, 2023, 2019], [16, 10001, 10002], [12, 12, 12], [25, 384, 65], [37, 226, 495], [13, 10001, 13], [77, 110, 77], [9, 36, 36], [2023, 120, 120], [15, 14, 14], [16, 16, 75], [37, 385, 37], [61, 65, 60], [15, 2022, 2022], [2020, 1, 1], [34, 139, 138], [66, 37, 36], [13, 16, 13], [10000, 383, 10001], [35, 12, 12], [25, 762, 65], [16, 14, 14], [37, 226, 37], [25, 37, 14], [10, 120, 496], [12, 14, 17], [10, 66, 76], [110, 77, 110], [12, 66, 65], [1, 455, 455], [12, 15, 12], [13, 10001, 10001], [2022, 456, 2020], [383, 119, 119], [384, 15, 66], [25, 12, 15], [14, 24, 60], [456, 456, 10], [138, 138, 384], [10, 16, 120], [14, 15, 65], [10000, 10001, 10000], [2021, 66, 12], [9999, 456, 455], [35, 11, 12], [13, 2020, 12], [10001, 10002, 10001], [60, 60, 60], [9, 2020, 1], [10000, 10000, 10000], [12, 75, 12], [139, 139, 139], [110, 77, 9999], [15, 10001, 15], [17, 2022, 1], [35, 35, 2020], [76, 10000, 10000], [11, 2020, 37], [119, 2021, 66], [2023, 65, 10000], [24, 16, 16], [383, 36, 37], [456, 456, 38], [1, 12, 60], [36, 59, 496], [138, 35, 35], [383, 16, 36], [67, 16, 16], [65, 65, 59], [2023, 67, 10000], [9999, 383, 75], [38, 495, 10000], [399, 59, 65], [495, 59, 67], [11, 13, 456], [2022, 2022, 2020], [76, 26, 26], [119, 66, 66], [10001, 16, 16], [59, 10001, 10001], [16, 14, 15], [8, 10001, 10000], [26, 12, 12], [384, 16, 66], [9, 10000, 10000], [35, 10000, 10000], [10002, 12, 66], [110, 138, 110], [10000, 65, 10000], [10001, 26, 10002], [11, 383, 383], [10, 240, 10], [495, 12, 495], [456, 456, 385], [9999, 110, 75], [61, 12, 12], [240, 67, 16], [17, 10000, 10001], [11, 9, 11], [13, 14, 14], [10002, 10001, 16], [11, 2020, 11], [13, 226, 226], [10001, 10000, 138], [119, 25, 15], [61, 59, 60], [12, 10001, 10001], [12, 37, 37], [10000, 10001, 10001], [399, 120, 398], [75, 12, 12], [456, 455, 385], [2022, 67, 10000], [495, 58, 65], [14, 1, 14], [14, 496, 138], [10000, 495, 383], [10, 2021, 119], [119, 10, 2021], [13, 65, 59], [13, 495, 495], [77, 110, 76], [26, 10000, 26], [37, 37, 37], [16, 495, 60], [9, 9999, 67], [2020, 12, 75], [9, 9, 2020], [10000, 17, 457], [12, 37, 17], [456, 13, 455], [12, 15, 17], [10, 12, 15], [456, 2021, 13], [26, 66, 26], [2022, 399, 2020], [10000, 12, 12], [37, 38, 37], [25, 762, 10002], [13, 35, 35], [24, 10001, 16], [35, 35, 2023], [456, 455, 386], [67, 226, 495], [65, 16, 9], [457, 137, 10], [10001, 16, 10001], [496, 16, 10002], [35, 240, 35], [26, 398, 26], [2021, 399, 139], [226, 35, 226], [383, 137, 137], [61, 226, 65], [14, 14, 10001], [15, 12, 2022], [76, 75, 2020], [16, 16, 120], [9, 2022, 39], [12, 65, 65], [11, 456, 456], [2022, 15, 2022], [494, 495, 495], [119, 383, 14], [58, 61, 66], [11, 494, 11], [13, 65, 67], [10000, 13, 10000], [2019, 11, 11], [110, 8, 2019], [14, 383, 119], [10000, 10, 10000], [65, 383, 10000], [10001, 495, 8], [10001, 383, 10001], [10000, 495, 8], [8, 9, 10000], [35, 35, 2021], [12, 36, 37], [495, 59, 75], [13, 13, 13], [12, 13, 226], [2020, 494, 24], [110, 8, 60], [137, 2021, 137], [384, 457, 12], [13, 15, 15], [10001, 2022, 13], [11, 11, 11], [36, 59, 10000], [15, 12, 25], [16, 455, 495], [87, 24, 49], [87, 10001, 35], [10001, 37, 495], [38, 120, 38], [399, 399, 37], [226, 66, 457], [61, 65, 65], [399, 119, 13], [12, 15, 61], [9, 12, 2022], [10, 12, 12], [34, 17, 138], [10000, 383, 383], [13, 65, 15], [65, 58, 13], [2021, 13, 49], [37, 58, 35], [10002, 16, 10003], [110, 2019, 110], [59, 65, 59], [9, 2023, 2022], [455, 10, 11], [136, 12, 137], [226, 383, 35], [39, 38, 14], [77, 76, 110], [12, 386, 2023], [110, 2019, 12], [138, 2023, 67], [385, 2022, 10001], [16, 1, 383], [36, 60, 59], [13, 10002, 15], [59, 65, 65], [25, 10001, 25], [10, 11, 10], [58, 226, 383], [495, 120, 67], [119, 120, 120], [75, 10001, 16], [2019, 65, 37], [76, 120, 240], [16, 16, 14], [2021, 49, 13], [10000, 9999, 119], [456, 456, 456], [76, 16, 76], [13, 13, 15], [36, 39, 35], [383, 10, 383], [10002, 10002, 457], [10000, 2023, 10001], [9, 119, 10], [398, 14, 14], [110, 8, 2023], [120, 67, 120], [66, 36, 36], [494, 16, 10002], [38, 65, 37], [35, 65, 15], [59, 11, 65], [16, 49, 66], [76, 75, 11], [12, 16, 15], [76, 240, 120], [24, 65, 136], [137, 2020, 12], [87, 87, 35], [15, 14, 139], [383, 119, 383], [137, 13, 226], [38, 25, 37], [12, 384, 12], [49, 2022, 2022], [77, 2019, 139], [37, 457, 137], [67, 457, 67], [457, 2020, 37], [10002, 457, 457], [2023, 120, 136], [2023, 1, 120], [65, 138, 15], [25, 12, 10], [10, 76, 110], [10000, 65, 66], [398, 24, 65], [17, 75, 26], [10001, 10001, 10000], [2020, 15, 2020], [385, 2020, 12], [15, 12, 2019], [455, 455, 455], [2021, 13, 13], [398, 496, 495], [11, 36, 35], [76, 12, 36], [383, 37, 12], [67, 10, 240], [39, 496, 385], [66, 37, 398], [60, 65, 60], [58, 62, 66], [12, 74, 12], [10002, 10002, 762], [9999, 75, 2020], [495, 60, 75], [10001, 762, 10002], [1, 455, 1], [139, 139, 138], [77, 36, 36], [383, 14, 14], [60, 60, 61], [60, 496, 15], [2023, 49, 2019], [457, 110, 10002], [2022, 65, 383], [398, 12, 15], [35, 35, 36], [119, 384, 15], [77, 77, 110], [2020, 11, 24], [2019, 65, 36], [11, 25, 35], [12, 15, 18], [13, 12, 15], [384, 2021, 12], [26, 25, 25], [11, 383, 11], [37, 37, 138], [77, 26, 139], [384, 11, 384], [2019, 400, 2020], [139, 138, 138], [138, 138, 138], [64, 25, 65], [35, 35, 35], [14, 76, 18], [120, 240, 240], [37, 227, 495], [383, 25, 383], [34, 2020, 74], [398, 59, 65], [457, 39, 457], [384, 14, 75], [399, 39, 496], [35, 34, 17], [25, 65, 25], [110, 2019, 2019], [457, 12, 139], [26, 25, 15], [385, 2021, 12], [762, 65, 25], [73, 12, 12], [13, 12, 385], [139, 60, 61], [120, 13, 120], [110, 138, 111], [2021, 65, 65], [10, 120, 120], [399, 39, 38], [398, 58, 398], [456, 457, 12], [49, 65, 15], [12, 456, 10], [10001, 399, 10001], [385, 10001, 14], [400, 87, 139], [67, 15, 26], [12, 456, 456], [76, 60, 76], [2022, 2020, 2020], [15, 16, 12], [13, 60, 60], [382, 11, 383], [8, 9, 10001], [65, 37, 36], [15, 15, 15], [87, 138, 138], [37, 24, 37], [10001, 17, 10001], [17, 25, 25], [16, 121, 121], [495, 496, 496], [65, 37, 65], [2018, 2018, 18], [58, 65, 66], [16, 75, 16], [75, 11, 2020], [14, 139, 10001], [383, 37, 65], [11, 37, 2018], [37, 386, 68], [2018, 1, 9999], [495, 496, 495], [8, 7, 10], [110, 49, 49], [456, 457, 456], [495, 17, 496], [1, 1, 2], [3, 4, 7], [5, 3, 4], [4, 5, 3], [1, 2, 1], [2, 1, 1], [2, 2, 5], [13, 14, 226], [10001, 1, 1], [60, 10000, 1], [9, 495, 12], [13, 60, 13], [120, 120, 240], [457, 457, 456], [10000, 457, 10000], [13, 2019, 226], [13, 120, 226], [9, 12, 13], [8, 12, 13], [457, 10000, 10000], [2021, 2, 2], [226, 457, 456], [14, 10000, 10000], [10, 495, 12], [14, 9, 495], [762, 763, 762], [10001, 1, 25], [2021, 456, 2], [9, 9, 12], [10000, 10000, 1], [10001, 1, 457], [2021, 2, 3], [9, 12, 9], [9, 12, 12], [10000, 1, 1], [77, 13, 226], [10, 495, 25], [226, 240, 120], [10001, 2020, 457], [14, 240, 14], [9, 12, 3], [2020, 225, 1], [77, 138, 77], [8, 456, 762], [457, 77, 456], [10001, 1, 10001], [9, 12, 11], [457, 457, 9], [12, 2, 3], [226, 2, 2], [8, 25, 12], [120, 120, 120], [2020, 1, 60], [383, 227, 495], [457, 12, 37], [763, 763, 12], [8, 495, 12], [763, 457, 456], [10001, 3, 10001], [65, 2, 3], [10001, 14, 77], [15, 226, 12], [14, 12, 15], [13, 13, 226], [11, 13, 14], [10001, 110, 2], [763, 12, 763], [60, 12, 763], [455, 2, 2], [763, 227, 77], [226, 12, 240], [13, 226, 10000], [10002, 65, 2], [10000, 9999, 1], [9999, 9999, 2], [763, 457, 763], [13, 226, 227], [2021, 8, 8], [11, 10000, 456], [226, 9, 240], [1, 2019, 9999], [138, 456, 10001], [457, 10001, 10001], [35, 496, 495], [14, 240, 495], [226, 241, 12], [763, 496, 763], [65, 60, 3], [12, 37, 225], [457, 457, 457], [65, 2, 65], [10000, 10001, 1], [225, 12, 225], [2020, 2021, 2020], [11, 35, 37], [242, 12, 13], [225, 2020, 2021], [12, 2, 12], [763, 762, 227], [456, 12, 37], [763, 763, 763], [457, 12, 10001], [138, 2020, 10002], [14, 457, 77], [11, 60, 763], [138, 3, 3], [26.117120159873124, 94.48837938393268, 94.48837938393268], [10000, 10001, 111], [35, 37, 37], [12, 11, 13], [120, 14, 25], [1, 8, 2], [13, 36, 37], [10001, 13, 9], [14, 15, 15], [241, 9, 9], [2021, 2, 36], [2, 2, 2021], [242, 226, 13], [138, 137, 1], [10001, 2021, 10002], [456, 12, 12], [12, 13, 13], [457, 456, 2022], [383, 13, 13], [763, 496, 764], [10002, 763, 3], [15, 241, 10000], [36, 36, 36], [120, 2022, 240], [10, 12, 9], [9999, 2, 2], [1, 15, 227], [94.48837938393268, 26.117120159873124, 93.65019636949225], [60, 13, 763], [2, 2021, 2021], [496, 227, 495], [15, 495, 9999], [14, 2, 15], [399, 762, 762], [2, 26, 25], [110, 241, 12], [225, 226, 240], [2020, 1, 10], [138, 455, 10002], [2019, 1, 1], [10000, 10002, 111], [10, 227, 227], [15, 3, 1], [2021, 13, 3], [15, 496, 9999], [26, 2, 2], [2020, 457, 457], [94.82545294464254, 26.117120159873124, 94.48837938393268], [241, 111, 12], [77, 12, 12], [11, 12, 240], [242, 227, 495], [137, 10000, 240], [10001, 10, 1], [13, 3, 3], [225, 13, 13], [137, 240, 137], [242, 496, 495], [110, 26, 12], [11, 61, 763], [137, 9999, 240], [10000, 60, 763], [77, 10002, 111], [13, 456, 456], [35, 457, 456], [10, 12, 10001], [13, 10002, 12], [2021, 13, 9999], [2019, 2019, 457], [457, 456, 457], [240, 9, 9], [457, 225, 3], [94.48837938393268, 26.117120159873124, 26.117120159873124], [10001, 8, 495], [9999, 3, 3], [8, 240, 9], [65, 60, 65], [11, 15, 240], [226, 120, 226], [2, 25, 25], [10001, 111, 77], [2022, 77, 138], [10000, 64, 10000], [10000, 35, 1], [138, 37, 225], [239, 240, 14], [457, 456, 456], [138, 2, 36], [13, 26, 2], [13, 239, 12], [763, 13, 763], [37, 26, 26], [764, 3, 2], [10001, 8, 10001], [457, 61, 2022], [64, 66, 64], [60, 12, 3], [10, 10000, 227], [10001, 2022, 10001], [14, 136, 77], [763, 8, 763], [111, 10002, 13], [35, 457, 457], [457, 10001, 10000], [2021, 15, 14], [241, 12, 12], [8, 12, 11], [12, 10, 13], [14, 12, 13], [9, 495, 9], [11, 15, 15], [11, 10002, 111], [14, 36, 36], [13, 120, 225], [8, 11, 12], [457, 10002, 226], [2, 495, 495], [226, 111, 226], [9998, 2, 9999], [9997, 2, 9999], [458, 10003, 10002], [11, 11, 764], [14, 13, 13], [2019, 1, 2019], [13, 456, 10], [64, 67, 120], [12, 14, 12], [11, 12, 13], [2020, 2020, 2020], [120, 3, 2], [14, 3, 14], [35, 35, 13], [10001, 2021, 136], [764, 3, 3], [10002, 11, 13], [26.117120159873124, 113.29820827740289, 26.117120159873124], [60, 36, 36], [13, 9, 10], [60, 15, 13], [10000, 14, 14], [1, 9998, 227], [37, 36, 36], [14, 763, 240], [10002, 763, 2], [15, 495, 1], [137, 762, 458], [9, 455, 12], [457, 10002, 10000], [456, 12, 11], [66, 455, 2], [10000, 25, 10000], [35, 457, 455], [383, 2022, 495], [225, 2020, 2020], [12, 14, 14], [456, 10003, 10002], [763, 12, 9], [766, 765, 12], [456, 14, 457], [12, 12, 13], [8, 11, 8], [762, 763, 67], [1, 240, 1], [11, 2, 37], [60, 11, 3], [15, 226, 15], [456, 10, 456], [12, 10002, 10001], [764, 3, 764], [763, 66, 457], [10002, 10002, 10001], [13, 26, 26], [10, 13, 2], [12, 10001, 13], [2, 239, 3], [137, 496, 458], [762, 763, 37], [15, 455, 10001], [496, 35, 495], [11, 8, 8], [36, 61, 763], [763, 77, 227], [241, 112, 12], [10001, 3, 456], [65, 66, 64], [2, 64, 3], [2020, 457, 2020], [226, 10000, 226], [10, 8, 8], [9, 13, 15], [10001, 2, 10001], [457, 9, 10], [15, 13, 15], [457, 239, 12], [2019, 10001, 10001], [9, 10003, 9], [2020, 458, 10001], [77, 241, 241], [36, 37, 65], [2020, 15, 10000], [11, 7, 8], [240, 1, 240], [2022, 75, 138], [2021, 26, 65], [60, 766, 15], [14, 239, 12], [137, 10000, 112], [457, 227, 10001], [9999, 495, 9999], [9, 11, 9], [14, 495, 495], [66, 64, 64], [66, 64, 66], [12, 240, 15], [763, 3, 764], [764, 241, 241], [110, 10002, 13], [9999, 10000, 239], [242, 241, 9], [227, 9, 9], [9998, 25, 495], [10001, 14, 383], [239, 457, 1], [2021, 2, 2020], [456, 2, 456], [111, 1, 60], [94.82545294464254, 94.82545294464254, 26.117120159873124], [2, 64, 2], [111, 226, 225], [111, 1, 111], [11, 25, 3], [111, 67, 225], [13, 242, 3], [35, 35, 14], [15, 14, 25], [13, 120, 120], [494, 766, 495], [242, 12, 226], [9, 2019, 13], [120.27264036217386, 95.48313167066331, 26.117120159873124], [24.71115668501026, 93.15108572417166, 93.65019636949225], [24, 457, 65], [64, 63, 64], [1, 15, 228], [240, 10, 10], [2, 26, 2], [242, 226, 226], [9, 77, 12], [77, 10002, 8], [10, 10, 10], [458, 457, 457], [495, 9999, 495], [2022, 9, 138], [12, 226, 226], [9997, 1, 9999], [13, 239, 11], [458, 27, 2], [27, 26, 2], [226, 12, 12], [7, 1, 137], [66, 762, 763], [7, 11, 8], [1, 15, 15], [136, 240, 137], [456, 12, 456], [111, 77, 77], [226, 8, 225], [10000, 120, 226], [13, 457, 457], [8, 8, 8], [762, 494, 763], [25.16373529161418, 94.48837938393268, 94.48837938393268], [9997, 9999, 9997], [455, 3, 2], [13, 240, 15], [457, 77, 14], [2, 9, 2020], [59, 12, 8], [66, 66, 67], [12, 3, 12], [9, 239, 12], [1, 11, 765], [138, 138, 456]]
    results = [True, False, True, False, True, False, True, True, True, False, False, True, True, False, True, True, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(right_angle_triangle)