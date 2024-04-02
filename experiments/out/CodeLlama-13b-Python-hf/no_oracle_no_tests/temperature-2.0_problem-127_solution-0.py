def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """

    def is_prime(number):
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    if interval1[0] > interval1[1] or interval2[0] > interval2[1]:
        return "NO"

    if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
        return "NO"

    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if is_prime(end - start + 1):
        return "YES"

    return "NO"




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
    inputs = [[[1, 2], [2, 3]], [[-1, 1], [0, 4]], [[-3, -1], [-5, 5]], [[-2, 2], [-4, 0]], [[-11, 2], [-1, -1]], [[1, 2], [3, 5]], [[1, 2], [1, 2]], [[-2, -2], [-3, -2]], [[0, 0], [0, 1]], [[10, 20], [15, 25]], [[-15, 15], [-10, 10]], [[0, 5], [6, 10]], [[5, 10], [1, 7]], [[11, 11], [11, 11]], [[1, 5], [3, 7]], [[-6, -2], [-1, 1]], [[7, 13], [10, 23]], [[-10, 0], [-2, 2]], [[-6, -2], [-6, -2]], [[6, 6], [6, 6]], [[0, 1], [0, 0]], [[3, 7], [3, 7]], [[7, 12], [10, 23]], [[-6, -2], [-1, 0]], [[1, 5], [1, 5]], [[5, 6], [5, 6]], [[5, 5], [5, 5]], [[0, 0], [0, 0]], [[3, 13], [3, 13]], [[-2, -2], [-2, -2]], [[2, 3], [2, 3]], [[10, 23], [10, 23]], [[-15, 20], [-15, 20]], [[10, 20], [10, 20]], [[5, 11], [1, 7]], [[7, 12], [7, 12]], [[5, 10], [-1, 7]], [[2, 5], [3, 7]], [[0, 3], [0, 0]], [[5, 10], [5, 10]], [[-10, 0], [-10, 0]], [[2, 2], [2, 2]], [[-15, 12], [-10, 10]], [[-2, 7], [-2, 7]], [[-15, 15], [-15, 15]], [[-10, 10], [-10, 10]], [[11, 15], [11, 15]], [[-15, 6], [-15, 6]], [[-15, 1], [-15, 1]], [[12, 12], [12, 12]], [[-10, 1], [-2, 2]], [[12, 13], [12, 13]], [[1, 1], [1, 1]], [[2, 5], [2, 5]], [[-10, 1], [-10, 1]], [[7, 13], [9, 10]], [[10, 15], [10, 15]], [[6, 10], [6, 10]], [[1, 6], [3, 7]], [[-10, -1], [-10, -1]], [[2, 13], [2, 13]], [[5, 9], [5, 9]], [[10, 21], [10, 21]], [[15, 25], [15, 25]], [[10, 10], [10, 10]], [[-15, 12], [-15, 12]], [[7, 13], [3, 10]], [[1, 5], [-1, 7]], [[-1, 1], [-1, 1]], [[-7, -2], [-7, -2]], [[4, 10], [4, 10]], [[-1, 0], [-1, 0]], [[9, 23], [9, 23]], [[0, 5], [9, 10]], [[2, 7], [2, 7]], [[6, 7], [6, 7]], [[-1, -1], [-1, -1]], [[23, 23], [23, 23]], [[9, 9], [9, 9]], [[1, 7], [1, 7]], [[10, 11], [10, 11]], [[7, 13], [7, 13]], [[0, 5], [0, 5]], [[0, 2], [0, 2]], [[8, 8], [8, 8]], [[-15, 10], [-15, 10]], [[-7, 5], [-7, 5]], [[5, 10], [-1, 6]], [[2, 12], [2, 12]], [[-15, -10], [-15, -10]], [[-7, 4], [-7, 4]], [[-7, 10], [-7, 10]], [[19, 23], [19, 23]], [[0, 1], [0, 1]], [[-10, 10], [-15, 15]], [[2, 4], [2, 4]], [[-12, 2], [-12, 2]], [[9, 10], [9, 10]], [[15, 15], [-10, -10]], [[-15, 9], [-15, 9]], [[4, 10], [-1, 7]], [[-11, 10], [-15, 15]], [[-11, 3], [-11, 3]], [[1, 12], [1, 12]], [[5, 23], [5, 23]], [[1, 6], [1, 6]], [[0, 5], [3, 10]], [[-10, 10], [-20, 20]], [[-100, 50], [25, 150]], [[-3, 5], [-9, -2]], [[-7, -5], [0, 5]], [[-1000, -999], [-1000, -999]], [[1000000000, 1000000001], [1000000001, 1000000002]], [[-999999999, 1000000000], [-1000000000, 1000000001]], [[7, 11], [13, 19]], [[100000007, 100000009], [100000009, 100000011]], [[-1000000000, 1000000000], [1, 1000000001]], [[-100, 50], [-100, 50]], [[-3, 50], [-3, 50]], [[50, 50], [50, 50]], [[1000000000, 1000000002], [1000000001, 1000000002]], [[-10, 1000000001], [-10, 1000000001]], [[1000000001, 1000000002], [1000000000, 1000000002]], [[1000000001, 1000000002], [1000000001, 1000000002]], [[-20, 20], [-10, 10]], [[1000000000, 1000000001], [1000000000, 1000000001]], [[-4, -4], [0, 5]], [[100000007, 100000009], [100000007, 100000009]], [[1000000000, 1000000001], [1000000001, 1000000001]], [[-20, 20], [-20, 20]], [[-999, -5], [-999, -5]], [[-20, 20], [-4, 10]], [[-100, 49], [-100, 49]], [[-4, 11], [-4, 11]], [[1000000001, 1000000001], [1000000001, 1000000001]], [[0, 1000000001], [0, 1000000001]], [[-1000000000, 1000000000], [-1000000000, 1000000000]], [[1000000000, 1000000002], [1000000000, 1000000002]], [[-999, 5], [-999, 5]], [[-999, -100], [-999, -100]], [[-100, -100], [-100, -100]], [[-999, -99], [-999, -99]], [[100000009, 100000011], [100000007, 100000009]], [[-4, 5], [-9, -2]], [[-20, 20], [-4, 9]], [[26, 150], [26, 150]], [[19, 19], [19, 19]], [[-999, 0], [-999, 0]], [[7, 11], [7, 11]], [[-9, -9], [-9, -9]], [[9, 11], [13, 19]], [[-4, -4], [-4, -4]], [[-999, 1], [-999, 1]], [[9, 11], [9, 11]], [[-999, 9], [-999, 9]], [[1000000000, 1000000003], [1000000001, 1000000002]], [[-4, 1000000000], [-4, 1000000000]], [[-1000000000, 999999999], [-1000000000, 999999999]], [[-20, 20], [-4, 5]], [[26, 27], [26, 27]], [[-100, 11], [-100, 11]], [[-3, -3], [-3, -3]], [[-1000, -5], [-1000, -5]], [[-999, 6], [-999, 6]], [[-999999999, 1000000000], [-999999999, 1000000000]], [[-4, 50], [-4, 50]], [[999999999, 999999999], [999999999, 999999999]], [[-9, 10], [-9, 10]], [[-4, 150], [-4, 150]], [[-4, 5], [-4, 5]], [[-1001, -1000], [-1001, -1000]], [[49, 1000000000], [49, 1000000000]], [[-1000, -1000], [-1000, -1000]], [[-20, 150], [-20, 150]], [[-1000, 7], [-1000, 7]], [[-1001, -1001], [-1001, -1001]], [[25, 25], [25, 25]], [[-999, -999], [-1000, -999]], [[13, 100000009], [13, 100000009]], [[-1000, 0], [-1000, 0]], [[-999, -999], [-999, -999]], [[-999999999, 20], [-4, 9]], [[-100, -99], [-100, -99]], [[-10, 50], [-10, 50]], [[-1000, -1], [-1000, -1]], [[-999, 25], [-999, 25]], [[13, 1000000000], [1, 1000000001]], [[150, 150], [150, 150]], [[1000000002, 1000000002], [1000000002, 1000000002]], [[-20, 20], [-4, -4]], [[-1000, -6], [-1000, -6]], [[-1000, 11], [13, 19]], [[19, 150], [19, 150]], [[-3, 999999999], [-3, 999999999]], [[26, 151], [26, 151]], [[-3, 51], [-3, 51]], [[-3, 1000000000], [-3, 1000000000]], [[-4, 0], [-4, 0]], [[-5, 0], [-5, 0]], [[-4, 10], [-4, 10]], [[100000009, 100000011], [100000008, 100000009]], [[-3, 25], [-3, 25]], [[49, 49], [49, 49]], [[-99, -99], [-99, -99]], [[-99, 25], [-99, 25]], [[100000009, 100000011], [100000008, 100000008]], [[-6, 999999999], [-6, 999999999]], [[50, 1000000001], [50, 1000000001]], [[100000008, 100000008], [100000008, 100000008]], [[100000007, 1000000000], [100000007, 1000000000]], [[19, 1000000000], [19, 1000000000]], [[-20, 1], [-4, 10]], [[-3, 0], [-3, 0]], [[50, 1000000002], [50, 1000000002]], [[50, 1000000000], [50, 1000000000]], [[25, 150], [25, 150]], [[-5, -5], [-5, -5]], [[25, 1000000001], [25, 1000000001]], [[-4, 13], [-4, 13]], [[8, 11], [13, 19]], [[-4, 10], [-20, 20]], [[-3, 100000009], [-3, 100000009]], [[13, 19], [9, 11]], [[-3, 100000008], [-3, 100000008]], [[-20, 1], [-20, 1]], [[-4, 19], [-4, 19]], [[-7, 5], [0, 5]], [[-4, 9], [-20, 20]], [[8, 11], [8, 11]], [[-20, 2], [-4, 10]], [[0, 1000000002], [0, 1000000002]], [[11, 1000000000], [11, 1000000000]], [[-1000, -99], [-1000, -99]], [[26, 26], [26, 26]], [[1000000000, 1000000003], [1000000000, 1000000003]], [[1000000000, 1000000004], [1000000000, 1000000004]], [[6, 25], [6, 25]], [[-20, 11], [-20, 11]], [[-11, 10], [-11, 10]], [[100000009, 100000011], [100000009, 100000009]], [[0, 11], [0, 11]], [[100000009, 100000011], [100000009, 100000011]], [[14, 100000009], [14, 100000009]], [[-999, -101], [-999, -101]], [[100000008, 100000009], [100000008, 100000009]], [[-10, 151], [-10, 151]], [[-1001, -1], [-1001, -1]], [[-11, 1], [-11, 1]], [[-100, 10], [-100, 10]], [[149, 150], [149, 150]], [[-4, 6], [-4, 6]], [[-1000000000, -4], [-1000000000, -4]], [[-10, -9], [-10, -9]], [[-999, 151], [-999, 151]], [[-100, -4], [-100, -4]], [[26, 149], [26, 149]], [[-4, 7], [-4, 7]], [[13, 1000000000], [13, 1000000000]], [[-2, 10], [-2, 10]], [[1000000000, 1000000001], [11, 1000000001]], [[-9, 1], [-9, 1]], [[-100, 0], [-100, 0]], [[1, 1000000002], [1, 1000000002]], [[-7, -5], [-7, -5]], [[151, 1000000001], [151, 1000000001]], [[-9, 11], [-9, 11]], [[100000009, 100000009], [100000009, 100000009]], [[13, 19], [13, 19]], [[11, 50], [11, 50]], [[-1000, 11], [-1000, 11]], [[-100, 150], [-100, 150]], [[1000000001, 1000000001], [1000000000, 1000000001]], [[-7, -6], [-7, -6]], [[100000011, 1000000002], [100000011, 1000000002]], [[8, 1000000004], [8, 1000000004]], [[-6, 50], [-6, 50]], [[-1000, -2], [-1000, -2]], [[-999999999, 1], [-999999999, 1]], [[-19, 150], [-19, 150]], [[-1002, -1000], [-1002, -1000]], [[-9, 1000000001], [-9, 1000000001]], [[-3, 24], [-3, 24]], [[-2, 51], [-2, 51]], [[-999999999, 50], [-999999999, 50]], [[-998, 0], [-998, 0]], [[48, 49], [48, 49]], [[999999999, 1000000002], [999999999, 1000000002]], [[14, 150], [14, 150]], [[48, 999999999], [48, 999999999]], [[100000008, 100000011], [100000008, 100000008]], [[-7, -3], [-7, -3]], [[-1000000000, -998], [-1000000000, -998]], [[-998, -100], [-998, -100]], [[27, 1000000001], [27, 1000000001]], [[999999999, 1000000000], [999999999, 1000000000]], [[-10, 9], [-10, 9]], [[13, 20], [13, 20]], [[-4, 27], [-4, 27]], [[11, 1000000000], [-1000000000, 1000000001]], [[-1, 51], [-1, 51]], [[5, 100000011], [5, 100000011]], [[27, 50], [27, 50]], [[-20, 1000000000], [-20, 1000000000]], [[-1, 11], [-1, 11]], [[-20, 1], [-4, -4]], [[5, 1000000002], [5, 1000000002]], [[-999999999, 51], [-999999999, 51]], [[100000010, 100000011], [100000010, 100000011]], [[-3, 100000008], [-9, -2]], [[999999998, 1000000002], [999999998, 1000000002]], [[-19, 0], [-19, 0]], [[-999, -2], [-999, -2]], [[14, 19], [14, 19]], [[-2, 11], [-2, 11]], [[-999, -1], [-999, -1]], [[-4, 28], [-4, 28]], [[-6, -6], [-6, -6]], [[-7, -4], [0, 5]], [[-999999999, 0], [-999999999, 0]], [[-99, 10], [-99, 10]], [[-3, 2], [-9, -2]], [[10, 13], [10, 13]], [[-1000000000, 1000000001], [-1000000000, 1000000001]], [[-5, 9], [-5, 9]], [[0, 6], [0, 6]], [[1000000000, 1000000000], [1000000000, 1000000000]], [[-21, 2], [-21, 2]], [[-4, 100000007], [-4, 100000007]], [[13, 149], [13, 149]], [[-7, -4], [-6, 5]], [[20, 150], [20, 150]], [[-5, 10], [-5, 10]], [[-999999999, 20], [-999999999, 20]], [[19, 151], [19, 151]], [[48, 48], [48, 48]], [[-21, 50], [-21, 50]], [[-20, 2], [-4, -4]], [[100000011, 100000011], [100000011, 100000011]], [[-11, -10], [-11, -10]], [[10, 27], [10, 27]], [[-4, 10], [-20, 9]], [[-998, 1], [-998, 1]], [[-998, -5], [-998, -5]], [[-999999998, -999999998], [-999999998, -999999998]], [[-999, 24], [-999, 24]], [[-21, 20], [-4, 10]], [[-1001, 7], [-1001, 7]], [[-10, -5], [-3, -1]], [[-10, -5], [-3, 0]], [[-1, 0], [0, 1]], [[0, 1], [2, 3]], [[0, 0], [1, 1]], [[1, 6], [4, 10]], [[0, 4], [-3, -1]], [[-10, 7], [-20, 20]], [[-8, -5], [-8, -5]], [[-999999999, 1000000001], [1000000001, 1000000002]], [[-1000, 7], [-20, 20]], [[-1, 5], [-1, 5]], [[-1001, -999], [-1001, -999]], [[-8, -7], [-8, -7]], [[-19, 20], [-19, 20]], [[-8, -6], [-8, -6]], [[-1001, 100000009], [-1001, 100000009]], [[-1, 150], [-1, 150]], [[-10, -8], [-10, -8]], [[-1000, 1000000001], [-1000, 1000000001]], [[-1001, 100000010], [-1001, 100000010]], [[-999, 1000000000], [1, 1000000001]], [[-6, 25], [-6, 25]], [[-1000000000, 100000010], [-1000000000, 100000010]], [[13, 13], [13, 13]], [[-6, 19], [-6, 19]], [[-1, 1000000002], [-1, 1000000002]], [[-7, 149], [-7, 149]], [[-999999999, 1000000000], [-8, 1000000001]], [[-100, 50], [25, 151]], [[25, 151], [25, 151]], [[-99, 50], [25, 150]], [[151, 151], [151, 151]], [[-8, 1000000002], [-8, 1000000002]], [[-9, 25], [-9, 25]], [[-1, 50], [-1, 50]], [[-999, 1000000000], [1000000000, 1000000001]], [[1, 1000000001], [1, 1000000001]], [[100000007, 100000007], [100000007, 100000007]], [[1, 26], [1, 26]], [[-10, 7], [-10, 7]], [[-19, -19], [-19, -19]], [[-999, 1000000000], [-999, 1000000000]], [[-19, 149], [-19, 149]], [[100000011, 1000000003], [100000011, 1000000003]], [[-19, 25], [-19, 25]], [[-999, 20], [-999, 20]], [[1000000001, 1000000002], [-999999999, 1000000001]], [[23, 151], [23, 151]], [[12, 100000007], [12, 100000007]], [[-999999999, 1000000000], [-8, -8]], [[7, 1000000000], [7, 1000000000]], [[-8, 1000000001], [-999999999, 1000000000]], [[0, 5], [-7, -5]], [[-5, 19], [-5, 19]], [[-19, 26], [-19, 26]], [[-1001, 1000000002], [-1001, 1000000002]], [[11, 100000007], [11, 100000007]], [[13, 50], [13, 50]], [[149, 149], [149, 149]], [[-20, 26], [-20, 26]], [[-9, -2], [-9, -2]], [[11, 151], [11, 151]], [[-10, 11], [-10, 11]], [[-9, 24], [-9, 24]], [[7, 7], [7, 7]], [[0, 100000007], [0, 100000007]], [[-999999999, 11], [-999999999, 11]], [[-1002, -1001], [-1002, -1001]], [[-3, 5], [-3, 5]], [[-10, -10], [-10, -10]], [[151, 152], [151, 152]], [[-7, 151], [-7, 151]], [[100000006, 100000007], [100000006, 100000007]], [[-999999999, 1000000001], [-999999999, 1000000001]], [[-2, 1000000002], [-2, 1000000002]], [[8, 1000000000], [8, 1000000000]], [[-2, 151], [-2, 151]], [[-8, -8], [-8, -8]], [[-1000000001, 1000000000], [1, 1000000001]], [[100000010, 1000000002], [100000010, 1000000002]], [[12, 50], [12, 50]], [[100000009, 1000000002], [-999999999, 1000000001]], [[-11, -8], [-11, -8]], [[12, 100000006], [12, 100000006]], [[12, 20], [12, 20]], [[1000000000, 1000000002], [-999999999, 1000000001]], [[-20, 10], [-20, 10]], [[-1000000001, 20], [-1000000001, 20]], [[11, 1000000001], [11, 1000000001]], [[1000000001, 1000000002], [1000000000, 1000000001]], [[1000000002, 1000000002], [1000000000, 1000000001]], [[20, 20], [20, 20]], [[-11, -7], [-11, -7]], [[-8, 1000000000], [-999999999, 1000000000]], [[-1000000001, 100000008], [-1000000001, 100000008]], [[-8, 100000011], [-8, 100000011]], [[-10, 8], [-10, 8]], [[-5, -1], [-5, -1]], [[-9, 1000000001], [1000000001, 1000000002]], [[-1000000000, 20], [-1000000000, 20]], [[13, 14], [13, 14]], [[-999999999, 1000000001], [1000000000, 1000000002]], [[-8, 7], [-8, 7]], [[12, 14], [12, 14]], [[-1001, 100000011], [-1001, 100000011]], [[150, 1000000002], [150, 1000000002]], [[-2, 150], [-2, 150]], [[100000007, 100000011], [100000007, 100000011]], [[-2, 19], [-2, 19]], [[-1000000000, -1001], [-1000000000, -1001]], [[23, 50], [23, 50]], [[-1002, -1002], [-1002, -1002]], [[24, 150], [24, 150]], [[999999999, 1000000000], [-8, 1000000001]], [[-11, 1000000000], [-8, -8]], [[-9, 12], [-9, 12]], [[-1003, -1002], [-1003, -1002]], [[-8, 1000000001], [-8, 1000000001]], [[-11, 19], [-11, 19]], [[-1000000000, 1000000000], [-999999999, -20]], [[14, 149], [14, 149]], [[12, 19], [12, 19]], [[100000010, 100000012], [100000010, 100000012]], [[100000009, 100000012], [100000009, 100000012]], [[149, 100000008], [149, 100000008]], [[11, 1000000002], [11, 1000000002]], [[11, 23], [11, 23]], [[14, 100000010], [14, 100000010]], [[20, 21], [20, 21]], [[150, 100000008], [150, 100000008]], [[11, 12], [11, 12]], [[151, 100000008], [151, 100000008]], [[100000010, 1000000003], [100000010, 1000000003]], [[-8, 25], [-8, 25]], [[-7, -7], [-7, -7]], [[-8, 1000000001], [1000000000, 1000000000]], [[-6, 27], [-6, 27]], [[-999, -11], [-999, -11]], [[26, 100000007], [26, 100000007]], [[-20, 50], [-20, 50]], [[-7, 1000000002], [-7, 1000000002]], [[-1000, 1000000000], [-1000, 1000000000]], [[-1000, -999], [-999, -999]], [[-9, 1000000001], [-999999999, 1000000000]], [[-1000, 100000009], [-1000, 100000009]], [[-999, 26], [-999, 26]], [[-1, 19], [-1, 19]], [[-6, 18], [-6, 18]], [[-8, -8], [-999999999, 1000000000]], [[-7, 100000007], [-7, 100000007]], [[-999999999, 1000000001], [13, 1000000002]], [[24, 24], [24, 24]], [[-999, 1000000000], [0, 1000000001]], [[-11, 1000000002], [-11, 1000000002]], [[18, 18], [18, 18]], [[8, 50], [8, 50]], [[-6, -5], [-6, -5]], [[-8, 1000000001], [999999999, 1000000000]], [[-10, 10], [-20, 0]], [[50, 151], [50, 151]], [[-11, 20], [-11, 20]], [[10, 149], [10, 149]], [[-20, 1000000002], [-20, 1000000002]], [[-100, 100000009], [-100, 100000009]], [[-999, 100000011], [-999, 100000011]], [[-1000, 12], [-1000, 12]], [[50, 100000009], [50, 100000009]], [[-5, 14], [-5, 14]], [[-6, 149], [-6, 149]], [[27, 149], [27, 149]], [[150, 1000000000], [150, 1000000000]], [[-2, 12], [-2, 12]], [[-1000, 151], [-1000, 151]], [[-5, 1000000002], [-5, 1000000002]], [[1000000001, 1000000002], [-999999999, 999999999]], [[-1000000000, -999999999], [-1000000000, -999999999]], [[-1000000001, 13], [-1000000001, 13]], [[-7, 11], [-7, 11]], [[-6, 147], [-6, 147]], [[-100, 149], [-100, 149]], [[-1000000001, -3], [-1000000001, -3]], [[-2, 1000000001], [-2, 1000000001]], [[-1003, -7], [-1003, -7]], [[-1000000000, 1000000001], [-999999999, 1000000000]], [[-19, 13], [-19, 13]], [[-8, 1000000000], [-8, 1000000000]], [[-8, 11], [-8, 11]], [[-999, -998], [-999, -998]], [[-1002, -5], [-1002, -5]], [[-11, -11], [-11, -11]], [[-999, 100000007], [-999, 100000007]], [[49, 151], [49, 151]], [[-1000000000, 100000011], [-1000000000, 100000011]], [[-1000000000, 100000008], [-1000000000, 100000008]], [[14, 14], [14, 14]], [[-8, 1000000001], [-1000000000, 1000000000]], [[-9, 1000000000], [-9, 1000000000]], [[11, 22], [11, 22]], [[-9, -8], [-9, -8]], [[14, 50], [14, 50]], [[-1000000001, 1000000000], [-1000000001, 1000000000]], [[100000007, 1000000002], [100000007, 1000000002]], [[50, 149], [50, 149]], [[-2, 21], [-2, 21]], [[14, 151], [14, 151]], [[-1000, -998], [-1000, -998]], [[-1000000000, 1000000000], [1, 21]], [[-3, 18], [-3, 18]], [[-999999998, 1000000000], [-8, 1000000001]], [[-3, 21], [-3, 21]], [[-999999999, 19], [-999999999, 19]], [[25, 100000007], [25, 100000007]], [[-999, 21], [-999, 21]], [[4, 5], [4, 5]], [[6, 8], [6, 8]], [[49, 1000000001], [49, 1000000001]], [[100000009, 1000000002], [-999999999, 1000000002]], [[-998, -998], [-998, -998]], [[-1001, 19], [-1001, 19]], [[-1003, 1000000001], [-1003, 1000000001]], [[-999, 19], [-999, 19]], [[100000009, 1000000001], [100000009, 1000000001]], [[-19, 49], [-19, 49]], [[21, 21], [21, 21]], [[-999999999, 1000000002], [-999999999, 1000000002]], [[-1, 151], [-1, 151]], [[4, 1000000001], [999999999, 1000000001]], [[-999999998, -7], [-999999998, -7]], [[-1000000001, 1000000000], [0, 1000000001]], [[-6, 150], [-6, 150]], [[-1000000000, -1000000000], [-1000000000, -1000000000]], [[-1000, 26], [-1000, 26]], [[-99, -1], [-99, -1]], [[-9, 100000012], [-9, 100000012]], [[-11, 27], [-11, 27]], [[21, 23], [21, 23]], [[15, 100000010], [15, 100000010]], [[20, 1000000002], [20, 1000000002]], [[-999, 153], [-999, 153]]]
    results = ['NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'YES', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(intersection)