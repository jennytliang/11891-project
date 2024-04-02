def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n <= 0:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
    return x
        
    




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
    inputs = [[7, 34, 12], [15, 8, 5], [3, 33, 5212], [1259, 3, 52], [7919, -1, 12], [3609, 1245, 583], [91, 56, 129], [6, 34, 1234], [1, 2, 0], [2, 2, 0], [-2, 0, 1], [0, 500, 1000], [11, 1, 0], [25, -25, 25], [37, 123, 456], [113, 100, 200], [17, 5, 9], [31, -5, 22], [49, 0, 3], [61, 20, 40], [100, 99, 200], [62, 40, 20], [199, 99, 200], [5, 100, 5], [500, 500, 500], [62, 40, 62], [25, -26, 25], [123, 499, 500], [17, 9, 17], [6, 123, 100], [37, 122, 455], [37, 123, 25], [49, 3, 3], [11, 100, 201], [6, 100, 100], [99, 99, 200], [41, 20, 20], [36, 456, 37], [500, 501, 500], [100, 456, 99], [500, 500, 501], [62, 49, 100], [31, 1, 31], [1000, 62, 501], [-4, -3, -26], [100, 200, 200], [41, 122, 455], [100, 19, 200], [99, 41, 1], [49, -26, -26], [99, 99, 99], [50, 49, 3], [17, 18, 9], [6, 1, 100], [99, 40, 99], [41, 0, 3], [31, 500, 22], [5, 101, 5], [41, 3, -26], [498, 501, 500], [49, -4, 3], [41, 499, -26], [-4, -26, -26], [99, -25, 99], [26, 25, 26], [40, 61, 62], [99, 3, 9], [41, 199, 24], [32, 500, 22], [-3, -26, -3], [31, 32, 22], [500, 500, 22], [98, 199, 200], [113, 200, 200], [5, 5, 5], [1, 0, 3], [501, 456, 37], [19, 113, 100], [-28, -27, -4], [38, 122, 455], [40, 0, 98], [37, 123, 6], [19, 200, 200], [199, 99, -5], [499, 5, 20], [99, 9, 100], [500, 500, 122], [50, 36, 3], [113, 100, 113], [456, 100, 100], [0, 456, 37], [-3, -3, 9], [48, 0, 499], [25, 1000, -26], [100, 31, 1000], [100, 456, 100], [25, 27, 25], [-27, 9, 17], [24, 200, 200], [32, 31, 31], [62, 40, 41], [1000, 40, 501], [50, 27, -26], [-3, 1, 1], [40, 62, 62], [100, 457, 100], [31, 24, 22], [21, -25, 200], [500, 22, 500], [41, -26, -26], [-5, 34, 1234], [0, 2, 0], [101, 56, 129], [399, 2, 0], [7919, 33, 5212], [61, -100, 50], [73, 0, 15], [101, 17, 0], [-10, 4, 5], [0, 6, 10], [-5, -10, 1234], [1234, 56, 129], [10, -5, -5], [-10, 4, 10], [4, 10, 10], [-9, 4, 5], [-11, 56, 10], [34, -10, 34], [73, 56, 129], [-9, -10, 4], [4, 2, 10], [0, 5, 10], [-9, 5, 5], [10, -4, -5], [1234, 129, 128], [129, 9, 10], [-11, 56, 56], [9, 129, -5], [129, 10, -10], [-9, -10, -10], [10, -6, -5], [-5, 56, -5], [-9, 6, 0], [-8, -9, 6], [101, 129, -5], [34, -10, 50], [49, -100, 50], [34, -10, 51], [1233, 56, 130], [10, 10, 10], [34, -5, -5], [-5, -5, 10], [129, 1234, 1234], [1234, 1234, 5], [-11, 4, 5], [1234, 129, 1234], [-7, 17, 0], [6, 128, 10], [34, -7, 34], [-4, -4, -5], [7919, 33, 7919], [0, -11, 10], [-7, 0, 0], [-5, 129, -5], [56, 56, 129], [10, 129, -5], [-10, -11, -11], [34, 2, 50], [-10, 34, 35], [5, 5212, 1234], [1234, 129, 129], [0, 4, 5], [17, 129, 56], [-9, 61, 0], [-8, 5, 0], [4, -7, 34], [-7, 0, -6], [61, 0, 0], [129, 56, 129], [-10, 56, 10], [49, 49, 17], [6, 6, 6], [129, 1235, 1234], [9, 33, 33], [-5, 34, -5], [-5, -10, -5], [17, -5, -5], [-10, 35, 35], [2, 9, 50], [399, 0, 0], [35, 49, 49], [5, -6, -5], [-7, 8, 9], [399, 2, 2], [1234, 131, 1234], [-5, -5, -5], [-100, -7, 0], [1234, 129, 15], [131, 128, 128], [-4, 34, 49], [-6, -5, -5], [129, 56, -6], [10, 1234, 8], [-10, 5, 5], [4, 5, 5], [17, 5, 5], [-10, 0, 5], [399, 399, 0], [129, 5, 5], [1234, 4, 0], [400, 399, 2], [61, 0, 1], [128, -10, 1234], [-10, 131, 34], [-11, 131, 34], [129, 0, -6], [15, -5, -5], [10, -10, 1234], [49, 48, 5211], [55, 56, 56], [-9, -10, 130], [16, 17, 3], [34, 51, -10], [-4, 10, -10], [-8, 8, 9], [-11, 9, -11], [-10, 33, 33], [-9, 62, 0], [-10, -11, -10], [1233, 399, 74], [-9, 8, 9], [-4, 10, -5], [131, 131, 33], [-8, -9, 17], [55, 56, 55], [6, 17, 2], [-9, 399, 62], [131, -7, 1235], [131, 33, 33], [10, 33, 1234], [-8, -9, 128], [-11, 129, -11], [9, 0, 9], [50, 56, 56], [128, -10, 7919], [-9, -9, 6], [-11, -10, 5], [49, 50, 50], [132, 33, 33], [0, 61, 0], [129, 128, 127], [-7, 8, 8], [131, 51, 51], [-4, 128, 9], [55, 9, 9], [2, 5211, 50], [15, 6, 5], [18, 129, 57], [2, 2, 50], [-9, 6, 5], [17, 5, 4], [16, 33, 18], [4, 35, 5], [73, -10, -10], [34, 35, 5], [17, 2, 17], [7919, 130, 6], [10, 5, 128], [399, 129, 128], [1234, 1234, 1234], [54, 57, 57], [33, 4, 5212], [4, -10, 1234], [61, 57, 1], [1, 5211, 50], [129, 9, 11], [-9, 62, 62], [17, 129, 131], [-10, 8, 10], [127, -9, 33], [62, 0, 0], [4, 5212, 56], [56, -11, 10], [74, -11, -11], [-6, 17, -7], [5, 10, 10], [-100, 0, 0], [3, 0, 15], [-8, -10, 9], [17, 1235, 1235], [-10, 15, -10], [61, -100, -100], [7919, 56, 6], [74, 9, 11], [33, -5, -5], [49, 3, 5211], [-9, 62, 399], [17, 17, -7], [-6, 131, -7], [62, 0, 1], [100, 50, 101], [5, -10, -9], [35, 35, 35], [5, 6, 5], [5, 49, 49], [-4, 49, -4], [-9, -9, 62], [100, 10, -10], [57, 55, 56], [5, 128, 6], [10, -9, 2], [57, 17, 17], [-10, 4, 1233], [-4, 128, -4], [1234, 128, 1234], [62, 56, 62], [7920, 33, 7919], [399, -8, 74], [61, 0, 3], [0, -7, 0], [-1, 6, 10], [72, 0, 34], [-10, 9, 10], [-10, 72, 10], [-4, -6, -6], [130, 10, 1235], [10, 129, -8], [48, 10, -5], [56, 0, 0], [1234, 1234, 129], [72, 17, 0], [1234, 36, -9], [10, -5, 10], [-11, -11, -11], [-8, -9, 16], [5, 5212, 5], [-8, 17, -8], [128, -10, 1233], [34, -10, 52], [72, -9, 0], [48, 4, 1234], [-8, -11, 9], [-10, 50, 10], [-6, 129, -5], [17, 1235, 6], [-10, 1234, -10], [-9, 15, -9], [4, 34, -7], [5, 4, 4], [1, 2, 2], [3, 4, 0], [16, 2, 17], [1235, -5, 1234], [34, 131, 50], [17, 399, -5], [7918, -5, -5], [17, 399, 17], [14, 128, 18], [10, -9, 1234], [2, 48, 15], [33, 5211, 100], [5, 5, 6], [33, 11, 11], [5212, 0, 5211], [-8, 128, 0], [14, 100, 1], [101, 1, -1], [48, 47, 5211], [1235, 16, 35], [5, 128, -1], [14, 128, 14], [7, 399, 6], [7920, 34, -5], [74, 9, 7920], [17, 6, 130], [1, 0, 0], [57, -5, -5], [128, 1234, 128], [5, 7920, 127], [-5, 129, 62], [15, 57, -5], [61, 52, 1], [61, 51, 1], [1235, 1235, 1235], [127, 7, 128], [0, 6, 128], [-7, -9, 17], [-5, 0, 0], [48, 49, -100], [-6, -7, -6], [-5, 17, -5], [1234, 1233, 129], [7, 10, 10], [-10, 8, 130], [128, 50, 128], [0, 72, 5], [34, -4, -5], [51, 131, 50], [14, 399, 128], [1234, 1234, 6], [7919, 0, 14], [-101, -7, 101], [127, -9, 34], [-9, 7, 5], [74, 9, 74], [0, 5211, 5211], [-5, 56, -4], [9, 34, 9], [1233, 57, 130], [100, 2, 17], [-11, 4, 4], [7919, 9, 9], [1234, 7918, 1234], [2, 2, 2], [-10, 8, -10], [72, 0, 0], [129, 8, 129], [101, 5, 56], [-9, 4, 1234], [9, 9, 9], [-8, -9, -8], [16, 3, 16], [17, 0, 0], [-11, 48, 5211], [0, 8, 8], [17, 5, 17], [129, -1, -9], [-100, -9, 6], [1233, 2, 49], [9, 10, 10], [17, 6, 129], [15, -4, -5], [-101, 6, 5], [1233, -4, 5], [7919, -1, 14], [50, 3, 14], [-9, 0, 128], [15, 15, 1234], [62, 0, 62], [0, 0, 0], [-5, 3, 3], [0, 62, 62], [5212, 0, 17], [-5, 0, -1], [61, 62, 62], [129, 0, 0], [1, 2, 1], [8, 10, -10], [34, 5212, 61], [1, 1, 2], [61, 60, 63], [17, 73, 129], [-9, 1234, -9], [-10, 128, 131], [34, 35, 35], [1233, -100, -5], [34, 35, -5], [1234, 100, 1], [10, 9, 9], [5212, 17, 0], [-7, 1, 1], [8, 10, 10], [127, 7, 127], [-101, 74, 5], [32, 33, 32], [18, -7, 0], [1234, -7, 34], [62, -7, -6], [-7, 15, 1], [16, 7, 17], [73, 72, 72], [-6, 0, 4], [61, 0, 61], [10, 52, -5], [61, 60, 61], [-10, 9, -11], [-9, -9, -9], [9, 9, 7919], [-10, -11, 51], [9, 8, 8], [73, -6, -5], [1235, 1233, 5], [10, 1234, 1234], [7919, 7919, 7920], [-9, 128, 7920], [61, 1234, -5], [4, 52, 35], [51, -5, 1234], [4, -10, -11], [-7, 15, 0], [-5, 0, -5], [131, 34, 131], [51, 49, 49], [54, 39, 7919], [60, 52, 1], [34, 35, 34], [11, -8, -9], [15, -4, 5], [-9, 5, 6], [33, 18, 33], [-7, 17, 7919], [2, 0, 0], [127, 100, 100], [-100, 1, 2], [56, 7919, 6], [4, 62, 61], [74, 5, 73], [-7, 2, 2], [74, 9, 73], [399, -10, 0], [100, 3, 5211], [-4, -6, -11], [6, 56, 6], [-7, 400, 8], [73, 5212, 73], [35, 399, 2], [10, 9, 7920], [-5, -11, -5], [59, 52, 1], [-7, 52, 35], [6, 18, 3], [72, 36, 72], [129, 127, 129], [39, -7, 52], [47, 34, 9], [2, 0, 9], [5, 7, 6], [1233, 2, 1233], [131, 130, 10], [35, 6, 5], [-3, 34, 49], [-7, 8, -7], [-6, -7, 34], [18, 132, 50], [5, -1, 5], [1234, 16, 129], [5212, 17, 51], [129, -9, 7919], [-4, -11, -11], [39, 9, 10], [63, -5, 63], [-7, 1234, 1234], [18, 399, -5], [7919, 7919, 33], [35, -6, 129], [34, -5, 34], [63, 35, 399], [8, 9, 8], [-4, 11, -6], [-4, -10, 1234], [129, 7918, -6], [4, 49, 48], [-4, -4, -4], [129, 129, -9], [128, 399, 128], [48, 63, 8], [35, 128, 49], [100, 74, 5211], [-5, 10, -5], [34, 131, 1234], [1234, -9, -9], [-6, -6, -6], [4, 34, 3], [5212, 36, -9], [128, 34, 4], [73, 73, -10], [7, 10, 8], [1233, 14, 1233], [132, 131, 34], [0, 1, 0], [51, 73, 61], [399, -9, 17], [8, 129, 8], [129, -6, -6], [132, 128, 128], [9, 10, -10], [132, 1, -2], [-9, 14, 5], [17, -7, 49], [9, 74, 9], [131, 57, 1233], [52, -1, 5211], [7919, 55, 6], [61, 62, 1], [55, 56, 6], [33, -5, 130], [61, 61, 61], [9, -100, 11], [-10, 10, 10], [49, 4, 1233], [11, -9, 2], [61, -2, 1], [100, 4, 34], [131, 131, 131], [3, 7919, 3], [101, 1234, 1234], [-11, 10, 10], [10, 34, 2], [0, 5, 4], [-6, 5, 5], [34, 52, -10], [-5, 34, 34], [9, 8, 1235], [1232, 100, 1232], [4, 49, 49], [61, -4, 9], [-11, 400, 5], [16, 16, 5], [131, 1232, 1233], [-8, 16, -8], [132, -9, 33], [130, 131, 132], [9, 49, 49], [-10, -11, 10], [33, 128, 49], [-7, 51, 35], [1234, 132, 131], [48, 10, -6], [1233, 5, 1233], [-7, 3, 6], [-5, 12, 17], [4, 0, 4], [34, 0, 4], [72, 0, 15], [34, 1, 34], [34, 0, 50], [2, 0, 399], [7919, 7919, 35], [6, 101, 56], [73, 1, 1], [0, 6, 1], [102, 6, 101], [60, -100, 50], [7919, 7920, 35], [3, 50, 2], [56, 129, 129], [73, 0, 33], [6, 3, 5], [17, 72, 56], [-10, 3, 4], [1, 399, 0], [-1, 15, 73], [17, 15, 17], [399, 2, -100], [3, 60, 2], [35, 0, 10], [33, 5212, 33], [56, 7920, 35], [4, 0, 34], [34, -1, 50], [34, -1, 0], [61, 4, -1], [3, 60, 61], [399, -100, 2], [0, 35, 0], [3, 2, 60], [73, 73, 1], [-1, 50, -1], [50, 34, -1], [0, 10, 10], [2, 101, 56], [-10, 34, 56], [60, -100, -10], [35, 16, 34], [61, 50, 61], [101, 0, 101], [17, 16, 15], [51, 34, 50], [7919, -100, -100], [35, 15, 15], [101, 399, 129], [34, 3, 0], [0, 34, 0], [14, 2, 15], [1234, 10, 1234], [15, -100, 50], [34, 15, 17], [7919, 7920, 7919], [56, 129, 128], [7919, 399, 7919], [7919, -100, 128], [-1, 34, -1], [61, 1234, 7918], [3, 2, 1234], [73, 15, 73], [4, 2, 60], [7919, 7919, 7919], [100, 56, 101], [7919, -100, 50], [35, 33, 35], [1234, -100, 1234], [56, 56, 56], [6, 4, 34], [17, 56, 56], [7920, 33, 5212], [399, 399, 399], [6, 7, 10], [56, 128, 128], [0, -1, 0], [0, -100, 128], [50, 61, 50], [2, 1, 2], [34, 0, 5212], [73, 0, 16], [6, 16, 7], [129, 56, 399], [7918, 61, 61], [2, 0, 1], [50, -10, 50], [16, -100, 129], [0, 399, 0], [72, 5, 15], [-5, 2, 1234], [71, 72, 7], [1234, 34, 1234], [56, 34, 51], [0, 0, 1], [6, 4, 33], [73, 129, 130], [51, -100, 51], [101, -10, 6], [101, 17, -1], [0, -101, 399], [-4, 14, 71], [34, -1, 33], [73, 101, 33], [7919, 73, 34], [-1, -1, -1], [2, 101, -101], [33, 4, 60], [101, 399, -1], [17, -5, 17], [399, -1, 101], [72, 15, 15], [101, 399, 7], [3, 1235, 1234], [0, 5212, 5212], [4, 0, 10], [7917, 1234, 7918], [34, 14, 33], [35, 0, 399], [2, 56, -101], [102, 128, 128], [15, -1, 399], [73, 16, 15], [-100, 0, 129], [35, 399, 6], [17, 34, 101], [2, 1234, -5], [1, 0, 1], [4, 33, 0], [101, 34, 6], [56, -10, 56], [1235, 56, 56], [73, -10, 130], [0, 101, 0], [4, 5, 11], [-100, -100, -100], [34, 33, 6], [4, 61, 61], [73, 73, 73], [15, -1, 15], [-101, 0, 0], [-1, 15, 15], [72, 7, 0], [1234, 56, 51], [35, 33, 34], [1235, 50, 5212], [0, 50, 50], [2, 1, 100], [2, 73, -101], [1, 6, 10], [0, 10, 5], [5, 15, 15], [16, -101, 129], [-1, -1, 61], [3, 60, 3], [102, 102, 0], [399, 0, 399], [34, -1, 5212], [6, 15, 15], [-1, -1, 0], [7917, 1234, 1234], [1233, -100, 1234], [72, 7, 7], [2, 72, -101], [1, 1, 1], [17, 72, -100], [50, 1, 2], [101, -1, 0], [51, 34, -1], [17, -100, 17], [2, -10, 2], [7920, 9, 5], [1234, -2, 50], [-10, 3, 5], [-4, 1235, 2], [15, -2, -1], [72, -1, 50], [-1, 60, -1], [0, 1, 1], [74, -10, 130], [32, 32, 32], [102, 10, 0], [-4, 57, 56], [34, 33, 50], [60, 61, 61], [35, -100, 10], [6, 7, 16], [1235, 2, -1], [-11, 3, 4], [7, 0, 0], [1, 399, 33], [34, 2, 1], [10, 0, 0], [4, -10, 34], [3, 3, 4], [56, 34, -2], [74, 129, 128], [74, 7, 0], [73, 15, 15], [35, 130, -100], [7920, 7920, 7919], [100, -10, 6], [2, 56, 7], [-1, 33, 33], [17, 73, 7], [15, 4, 50], [0, -2, 0], [128, 1, 1], [128, -100, 10], [7, 6, 7], [100, -1, 11], [7920, 33, 0], [102, -1, -1], [0, 5211, 5212], [9, 35, 0], [399, 56, -100], [101, 130, 0], [-10, -10, -10], [6, 15, 5211], [102, 103, 10], [7919, 34, 34], [128, -4, 128], [-1, 15, 0], [34, 5, 4], [71, 74, 6], [61, 128, 1233], [-1, 100, 15], [33, 0, 5212], [35, 3, 34], [5212, 1235, 2], [101, 5212, 33], [34, 16, 17], [-5, -4, 14], [-100, 73, 51], [129, 0, -1], [33, 60, 35], [5212, -2, 5211], [0, 15, 15], [0, 35, -101], [128, 62, 1233], [128, 56, 399], [61, 7918, 7918], [129, 102, 127], [34, 16, 18], [128, -100, 128], [2, 2, 1], [400, 2, 0], [-1, 51, 50], [9, -1, 399], [-10, 4, -10], [-2, -1, -1], [399, 4, 56], [0, 0, 72], [7920, 5212, 7920], [-4, 32, 32], [60, 4, 0], [-100, 1, 129], [2, -10, 127], [73, 7, 0], [1, 2, 3], [3, 2, 2], [-101, 0, 18], [-101, 19, 18], [399, 128, 4], [99, -1, -1], [35, 74, 74], [56, 400, 35], [1, 2, 1234], [3, 17, 4], [2, 1, 1234], [128, 399, 399], [56, 128, 56], [99, -10, -10], [17, 399, 399], [102, 103, 61], [1, 34, 51], [0, 1, 2], [48, 34, 1233], [73, 101, 6], [14, 6, 7], [-2, 7917, 4], [-99, 103, 129], [101, 5, 15], [5212, 34, 51], [5212, 33, 130], [71, 15, 15], [71, 74, -11], [0, 5212, 399], [102, 73, 0], [34, 14, 7917], [-1, 99, 15], [1233, 1, 1], [1, 100, 100], [129, 15, 14], [102, 129, 102], [3, 50, 4], [399, 62, 2], [5211, 4, 5], [72, 71, 7], [6, -1, 18], [0, 7, 0], [399, -100, 399], [3, 61, 7918], [48, 130, 5210], [61, 50, 60], [60, -100, -100], [57, 2, 3], [73, 0, 131], [102, -1, 1234], [103, 34, 129], [-5, 128, -5], [15, 15, 4], [3, 5, 6], [128, 56, 128], [35, 17, 16], [51, 56, 56], [-99, -99, 60], [48, 1, 100], [7921, 7920, 7919], [7919, 4, 10], [3, 17, 103], [1234, 2, 1], [50, 4, 50], [131, 0, 6], [5, 0, 4], [63, 62, 50], [5212, 56, 7920], [-10, 34, -10], [60, 60, -100], [5, 35, 16], [15, -1, 17], [34, 1235, 3], [11, 5211, -2], [400, -1, 100], [100, 11, 11], [50, 399, 399], [5211, 5212, 33], [5, 60, 5], [34, 399, 399], [129, 102, 128], [-1, 100, -1], [60, -4, 60], [60, 62, 61], [131, 131, 0], [-100, -1, 16], [101, 0, 0], [7920, -99, 7920], [1235, 52, 5212], [-4, 14, 13], [5212, 6, 5211], [1235, 56, 1235], [34, 16, 20], [50, 9, 9], [72, 1235, 50], [15, 6, 0], [9, 35, -1], [0, 2, 1], [15, 7917, 7917], [1234, 1233, 1234], [57, 15, 32], [17, 17, 16], [15, 14, 399], [129, 129, 56], [61, 127, 1233], [7919, 7918, 7919], [129, 10, 10], [33, 33, 34], [7, 72, 7919], [57, -10, 6], [-10, -4, -11], [103, -1, 15], [1234, 50, 1234], [101, 101, 6], [0, 2, 2], [0, 2, 1234], [2, 6, 1], [74, 73, 6], [-99, 0, 129], [18, 16, 17], [73, 73, 5], [32, 34, 32], [34, 51, 51], [399, 5, 128], [71, 5212, 6], [127, 129, 129], [34, 131, -1]]
    results = [34, 5, 33, 3, -1, 583, 129, 1234, 0, 2, 1, 1000, 1, 25, 123, 100, 5, -5, 3, 20, 200, 20, 99, 100, 500, 62, 25, 500, 9, 100, 122, 123, 3, 100, 100, 200, 20, 37, 500, 99, 501, 100, 1, 501, -26, 200, 122, 200, 1, -26, 99, 3, 18, 100, 99, 0, 500, 101, 3, 500, 3, 499, -26, 99, 26, 62, 9, 199, 22, -3, 32, 22, 200, 200, 5, 3, 37, 113, -4, 455, 98, 123, 200, 99, 5, 100, 122, 3, 100, 100, 37, 9, 499, -26, 1000, 100, 25, 17, 200, 31, 41, 501, -26, 1, 62, 100, 24, 200, 500, -26, 1234, 0, 56, 0, 33, -100, 0, 17, 5, 10, 1234, 129, -5, 10, 10, 5, 10, 34, 56, 4, 10, 10, 5, -5, 128, 10, 56, -5, -10, -10, -5, -5, 0, 6, 129, 50, 50, 51, 130, 10, -5, 10, 1234, 5, 5, 1234, 0, 10, 34, -5, 33, 10, 0, -5, 129, -5, -11, 50, 35, 5212, 129, 5, 129, 0, 0, 34, -6, 0, 129, 10, 17, 6, 1234, 33, -5, -5, -5, 35, 9, 0, 49, -6, 9, 2, 1234, -5, 0, 15, 128, 49, -5, -6, 8, 5, 5, 5, 5, 0, 5, 0, 2, 0, 1234, 34, 34, -6, -5, 1234, 5211, 56, 130, 3, -10, -10, 9, -11, 33, 0, -10, 74, 9, -5, 131, 17, 55, 2, 62, -7, 33, 1234, 128, -11, 9, 56, 7919, 6, 5, 50, 33, 0, 127, 8, 51, 9, 9, 5211, 5, 57, 2, 5, 5, 18, 5, -10, 5, 2, 130, 128, 128, 1234, 57, 5212, 1234, 57, 50, 11, 62, 129, 10, -9, 0, 56, 10, -11, -7, 10, 0, 0, 9, 1235, -10, -100, 56, 11, -5, 5211, 399, 17, -7, 1, 101, -10, 35, 6, 49, -4, 62, -10, 56, 128, 2, 17, 1233, -4, 1234, 62, 7919, 74, 0, 0, 10, 34, 10, 10, -6, 1235, -8, -5, 0, 129, 0, -9, 10, -11, 16, 5212, -8, 1233, 52, 0, 1234, 9, 10, -5, 1235, -10, -9, -7, 4, 2, 4, 17, 1234, 50, 399, -5, 399, 18, 1234, 48, 100, 5, 11, 5211, 0, 1, 1, 5211, 35, 128, 14, 399, -5, 7920, 6, 0, -5, 128, 7920, 62, -5, 52, 51, 1235, 7, 128, 17, 0, -100, -6, -5, 129, 10, 130, 128, 5, -5, 50, 128, 6, 0, 101, -9, 5, 74, 5211, -4, 9, 130, 17, 4, 9, 1234, 2, -10, 0, 129, 5, 1234, 9, -8, 16, 0, 5211, 8, 5, -9, 6, 49, 10, 6, -5, 5, 5, -1, 14, 128, 1234, 62, 0, 3, 62, 17, -1, 62, 0, 1, -10, 61, 2, 60, 73, -9, 131, 35, -5, -5, 1, 9, 0, 1, 10, 7, 5, 32, 0, 34, -6, 1, 17, 72, 4, 0, -5, 60, -11, -9, 7919, 51, 8, -6, 5, 1234, 7919, 7920, 1234, 35, 1234, -11, 0, -5, 34, 49, 7919, 1, 34, -8, 5, 6, 33, 7919, 0, 100, 2, 6, 61, 73, 2, 73, 0, 5211, -11, 6, 8, 5212, 2, 7920, -5, 52, 35, 3, 72, 129, 52, 34, 0, 7, 1233, 130, 5, 49, -7, 34, 50, -1, 129, 51, 7919, -11, 10, 63, 1234, -5, 7919, 129, 34, 399, 8, -6, 1234, -6, 48, -4, -9, 128, 8, 49, 5211, -5, 1234, -9, -6, 3, -9, 4, 73, 10, 1233, 34, 0, 61, 17, 8, -6, 128, -10, -2, 5, -7, 9, 57, 5211, 55, 62, 6, 130, 61, 11, 10, 1233, -9, -2, 34, 131, 7919, 1234, 10, 2, 4, 5, -10, 34, 1235, 1232, 49, -4, 5, 5, 1232, -8, 33, 132, 49, 10, 49, 35, 131, -6, 1233, 6, 17, 4, 4, 15, 34, 50, 0, 7919, 56, 1, 1, 101, 50, 7920, 50, 129, 0, 5, 72, 4, 0, 73, 15, -100, 60, 10, 33, 35, 34, 50, 0, 4, 60, 2, 0, 2, 73, -1, -1, 10, 101, 56, -10, 34, 50, 0, 16, 50, -100, 15, 399, 0, 0, 15, 1234, 50, 17, 7920, 128, 399, -100, -1, 1234, 2, 15, 60, 7919, 101, -100, 35, 1234, 56, 34, 56, 5212, 399, 10, 128, 0, 128, 50, 1, 5212, 0, 7, 399, 61, 0, 50, 129, 0, 15, 1234, 72, 1234, 51, 1, 33, 129, 51, -10, 17, 399, 71, 33, 101, 73, -1, 101, 60, 399, -5, 101, 15, 399, 1235, 5212, 10, 7918, 33, 399, 56, 128, 399, 16, 129, 6, 34, 1234, 1, 0, 34, 56, 56, -10, 0, 11, -100, 6, 61, 73, 15, 0, 15, 0, 51, 34, 5212, 50, 1, 73, 10, 5, 15, 129, 61, 60, 0, 399, 5212, 15, 0, 1234, 1234, 7, 72, 1, 72, 2, -1, -1, -100, -10, 5, 50, 5, 2, -1, 50, -1, 1, 130, 32, 0, 56, 50, 61, 10, 16, -1, 4, 0, 33, 1, 0, 34, 3, -2, 128, 0, 15, -100, 7919, 6, 56, 33, 73, 50, 0, 1, 10, 6, 11, 0, -1, 5212, 0, -100, 130, -10, 5211, 10, 34, 128, 0, 4, 74, 128, 15, 5212, 34, 2, 5212, 17, 14, 51, -1, 35, 5211, 15, -101, 1233, 399, 7918, 127, 18, 128, 2, 0, 50, 399, -10, -1, 56, 72, 7920, 32, 0, 129, -10, 7, 3, 2, 18, 18, 4, -1, 74, 35, 1234, 17, 1, 399, 56, -10, 399, 61, 51, 2, 1233, 101, 7, 4, 129, 5, 51, 130, 15, 74, 399, 0, 7917, 15, 1, 100, 14, 102, 50, 2, 5, 7, 18, 0, 399, 61, 5210, 50, -100, 3, 0, 1234, 34, -5, 4, 5, 128, 16, 56, 60, 100, 7919, 4, 17, 1, 50, 0, 0, 50, 7920, -10, -100, 35, 17, 3, 5211, 100, 11, 399, 33, 60, 399, 128, -1, 60, 61, 131, 16, 0, 7920, 5212, 13, 5211, 1235, 20, 9, 50, 0, -1, 1, 7917, 1234, 32, 17, 399, 56, 127, 7918, 10, 34, 72, 6, -11, -1, 1234, 101, 2, 1234, 6, 6, 129, 17, 73, 32, 51, 128, 5212, 129, -1]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(x_or_y)