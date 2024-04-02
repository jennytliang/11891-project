def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x <= 0 or y <= 0 or x > y:
        return -1
    if x % 2 != 0:
        x += 1
    if y % 2 != 0:
        y -= 1
    if x > y:
        return -1
    if x == y:
        return x
    if (y - x) % 2 == 0:
        return (y - x) // 2 + x
    else:
        return -1




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
    inputs = [[12, 15], [13, 12], [33, 12354], [5234, 5233], [6, 29], [27, 10], [7, 7], [546, 546], [20, 30], [30, 30], [50, 60], [12, 14], [10, 12], [3, 5], [6, 20], [100, 200], [1, 2], [30, 35], [100, 6], [6, 30], [101, 6], [21, 3], [14, 14], [100, 100], [100, 35], [35, 101], [60, 60], [35, 35], [5, 6], [2, 35], [60, 50], [28, 1], [35, 200], [200, 5], [60, 6], [20, 20], [30, 6], [28, 35], [200, 200], [20, 36], [1, 6], [30, 1], [21, 5], [35, 199], [11, 14], [201, 201], [6, 5], [13, 10], [12, 16], [199, 12], [14, 13], [1, 1], [60, 11], [13, 35], [100, 30], [12, 12], [15, 14], [5, 5], [36, 29], [12, 11], [100, 15], [27, 28], [200, 201], [11, 201], [10, 11], [100, 13], [15, 29], [200, 101], [3, 3], [101, 15], [36, 35], [34, 101], [101, 101], [1, 14], [30, 21], [12, 3], [10, 4], [2, 2], [21, 20], [30, 50], [200, 199], [3, 101], [6, 15], [50, 59], [11, 11], [12, 13], [29, 35], [30, 201], [99, 5], [60, 21], [20, 5], [6, 35], [6, 36], [100, 98], [5, 200], [31, 50], [60, 59], [59, 21], [101, 34], [1, 15], [201, 1], [35, 50], [50, 3], [10, 35], [14, 30], [201, 200], [201, 199], [61, 60], [23, 27], [8, 10], [10, 17], [999, 998], [7, 20], [17, 21], [31, 99], [1000, 2000], [2, 20], [24, 27], [17, 24], [18, 31], [998, 998], [31, 1], [20, 21], [1, 7], [23, 100], [100, 23], [101, 100], [18, 32], [99, 99], [101, 18], [998, 31], [7, 24], [2000, 21], [19, 20], [1000, 2], [2, 3], [8, 1], [31, 999], [1, 23], [18, 33], [10, 2], [100, 998], [10, 20], [31, 20], [8, 24], [24, 24], [32, 1], [18, 18], [20, 19], [2, 100], [99, 31], [100, 1000], [1, 19], [31, 31], [32, 7], [20, 27], [2, 31], [32, 6], [10, 10], [2, 5], [2000, 998], [24, 33], [17, 17], [8, 9], [33, 2000], [20, 31], [1, 8], [102, 22], [1000, 24], [9, 10], [18, 6], [24, 99], [10, 101], [100, 10], [24, 7], [2, 17], [1000, 22], [20, 22], [23, 21], [9, 24], [32, 3], [9, 5], [3, 1], [2000, 2000], [22, 32], [8, 7], [3, 2], [31, 32], [27, 6], [7, 2000], [27, 101], [20, 7], [2, 1], [17, 33], [10, 24], [33, 33], [100, 31], [23, 18], [99, 998], [23, 31], [21, 21], [99, 32], [1000, 10], [1000, 1], [100, 22], [23, 6], [2, 21], [18, 8], [17, 32], [2, 28], [33, 32], [4, 7], [23, 23], [2001, 2000], [22, 99], [1000, 28], [1, 2001], [22, 4], [8, 2], [11, 10], [8, 8], [32, 22], [1999, 2000], [23, 32], [5, 24], [17, 102], [32, 32], [7, 18], [29, 28], [99, 10], [22, 31], [2, 4], [99, 100], [7, 1], [6, 1999], [10, 25], [28, 28], [1000, 2001], [17, 7], [1999, 28], [27, 27], [21, 19], [998, 100], [32, 33], [24, 10], [33, 24], [99, 6], [998, 32], [32, 34], [25, 20], [33, 3], [998, 1999], [24, 28], [24, 1999], [31, 18], [22, 17], [99, 3], [11, 5], [999, 102], [4, 2], [23, 24], [24, 9], [8, 998], [99, 20], [11, 9], [32, 11], [20, 1999], [19, 24], [1000, 6], [1999, 1], [19, 19], [29, 1], [5, 31], [1001, 18], [29, 18], [8, 20], [4, 4], [2000, 99], [32, 18], [1, 18], [10, 1], [6, 7], [6, 34], [26, 25], [24, 25], [9, 9], [32, 1001], [28, 2], [9, 20], [4, 27], [1, 10], [2000, 16], [20, 32], [1999, 1999], [102, 10], [999, 18], [9, 8], [5, 10], [9, 6], [999, 999], [2000, 101], [10, 29], [22, 8], [16, 6], [10, 32], [17, 34], [10, 28], [7, 102], [1001, 1001], [25, 33], [101, 20], [27, 100], [23, 101], [18, 17], [10, 5], [22, 21], [21, 998], [22, 22], [2, 16], [999, 24], [18, 21], [1000, 1000], [22, 10], [99, 999], [7, 6], [99, 26], [11, 102], [998, 999], [1, 99], [102, 20], [6, 1000], [17, 1000], [103, 7], [1999, 21], [1999, 997], [7, 9], [1003, 1002], [28, 998], [2, 1002], [19, 31], [32, 10], [1, 999], [7, 3], [31, 16], [7, 99], [7, 17], [99, 98], [100, 21], [100, 11], [20, 25], [9, 99], [25, 100], [2, 32], [100, 101], [33, 2001], [98, 32], [2001, 2001], [6, 21], [24, 6], [4, 20], [1003, 1001], [100, 2000], [1999, 1000], [30, 7], [103, 998], [999, 99], [34, 25], [19, 3], [1002, 1003], [34, 4], [17, 99], [23, 1001], [1, 3], [22, 23], [7, 2], [1999, 19], [3, 32], [6, 18], [23, 997], [17, 29], [27, 62], [26, 28], [1001, 7], [22, 5], [997, 998], [29, 100], [22, 100], [22, 6], [62, 62], [34, 34], [32, 21], [29, 6], [16, 3], [998, 10], [1999, 99], [27, 7], [17, 98], [34, 5], [30, 99], [17, 30], [104, 7], [100, 62], [28, 27], [100, 3], [4, 998], [3, 21], [10, 98], [1002, 1999], [98, 21], [4, 10], [25, 17], [24, 23], [2000, 2001], [1003, 998], [998, 997], [32, 1002], [28, 1001], [22, 1], [24, 26], [27, 104], [103, 1001], [11, 12], [6, 8], [101, 32], [1000, 999], [10, 21], [999, 28], [100, 99], [34, 33], [5, 20], [20, 34], [33, 1002], [30, 3], [1000, 29], [12, 29], [4, 24], [20, 102], [29, 98], [70, 70], [18, 62], [18, 19], [5, 16], [1002, 1002], [11, 93], [18, 3], [98, 7], [29, 29], [16, 17], [34, 2], [9, 93], [30, 103], [1001, 70], [23, 1999], [1001, 998], [26, 99], [21, 18], [998, 8], [21, 22], [23, 1], [1003, 1003], [23, 998], [2000, 3], [25, 28], [2, 27], [102, 102], [1004, 1003], [103, 99], [70, 100], [32, 104], [1003, 7], [5, 3], [18, 98], [25, 27], [22, 1000], [103, 103], [1000, 1001], [1002, 1001], [4, 31], [102, 101], [2000, 1004], [21, 8], [99, 70], [3, 1002], [20, 8], [1003, 1004], [33, 30], [6, 6], [25, 9], [31, 4], [70, 5], [31, 28], [19, 33], [3, 4], [5, 9], [1999, 1004], [104, 29], [62, 998], [25, 99], [21, 1999], [33, 34], [997, 4], [102, 998], [1000, 19], [23, 10], [1004, 1004], [997, 2001], [998, 6], [30, 29], [10, 998], [4, 9], [70, 32], [27, 20], [102, 21], [8, 3], [19, 4], [33, 6], [12, 23], [1, 17], [29, 99], [102, 99], [24, 29], [7, 22], [28, 12], [1001, 99], [22, 71], [3, 27], [999, 23], [7, 10], [18, 1], [63, 102], [25, 29], [103, 6], [8, 6], [28, 25], [99, 12], [10, 27], [32, 30], [21, 30], [996, 2001], [104, 27], [28, 17], [999, 1000], [103, 104], [16, 34], [11, 8], [2000, 24], [16, 35], [32, 31], [26, 23], [27, 26], [9, 21], [18, 20], [29, 17], [2, 33], [32, 23], [22, 9], [17, 5], [10, 22], [34, 20], [9, 2], [11, 998], [35, 1], [23, 102], [22, 2001], [2000, 23], [24, 30], [2000, 62], [100, 63], [996, 4], [18, 4], [101, 71], [1003, 20], [70, 21], [10, 3], [72, 71], [27, 1002], [31, 17], [1998, 1999], [62, 21], [71, 71], [2001, 21], [9, 104], [1004, 18], [18, 2], [7, 1000], [19, 32], [17, 2000], [104, 103], [27, 18], [21, 31], [1, 1004], [1999, 98], [21, 7], [30, 17], [1998, 1998], [101, 102], [17, 8], [29, 12], [2001, 16], [1000000, 1000001], [10, 23], [27, 23], [2000, 999], [1, 21], [8, 23], [30, 23], [10, 16], [23, 8], [27, 17], [2000, 17], [7, 31], [7, 27], [999, 30], [2000, 100], [30, 2], [21, 10], [999, 2000], [100, 2], [10, 18], [99, 2], [99, 23], [22, 2000], [1000, 9], [10, 2001], [30, 22], [1000, 17], [999, 17], [999, 100], [9, 2000], [999, 2001], [99, 1000], [31, 21], [2001, 20], [27, 2], [23, 9], [29, 23], [1999, 29], [27, 2001], [5, 23], [10, 100], [101, 2000], [999, 1], [99, 7], [23, 2001], [9, 16], [5, 2], [10, 9], [30, 16], [27, 2000], [17, 2001], [998, 1000], [22, 18], [1999, 999], [10, 1999], [29, 999], [1999, 31], [99, 16], [16, 10], [11, 30], [11, 2], [10, 31], [999, 9], [99, 1], [22, 30], [31, 7], [23, 17], [29, 101], [2002, 2002], [999, 2002], [2000, 18], [16, 21], [99, 17], [10, 7], [21, 16], [23, 7], [1999, 8], [999, 20], [8, 22], [26, 27], [1000, 16], [21, 27], [17, 22], [999, 21], [15, 21], [26, 7], [10, 2000], [11, 100], [21, 23], [5, 18], [9, 1999], [18, 7], [99, 101], [44, 1999], [44, 43], [16, 16], [30, 10], [2000, 7], [11, 99], [99, 24], [2000, 1], [11, 31], [28, 2001], [999, 10], [1001, 24], [29, 22], [2000, 20], [7, 999], [2001, 100], [99, 30], [18, 43], [6, 17], [24, 2001], [102, 30], [11, 22], [999, 5], [99, 1999], [20, 1001], [19, 7], [20, 2000], [7, 8], [2001, 1001], [98, 99], [7, 19], [102, 15], [11, 21], [19, 1001], [98, 1000], [26, 100], [999, 19], [21, 1000], [2002, 31], [23, 99], [26, 2000], [98, 17], [2002, 30], [23, 1002], [2001, 9], [102, 999], [9, 11], [1999, 11], [31, 8], [29, 997], [100, 102], [23, 98], [1999, 17], [5, 102], [28, 8], [24, 17], [29, 5], [15, 15], [1001, 11], [999, 26], [9, 22], [44, 9], [2002, 997], [2000, 10], [7, 23], [18, 2001], [5, 1999], [2000, 5], [101, 10], [2003, 11], [31, 6], [30, 5], [2001, 7], [28, 30], [1999, 30], [24, 5], [1001, 23], [998, 1], [9, 2002], [15, 10], [16, 9], [102, 24], [998, 29], [2002, 2000], [21, 999], [44, 6], [25, 2003], [10, 999], [102, 100], [1001, 100], [15, 2], [19, 22], [2002, 10], [23, 15], [8, 2001], [25, 5], [2001, 2002], [27, 30], [26, 101], [1001, 22], [5, 21], [99, 21], [28, 29], [6, 2002], [2000, 1000], [8, 27], [31, 1001], [32, 5], [2004, 2003], [15, 16], [18, 16], [10, 15], [1, 30], [1, 1001], [2001, 17], [2002, 2001], [99, 1002], [29, 2001], [30, 15], [6, 1001], [20, 26], [30, 100], [1002, 22], [10, 1998], [31, 10], [998, 101], [28, 31], [26, 102], [1, 997], [23, 22], [29, 30], [101, 21], [7, 32], [998, 23], [2003, 7], [43, 1], [1001, 20], [24, 2003], [17, 999], [1001, 30], [1998, 999], [22, 27], [14, 15], [1998, 9], [9, 2001], [998, 28], [24, 20], [1, 2000], [22, 999], [96, 99], [999, 7], [99, 25], [6, 26], [1001, 101], [1, 29], [16, 1], [100, 5], [19, 1999], [22, 1999], [25, 24], [3, 998], [44, 99], [2000, 9], [1998, 31], [1999, 27], [31, 14], [15, 999], [27, 29], [1999, 101], [24, 104], [998, 9], [997, 23], [26, 6], [997, 101], [4, 22], [2004, 31], [31, 30], [1000, 23], [24, 16], [98, 98], [28, 16], [100, 19], [44, 7], [16, 5], [26, 999], [100, 1002], [997, 22], [16, 2001], [2002, 2003], [1998, 2000], [16, 15], [98, 1001], [29, 2003], [21, 100], [2000, 1999], [1000, 1999], [1999, 102], [29, 1002], [6, 99], [103, 102], [100, 1001], [31, 24], [25, 26], [21, 6], [8, 26], [26, 5], [1000, 998], [44, 44], [2004, 8], [9, 7], [20, 16], [103, 27], [102, 18], [998, 2001], [101, 104], [4, 102], [24, 2004], [6, 4], [2001, 104], [17, 28], [100, 43], [1001, 2004], [1998, 43], [2002, 999], [43, 30], [102, 9], [2003, 5], [1002, 102], [1999, 998], [2003, 10], [14, 2], [32, 2001], [1000, 30], [8, 103], [999, 1999], [43, 43], [96, 96], [16, 2002], [7, 2002], [23, 34], [22, 11], [5, 15], [26, 26], [8, 5], [96, 4], [15, 20], [12, 8], [2, 999], [21, 2000], [20, 98], [1, 2004], [997, 997], [21, 102], [18, 9], [14, 998], [28, 2003], [23, 20], [2, 22]]
    results = [14, -1, 12354, -1, 28, -1, -1, 546, 30, 30, 60, 14, 12, 4, 20, 200, 2, 34, -1, 30, -1, -1, 14, 100, -1, 100, 60, -1, 6, 34, -1, -1, 200, -1, -1, 20, -1, 34, 200, 36, 6, -1, -1, 198, 14, -1, -1, -1, 16, -1, -1, -1, -1, 34, -1, 12, -1, -1, -1, -1, -1, 28, 200, 200, 10, -1, 28, -1, -1, -1, -1, 100, -1, 14, -1, -1, -1, 2, -1, 50, -1, 100, 14, 58, -1, 12, 34, 200, -1, -1, -1, 34, 36, -1, 200, 50, -1, -1, -1, 14, -1, 50, -1, 34, 30, -1, -1, -1, 26, 10, 16, -1, 20, 20, 98, 2000, 20, 26, 24, 30, 998, -1, 20, 6, 100, -1, -1, 32, -1, -1, -1, 24, -1, 20, -1, 2, -1, 998, 22, 32, -1, 998, 20, -1, 24, 24, -1, 18, -1, 100, -1, 1000, 18, -1, -1, 26, 30, -1, 10, 4, -1, 32, -1, 8, 2000, 30, 8, -1, -1, 10, -1, 98, 100, -1, -1, 16, -1, 22, -1, 24, -1, -1, -1, 2000, 32, -1, -1, 32, -1, 2000, 100, -1, -1, 32, 24, -1, -1, -1, 998, 30, -1, -1, -1, -1, -1, -1, 20, -1, 32, 28, -1, 6, -1, -1, 98, -1, 2000, -1, -1, -1, 8, -1, 2000, 32, 24, 102, 32, 18, -1, -1, 30, 4, 100, -1, 1998, 24, 28, 2000, -1, -1, -1, -1, -1, 32, -1, -1, -1, -1, 34, -1, -1, 1998, 28, 1998, -1, -1, -1, -1, -1, -1, 24, -1, 998, -1, -1, -1, 1998, 24, -1, -1, -1, -1, 30, -1, -1, 20, 4, -1, -1, 18, -1, 6, 34, -1, 24, -1, 1000, -1, 20, 26, 10, -1, 32, -1, -1, -1, -1, 10, -1, -1, -1, 28, -1, -1, 32, 34, 28, 102, -1, 32, -1, 100, 100, -1, -1, -1, 998, 22, 16, -1, 20, 1000, -1, 998, -1, -1, 102, 998, 98, -1, 1000, 1000, -1, -1, -1, 8, -1, 998, 1002, 30, -1, 998, -1, -1, 98, 16, -1, -1, -1, 24, 98, 100, 32, 100, 2000, -1, -1, 20, -1, 20, -1, 2000, -1, -1, 998, -1, -1, -1, 1002, -1, 98, 1000, 2, 22, -1, -1, 32, 18, 996, 28, 62, 28, -1, -1, 998, 100, 100, -1, 62, 34, -1, -1, -1, -1, -1, -1, 98, -1, 98, 30, -1, -1, -1, -1, 998, 20, 98, 1998, -1, 10, -1, -1, 2000, -1, -1, 1002, 1000, -1, 26, 104, 1000, 12, 8, -1, -1, 20, -1, -1, -1, 20, 34, 1002, -1, -1, 28, 24, 102, 98, 70, 62, 18, 16, 1002, 92, -1, -1, -1, 16, -1, 92, 102, -1, 1998, -1, 98, -1, -1, 22, -1, -1, 998, -1, 28, 26, 102, -1, -1, 100, 104, -1, -1, 98, 26, 1000, -1, 1000, -1, 30, -1, -1, -1, -1, 1002, -1, 1004, -1, 6, -1, -1, -1, -1, 32, 4, 8, -1, -1, 998, 98, 1998, 34, -1, 998, -1, -1, 1004, 2000, -1, -1, 998, 8, -1, -1, -1, -1, -1, -1, 22, 16, 98, -1, 28, 22, -1, -1, 70, 26, -1, 10, -1, 102, 28, -1, -1, -1, -1, 26, -1, 30, 2000, -1, -1, 1000, 104, 34, -1, -1, 34, -1, -1, -1, 20, 20, -1, 32, -1, -1, -1, 22, -1, -1, 998, -1, 102, 2000, -1, 30, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1002, -1, 1998, -1, -1, -1, 104, -1, -1, 1000, 32, 2000, -1, -1, 30, 1004, -1, -1, -1, 1998, 102, -1, -1, -1, 1000000, 22, -1, -1, 20, 22, -1, 16, -1, -1, -1, 30, 26, -1, -1, -1, -1, 2000, -1, 18, -1, -1, 2000, -1, 2000, -1, -1, -1, -1, 2000, 2000, 1000, -1, -1, -1, -1, -1, -1, 2000, 22, 100, 2000, -1, -1, 2000, 16, -1, -1, -1, 2000, 2000, 1000, -1, -1, 1998, 998, -1, -1, -1, 30, -1, 30, -1, -1, 30, -1, -1, 100, 2002, 2002, -1, 20, -1, -1, -1, -1, -1, -1, 22, 26, -1, 26, 22, -1, 20, -1, 2000, 100, 22, 18, 1998, -1, 100, 1998, -1, 16, -1, -1, 98, -1, -1, 30, 2000, -1, -1, -1, -1, 998, -1, -1, 42, 16, 2000, -1, 22, -1, 1998, 1000, -1, 2000, 8, -1, 98, 18, -1, 20, 1000, 1000, 100, -1, 1000, -1, 98, 2000, -1, -1, 1002, -1, 998, 10, -1, -1, 996, 102, 98, -1, 102, -1, -1, -1, -1, -1, -1, 22, -1, -1, -1, 22, 2000, 1998, -1, -1, -1, -1, -1, -1, 30, -1, -1, -1, -1, 2002, -1, -1, -1, -1, -1, 998, -1, 2002, 998, -1, -1, -1, 22, -1, -1, 2000, -1, 2002, 30, 100, -1, 20, -1, 28, 2002, -1, 26, 1000, -1, -1, 16, -1, 14, 30, 1000, -1, -1, 1002, 2000, -1, 1000, 26, 100, -1, 1998, -1, -1, 30, 102, 996, -1, 30, -1, 32, -1, -1, -1, -1, 2002, 998, -1, -1, 26, 14, -1, 2000, -1, -1, 2000, 998, 98, -1, -1, 26, -1, 28, -1, -1, 1998, 1998, -1, 998, 98, -1, -1, -1, -1, 998, 28, -1, 104, -1, -1, -1, -1, 22, -1, -1, -1, -1, 98, -1, -1, -1, -1, 998, 1002, -1, 2000, 2002, 2000, -1, 1000, 2002, 100, -1, 1998, -1, 1002, 98, -1, 1000, -1, 26, -1, 26, -1, -1, 44, -1, -1, -1, -1, -1, 2000, 104, 102, 2004, -1, -1, 28, -1, 2004, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2000, -1, 102, 1998, -1, 96, 2002, 2002, 34, -1, 14, 26, -1, -1, 20, -1, 998, 2000, 98, 2004, -1, 102, -1, 998, 2002, -1, 22]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(choose_num)