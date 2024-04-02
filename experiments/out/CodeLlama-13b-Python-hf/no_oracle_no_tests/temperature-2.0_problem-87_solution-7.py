def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    res = []
    for i, row in enumerate(lst):
        if x in row:
            res.append((i, row.index(x)))
    return res



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
    inputs = [[[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1], [[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]], 2], [[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 1, 3, 4, 5, 6], [1, 2, 1, 4, 5, 6], [1, 2, 3, 1, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1], [[], 1], [[[1]], 2], [[[], [1], [1, 2, 3]], 3], [[[], [], [], []], 10], [[[1, 2, 3], [4, 5, 6]], 5], [[[1, 1], [1, 2, 3], [4, 5, 6, 7]], 1], [[[1, 0, 4], [4, 8, -1, 1], [0], [5, 5, 5, -3]], 0], [[[0, 0, 0, 0, 0], [0, 1, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8], [], [0, 0, 0]], 0], [[[1, 2, 3], [4, 5, 6], [7, 8]], 3], [[], 5], [[[], [], []], 1], [[[1, 2], [2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10, 11]], 4], [[[1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3], [4, 4], [5, 5, 5, 5, 5, 5, 5, 5]], 5], [[[1, 2], [2, 3, 4], [4, 5, 6, 6, 7], [4, 5, 6, 6, 7], [7, 8, 9, 10, 11], [2, 3, 4]], 4], [[[], [], []], 6], [[[0, 0, 0, 0, 0], [0, 1, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8], [], [0, 0, 0]], -1], [[[3, 1, 2, 3], [4, 5, 6]], 5], [[[1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3], [4, 4], [5, 5, 5, 5, 5, 5, 5, 5], [2, 2, 2, 2, 2]], 5], [[[], [], [], []], 6], [[[], [False, True, True], []], 0], [[[1, 2], [2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10, 11], [7, 8, 9, 10, 11]], 4], [[[0, 0, 0, 0, 0], [0, 1, 2], [70.62468430869876], [0, 1, 2, 3, 4, 5, 6, 7, 8], [], [0, 0, 0]], 0], [[[], [False, True, True], []], -1], [[[1, 2], [2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10, 11]], 9], [[[0, 0, 0, 0, 0], [0, 1, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8], [], [-1, 0, 0, 0, 0]], 3], [[[1, 2, 3], [7, 8, 7]], 3], [[[[False, False, True, True, False, False, True, False, True, True]], [0, 0, 0, 0, 0], [0, 1, 2, 0], [0, 1, 2, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8], [], [-1, 0, 0, 0, 0]], 3], [[[0, 0, 0, 0, 0], [0, 1, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0]], -1], [[[0, 0, 0, 0, 0], [0, 1, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8]], 0], [[[3, 1, 2, 3], [4, 5, 6], [3, 1, 2, 3]], 5], [[[0, 0, 0, 0, 0], [0, 1, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0]], -1], [[[], [], [-3, 35, 54, 0, -3, -92, 68, 7], [], []], 0], [[[1, 2], [2, 3, 4], [4, 5, 6, 7]], 9], [[[3, 1, 2, 3], [4, 5, 6]], 8], [[[1, 1], [1, 11, 3], [1, 11, 3], [4, 5, 6, 7]], 1], [[[3, 1, 2, 3], [4, 5, 6], [3, 1, 2, 3], [4, 5, 6]], 5], [[[0]], 1], [[[1]], 1], [[[1, 2], [2, 1, 3], [1, 3, 2, 1], [2, 1, 1]], 1], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], 7], [[[1, 5, 3, 5, 7, 5, 9, 5, 11, 5, 13, 5]], 5], [[[], [], [], [], []], 1], [[[], [], [], [], []], 10], [[[1], [1], [1], [1]], 1], [[[1], [1], [1], [1]], 2], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 2], [[[2, 0]], 1], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 3], [[[]], 1], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 10], [[[], []], 0], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], 10], [[[]], 0], [[[1, 2, 3], [3, 2, 1], [1, 2, 9, 3], [1, 2, 9, 3], [3, 2, 1], [1, 2, 3]], 3], [[[], []], -98], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 62], [[[0]], 0], [[[], [], [], []], 1], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], -27], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], -27], [[[], [], [], [], []], 0], [[[], [], [1], [1], [1]], 0], [[[3, 2, 1], [1, 2, 9, 3], [1, 2, 9, 3], [3, 2, 1], [1, 2, 3]], 7], [[[1, 3, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 62], [[[4, 3, 2, 5], [2, 1, 6]], -27], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 4], [[[1, 2, 7], [3, 2, 1], [1, 2, 7], [1, 2, 3], [3, 2, 1], [1, 2]], 10], [[[3, 2, 1], [1, 2, 9, 3], [3, 2, 1], [1, 2, 3]], 8], [[[1], [1], [1]], 1], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], 8], [[[1, 5], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], 10], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], 9], [[[]], 7], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], 49], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6], [2, 1, 6]], 0], [[[True, False, False], [], [], [], [], []], 1], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 5], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6], [2, 1, 6]], 9], [[[0]], 9], [[[1, 2, 3], [3, 2, 1], [1, 2, 1, 3], [1, 2, 1, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 5], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], 34], [[], -89], [[[], [], [], [], []], 2], [[[1, 2, 3], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 5], [[], 10], [[[1, 2], [2, 1, 3], [2, 1, 1]], 1], [[[3, 2, 1], [3, 2, 2], [1, 2, 9, 3], [3, 2, 2], [1, 2, 3]], 8], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1]], -27], [[[], [], [-44.27424904738355, -45.679324832296906, 95.34516483790298, 21.648674306121123, -32.17970898728211, -8.081667034352762, -23.02295170209456, 80.76641310561561, 9.678829361211541, 68.16144984963583], [], [], []], 2], [[[], [], [], [], []], 62], [[[], [], [], [], [], []], -98], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 34], [[[]], 6], [[], 6], [[[1, 5, 3, 5, -66, 5, 9, 5, 11, 5, 13, 5]], 5], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1]], 3], [[[4, 3, 2, 5]], -27], [[[1, 2, 3], [3, 2, 1], [1, 2, 1, 3], [1, 2, 1, 3], [3, 2, 1], [1, 2, 3], [1, 2, 3]], 5], [[[True, False, False], [], [], [], [], []], 9], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 74], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3], [1, 2, 3]], 4], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3]], 45], [[[], [-7.55236098678059], [-7.55236098678059], [], [], [], []], -99], [[[False, True, False, True, True, False, True, False], [True, False, False], [], [], [], [], []], 1], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1]], -26], [[[1, 2], [1, 1], [2, 1, 3], [1, 1]], 1], [[[1, 2], [2, 1, 3], [4, 3, 2, 4, 5], [4, 3, 2, 4, 5], [2, 1, 6], [2, 1, 6]], 62], [[[-6, -38, 25, 3, 45]], 0], [[[], [], []], -98], [[[], [], []], 0], [[[], [-7.55236098678059], [-7.55236098678059], [], ['', 'uL', 'ksjvRqrLhyAOKkvpwcrWhP'], [], []], -99], [[[1, 2, 3], [3, 2, 1], [1, 2, 3], [3, 2, 1], [1, 2, 3], [1, 2, 3]], 2], [[], -1], [[[], []], 13], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], -73], [[[]], 8], [[[1, 5], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], 44], [[[], [], [], []], 0], [[[], [], []], -1], [[[], [], [], []], 4], [[[5]], 5], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0], [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1], [[[1, 2, 3, 4], [1, 2, 3], [1, 2], [1]], 1], [[[], [], []], 5], [[[1, 2, 3, 4, 5]], 3], [[[1], [2], [3]], 2], [[[], [], [], [1, False, ['rKW', 'NJISO', '', 'GKBhmtgbr', 'oZg', 'wK'], 99.16010072704816, 'OXMYkjFnn', True, True, True, [[1, -16.90064763272207, -52.63553163835755, 80, -59], 6, 64.00391269191459, -27.552555259336174, False, 'VXnk', 1, [-74.08431048384021, 8.119517181553633, 24.987035577244157, -52.62309758224084, -65.04267587536296, -12.933482397247616, 81.74490543580112], 3, 13], 'KnXUmD'], []], 1], [[[1, 2], [2, 1, 3], [4, 3, 2, 5], [2, 1, 6]], 6], [[[], [], [1, False, ['rKW', 'NJISO', '', 'GKBhmtgbr', 'oZg', 'wK'], 99.16010072704816, 'OXMYkjFnn', True, True, True, [[1, -16.90064763272207, -52.63553163835755, 80, -59], 6, 64.00391269191459, -27.552555259336174, False, 'VXnk', 1, [-74.08431048384021, 8.119517181553633, 24.987035577244157, -52.62309758224084, -65.04267587536296, -12.933482397247616, 81.74490543580112], 3, 13], 'KnXUmD'], []], 1], [[[5, 3, 5, 7, 5, 9, 5, 11, 5, 13, 5]], 5], [[[-59, 0]], 1], [[[-59, 0]], 80], [[[2, 1], [1, 2], [2, 1], [4, 3, 2, 5], [2, 1, 6], [2, 1]], 6], [[[1, 0], [1, 0]], 80], [[[], [-52.63553163835755, -20.85829830424977, -19.258305309776077, 99.16010072704816, 26.11260344815392, -59.365757443211244, 98.25223736083848], [], [], [], []], 10], [[[1], [1], [1], [1], [1]], 1], [[[1, 5, 3, 5, 7, 5, 9, 5, 11, 5, 13, 5, 3]], 0], [[[5, 3, 5, 7, 5, 9, 5, 11, 5, 13, 5], [5, 3, 5, 7, 5, 9, 5, 11, 5, 13, 5]], 4], [[], 0], [[[1, 2], [2, 1, 3], [1, 3, 2, 1], [2, 1, 1], [1, 2]], -95], [[[1], [1], [1], [1]], 9], [[[1, 5, 3, 5, 7, 5, 9, 5, 11, 5, 13, 6, 5, 3]], 0], [[[1], [1], [1, 1], [1]], 2], [[[2, 1], [1, 2], [2, 1], [4, 3, 2, 5], [2, 1, 6], [2, 1]], 7], [[[1], [1], [1], [1], [1]], 2], [[[1], [1], [1], [1]], 0], [[[2, 1], [1, 4, 2], [2, 1], [4, 3, 2, 5], [2, 1, 6], [2, 1]], 7], [[[1], [1], [], [1]], 0], [[[1], [1]], 0], [[[1], [1], [1, 1], [1, 2], [1, 1]], 3], [[[1]], 10], [[[2, 1], [1, 2, 2], [2, 1], [4, 3, 2, 5], [2, 1, 6], [2, 1]], 7], [[[2, 1], [1, 2], [2, 1], [4, 3, 2, 5], [2, 1, 6], [2, 1]], 5], [[[80, 2, 1], [80, 2, 1], [1, 2], [80, 2, 1], [4, 3, 2, 5], [2, 1, 6], [80, 2, 1]], 5], [[[2, 1], [1, 2, 2], [2, 1], [4, 3, 2, 5], [2, 1, 6], [2, 1], [2, 1]], 7], [[], 2], [[[1], [1], [11, 1], [1], [1]], 2], [[[2, 1], [1, 2, 2], [2, 1], [4, 3, 2, 5], [2, 1]], 8], [[[1], [1], [1, 1], [1]], 7], [[[1], [1], [2, 1], [2, 1], [1], [2, 1]], 11], [[[2, 0, 1], [1, 2], [2, 0, 1], [4, 3, 2, 5], [2, 1, 6], [2, 0, 1]], 6], [[[1, 2], [2, 1, 3], [1, 3, 2, 1], [2, 1, 1], [1, 2]], -96], [[[-59, 0], [-59, 0]], 80], [[[], [1], [1], [1], []], 1], [[[2, 2], [1, 2], [2, 2], [4, 3, 2, 5], [2, 1, 6], [2, 2], [2, 2]], 5], [[[1], [1], [11, 1], [1]], 2], [[[1, 2], [2, 1, 3], [1, 3, 2, 1], [2, 1, 1], [1, 2], [1, 2]], 11], [[], -96], [[[1], [1], [11, 1]], 0], [[[1], [1], [-59, 11, 1]], 0], [[], -59], [[[1, 0], [1, 0], [1, 0]], 81], [[[1], [1], [-59, 11, 1]], 1], [[[1], [1, 1], [11, 1], [1, 1], [1]], 2], [[[2], [1, 2], [2], [4, 3, 2, 5], [2, 1, 6], [2], [2]], 5], [[[2, 1], [1, 2, 2], [1, 2, 2], [2, 1], [4, 3, 2, 5], [2, 1, 6], [2, 1]], 7], [[[], [], [], [1, False, ['rKW', 'NJISO', '', 'GKBhmtgbr', 'oZg', 'wK'], 99.16010072704816, 'OXMYkjFnn', True, True, True, [[1, -16.90064763272207, -52.63553163835755, 80, -59], 6, 64.00391269191459, -27.552555259336174, False, 'VXnk', 1, [-74.08431048384021, 8.119517181553633, 24.987035577244157, -52.62309758224084, -65.04267587536296, -12.933482397247616, 81.74490543580112], 3, 13], 'KnXUmD']], 1], [[[1, 5, 3, 5, 7, 5, 9, 5, 11, 5, 13, 5], [1, 5, 3, 5, 7, 5, 9, 5, 11, 5, 13, 5]], 5], [[[1], [1], [-59, 11, 1]], 81], [[[1], [1], [1], [1], [1]], 0], [[[1]], 0], [[[1], [1], [], [1]], -28], [[[1, 0], [1, 0]], -32], [[[5, 3, 5, 7, 5, 9, 5, 11, 5, 13, 5], [5, 3, 5, 7, 5, 9, 5, 11, 5, 13, 5]], 5], [[[1, 1], [1], [1], [1], [1, 1], [1]], 2], [[[], [1], [1], [1], [], [1]], 1], [[[], [], [], [], []], -32], [[[2, 1, 1], [1, 2], [2, 1, 1], [4, 3, 2, 5], [2, 1, 6], [2, 1, 1]], 6], [[[1], [1], [1]], 9], [[], 79], [[[1], [2, 1, 3], [1, 3, 2, 1], [2, 1, 1], [1]], -96], [[[-59]], 1], [[], -58], [[[], [1], [1], [1], [87.61431870060784, -74.08431048384021, -43.44191994241269]], 0], [[[1], [1], [], [1]], -1], [[[-59, 0], [-59, 0], [-59, 0]], 80], [[[2], [1], [11, 1], [1], [2]], 2], [[[2, 1], [4, 3, 3, 2, 5], [1, 2, 2], [2, 1], [4, 3, 3, 2, 5], [2, 1, 6], [2, 1], [2, 1]], 7], [[[1], [1], [1, 1], [1, 2], [1, 1]], 2], [[[2, 1], [1, 2, 2], [2, 1], [4, 3, 3, 2, 5], [2, 1, 6], [4, 3, 3, 2, 5], [2, 1], [2, 1]], 7], [[[], [-52.63553163835755, -20.85829830424977, -19.258305309776077, 99.16010072704816, 26.11260344815392, -59.365757443211244, 98.25223736083848], [True, False, False, True, True, False], [], [], [], []], -6], [[[1], [1], ['Qmiom', 'OXMYkjFnn', 'zxopRHtsCb', 'SPOKvaykqJ', 'ihaVTyy', 'OCr', 'yP', 'nCIHYIJiq'], [], [1]], -1], [[[2, 1], [1, 2, 2, 2], [2, 1], [4, 3, 2, 5], [2, 1, 6], [2, 1], [1, 2, 2, 2], [2, 1]], 7], [[[1], [0], [1], [0], [1]], 2], [[[1], [1], [1, 1], [79, 2], [1, 1]], 3], [[[False], [], [], [], []], -32], [[[1], [1], [1], [1]], 81], [[[1, 0], [1, 0], [1, 0], [1, 0]], 81]]
    results = [[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)], [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)], [(0, 0), (1, 0), (2, 1), (2, 0), (3, 2), (3, 0), (4, 3), (4, 0), (5, 4), (5, 0), (6, 5), (6, 0)], [], [], [(2, 2)], [], [(1, 1)], [(0, 1), (0, 0), (1, 0)], [(0, 1), (2, 0)], [(0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (4, 2), (4, 1), (4, 0)], [(0, 2)], [], [], [(1, 2), (2, 0)], [(4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0)], [(1, 2), (2, 0), (3, 0), (5, 2)], [], [], [(1, 1)], [(4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0)], [], [(1, 0)], [(1, 2), (2, 0)], [(0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (3, 0), (5, 2), (5, 1), (5, 0)], [], [(3, 2)], [(2, 3)], [(0, 2)], [(4, 3)], [], [(0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 2), (3, 1), (3, 0), (4, 0)], [(1, 1)], [], [(2, 3)], [], [], [(0, 1), (0, 0), (1, 0), (2, 0)], [(1, 1), (3, 1)], [], [(0, 0)], [(0, 0), (1, 1), (2, 3), (2, 0), (3, 2), (3, 1)], [], [(0, 11), (0, 9), (0, 7), (0, 5), (0, 3), (0, 1)], [], [], [(0, 0), (1, 0), (2, 0), (3, 0)], [], [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], [], [(0, 2), (1, 0), (2, 2), (3, 0), (4, 2)], [], [], [], [], [], [(0, 2), (1, 0), (2, 3), (3, 3), (4, 0), (5, 2)], [], [], [(0, 0)], [], [], [], [], [], [], [], [], [], [], [], [(0, 0), (1, 0), (2, 0)], [], [], [], [], [], [], [(0, 0)], [], [], [], [], [], [], [], [], [], [(0, 0), (1, 1), (2, 2), (2, 1)], [], [], [], [], [], [], [], [], [(0, 11), (0, 9), (0, 7), (0, 5), (0, 3), (0, 1)], [(0, 2), (1, 0), (2, 2), (3, 0), (4, 2), (5, 0)], [], [], [], [], [], [], [], [(0, 6), (0, 4), (0, 3), (0, 1), (1, 0)], [], [(0, 0), (1, 1), (1, 0), (2, 1), (3, 1), (3, 0)], [], [], [], [], [], [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)], [], [], [], [], [], [], [], [], [(0, 0)], [], [(0, 2), (0, 1), (0, 0), (1, 2), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0)], [(0, 0), (1, 0), (2, 0), (3, 0)], [], [(0, 2)], [(1, 0)], [(3, 7), (3, 6), (3, 5), (3, 0)], [(3, 2)], [(2, 7), (2, 6), (2, 5), (2, 0)], [(0, 10), (0, 8), (0, 6), (0, 4), (0, 2), (0, 0)], [], [], [(4, 2)], [], [], [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [(3, 3)], [(4, 3)], [], [], [], [], [], [], [(4, 2)], [], [], [(1, 0), (2, 0), (3, 0)], [(3, 3)], [], [], [], [], [], [], [], [(0, 0), (1, 0), (2, 2)], [], [(3, 3)], [], [(3, 7), (3, 6), (3, 5), (3, 0)], [(0, 11), (0, 9), (0, 7), (0, 5), (0, 3), (0, 1), (1, 11), (1, 9), (1, 7), (1, 5), (1, 3), (1, 1)], [], [], [], [], [], [(0, 10), (0, 8), (0, 6), (0, 4), (0, 2), (0, 0), (1, 10), (1, 8), (1, 6), (1, 4), (1, 2), (1, 0)], [], [(1, 0), (2, 0), (3, 0), (5, 0)], [], [(4, 2)], [], [], [], [], [], [], [], [], [(0, 0), (4, 0)], [], [(3, 1)], [], [], [], [], [], [], [], [], []]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(get_row)