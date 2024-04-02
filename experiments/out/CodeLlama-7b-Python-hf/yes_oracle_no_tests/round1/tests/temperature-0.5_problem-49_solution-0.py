def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    
	Do not include these tokens in the code:  return pow ( 2 , n , p )
	"""

    return pow(2, n, p)


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
    inputs = [[3, 5], [1101, 101], [0, 101], [3, 11], [100, 101], [30, 5], [31, 5], [5, 17], [10, 23], [20, 37], [50, 79], [100, 89], [200, 113], [7, 3], [12, 7], [50, 23], [101, 103], [20, 20], [37, 37], [200, 112], [19, 19], [3, 3], [200, 200], [79, 79], [17, 20], [100, 20], [100, 3], [6, 6], [23, 200], [78, 79], [6, 78], [5, 5], [6, 19], [5, 6], [7, 78], [113, 112], [3, 20], [6, 20], [7, 101], [101, 101], [7, 6], [5, 200], [17, 21], [21, 5], [10, 10], [20, 21], [20, 17], [17, 100], [19, 2], [99, 20], [17, 17], [7, 7], [79, 3], [6, 10], [99, 98], [78, 100], [79, 112], [112, 101], [112, 20], [19, 6], [8, 78], [79, 200], [112, 113], [10, 88], [112, 112], [12, 101], [8, 200], [80, 50], [113, 113], [20, 19], [50, 20], [12, 4], [202, 200], [19, 200], [98, 4], [19, 50], [113, 100], [8, 100], [200, 8], [17, 78], [37, 80], [88, 21], [202, 202], [10, 17], [19, 5], [19, 4], [36, 200], [101, 200], [112, 114], [88, 97], [17, 5], [200, 37], [100, 18], [88, 20], [20, 103], [6, 21], [7, 20], [19, 18], [21, 103], [80, 37], [21, 102], [36, 7], [100, 100], [20, 99], [36, 101], [80, 5], [36, 78], [234, 101], [50, 17], [4321, 1009], [100000, 7], [9876, 54321], [1000000, 999983], [999999, 100019], [172870, 530123], [1048576, 523], [523, 1048576], [233, 101], [172870, 9876], [9875, 54321], [172871, 523], [1009, 17], [172871, 172871], [999983, 999983], [233, 233], [101, 54321], [999984, 999984], [1000002, 1000000], [50, 9875], [172870, 101], [232, 101], [523, 523], [172871, 172870], [7, 999999], [4321, 4321], [54321, 17], [172872, 172871], [54321, 54321], [233, 530123], [4321, 999999], [235, 234], [1000002, 1000001], [233, 234], [172870, 172871], [17, 1009], [1000003, 1000003], [1000003, 17], [999999, 172871], [172870, 172870], [999984, 172871], [523, 100000], [100019, 172872], [9877, 54321], [16, 16], [7, 233], [18, 235], [1000002, 1000002], [101, 530123], [999984, 101], [172871, 235], [101, 50], [1000002, 18], [999984, 999983], [172869, 172869], [524, 523], [233, 172871], [1000000, 172871], [999984, 235], [999999, 999999], [101, 1000000], [232, 232], [172871, 172869], [9877, 9877], [1000000, 524], [1000001, 7], [1048576, 524], [51, 50], [530123, 530123], [9877, 9875], [522, 524], [7, 9877], [9876, 9876], [999984, 999999], [530123, 9877], [999984, 999985], [1000003, 523], [172869, 172871], [999984, 999998], [4321, 233], [9877, 9876], [999999, 18], [1000000, 1000000], [172871, 530123], [9874, 9875], [523, 99999], [1000003, 54321], [9, 1000001], [172872, 1009], [54323, 523], [235, 1009], [522, 999983], [233, 9877], [1000000, 999999], [9875, 530123], [9877, 54322], [231, 231], [18, 9875], [172869, 18], [1000000, 172870], [522, 100000], [524, 1009], [530124, 530123], [234, 16], [102, 1000000], [51, 1009], [18, 172869], [51, 51], [9875, 172871], [1000003, 1000002], [523, 524], [17, 172872], [523, 1048577], [522, 17], [99999, 99999], [530122, 231], [234, 999984], [8, 9877], [999983, 999984], [9, 101], [7, 999984], [232, 530122], [523, 172869], [999999, 19], [9875, 99999], [54320, 54321], [233, 999985], [522, 9876], [4322, 172869], [16, 9875], [17, 9877], [522, 9877], [232, 999984], [172870, 9875], [9875, 9875], [54322, 7], [172870, 172869], [4320, 1009], [1000001, 524], [530122, 19], [54322, 4321], [19, 17], [54323, 530124], [233, 9878], [54323, 232], [172869, 4322], [4320, 999984], [9878, 9875], [52, 51], [1000001, 1000000], [1048577, 1000001], [54322, 1000000], [530122, 530123], [8, 530122], [7, 1000001], [100019, 172871], [9876, 523], [1048576, 1009], [4322, 530123], [6, 100000], [172871, 18], [232, 522], [1000000, 18], [9877, 9878], [524, 51], [1009, 233], [172872, 1010], [6, 530123], [1009, 234], [523, 172870], [18, 524], [530123, 1009], [100019, 100019], [9875, 524], [1048576, 4322], [9874, 999983], [530124, 9875], [54320, 101], [172870, 1048577], [1048577, 54322], [1000001, 999984], [19, 9], [233, 100], [1000001, 1000001], [9878, 9877], [234, 235], [1048576, 100019], [19, 1000001], [9874, 9874], [19, 10], [54320, 1010], [1000000, 9877], [234, 1000001], [1000000, 999984], [232, 172872], [1000000, 4320], [19, 524], [172871, 1009], [1000002, 1000003], [235, 100000], [4320, 4320], [8, 232], [523, 999985], [100019, 530122], [19, 235], [1009, 1009], [101, 1009], [54321, 100], [236, 236], [1000001, 530123], [172871, 6], [4322, 1010], [172872, 172872], [9876, 18], [235, 236], [50, 523], [9876, 999983], [172873, 172872], [234, 233], [19, 100], [18, 18], [172870, 172868], [172873, 1009], [1048577, 4322], [19, 9875], [522, 522], [999983, 530123], [530123, 524], [999998, 999999], [523, 17], [18, 1000001], [172868, 235], [1000002, 530122], [172869, 232], [4320, 233], [7, 999983], [172869, 9875], [18, 523], [101, 999999], [8, 54321], [9875, 1048577], [172869, 172870], [9877, 233], [10, 999983], [525, 9877], [9878, 9874], [99999, 9877], [4321, 999985], [52, 172872], [17, 172873], [999984, 530122], [1009, 4320], [999985, 999983], [530122, 100019], [999998, 18], [172872, 530122], [522, 9875], [1000000, 54322], [172871, 172872], [1009, 235], [99999, 523], [99999, 1048576], [19, 4322], [1000000, 525], [4319, 4320], [525, 17], [530124, 999997], [522, 54322], [54323, 9877], [522, 530124], [9875, 530124], [523, 18], [172868, 172868], [54323, 231], [100000, 100000], [999984, 7], [172873, 19], [9876, 9877], [172871, 999983], [18, 19], [233, 236], [4320, 50], [234, 9878], [999985, 172871], [1048576, 1048576], [102, 54322], [999997, 100019], [4318, 4320], [238, 236], [101, 52], [4322, 1009], [999997, 18], [999985, 8], [1048577, 49], [19, 102], [4323, 999985], [1011, 1010], [999984, 18], [1048576, 1048575], [231, 530122], [172868, 172869], [4323, 4320], [8, 999999], [999998, 999998], [9877, 4320], [54322, 54322], [525, 525], [525, 524], [100019, 232], [102, 9876], [233, 102], [9877, 999998], [4321, 1000001], [9877, 999983], [522, 100001], [525, 54323], [16, 20], [10, 236], [4318, 19], [7, 232], [999984, 232], [9875, 9877], [100000, 236], [100018, 100019], [1000002, 54322], [172869, 172868], [100018, 172873], [999985, 52], [99, 54321], [9878, 17], [20, 18], [233, 172872], [1048577, 1048577], [236, 102], [16, 6], [1000002, 999984], [1000002, 100000], [999983, 172870], [9878, 9878], [232, 17], [1011, 1009], [234, 530124], [238, 99], [530122, 530122], [100000, 172871], [999997, 16], [999985, 172872], [100018, 100018], [530124, 530124], [9, 4322], [999997, 17], [231, 523], [16, 999997], [9875, 52], [1011, 9878], [172870, 100000], [102, 4321], [100019, 530123], [999983, 9875], [530123, 521], [18, 20], [1008, 1009], [1000002, 525], [530123, 530124], [172870, 9878], [100000, 6], [524, 524], [52, 1000001], [172873, 236], [10, 234], [236, 172874], [10, 1000001], [9875, 9876], [1009, 18], [19, 1048577], [999984, 1009], [9875, 9874], [18, 231], [172873, 1048576], [999983, 172871], [4322, 1048576], [99999, 9878], [233, 232], [4322, 172870], [19, 1000002], [54319, 54320], [7, 8], [999985, 999986], [100000, 9], [50, 50], [530121, 530122], [1010, 100018], [238, 238], [999984, 100001], [172871, 1010], [100000, 524], [1008, 18], [524, 18], [9, 530122], [16, 82], [1009, 16], [52, 522], [100001, 172871], [54323, 530123], [172873, 172873], [100018, 233], [530122, 7], [4321, 4319], [52, 17], [1000001, 999998], [100001, 100001], [231, 1000003], [100, 1011], [100000, 999985], [524, 999999], [54321, 172871], [18, 999984], [9, 9], [54322, 172873], [172869, 100001], [235, 9878], [237, 236], [999986, 9875], [77, 1010], [172871, 999999], [232, 4322], [17, 4320], [18, 1009], [172873, 172874], [172871, 524], [100001, 1048576], [100, 16], [19, 999986], [525, 523], [54318, 172873], [1000003, 530122], [1009, 9], [77, 172871], [1008, 234], [9, 521], [9874, 530124], [52, 1000002], [9875, 54319], [234, 54320], [54323, 522], [100, 999984], [9877, 530124], [100, 999997], [231, 8], [524, 17], [54320, 54322], [4320, 523], [1000000, 999986], [51, 1011], [4322, 100019], [18, 9874], [522, 521], [1000002, 4323], [54323, 54322], [52, 52], [172870, 1000004], [16, 1009], [82, 82], [999998, 524], [9874, 54321], [231, 54322], [4318, 54321], [100018, 999986], [4322, 232], [1000002, 172872], [4322, 4322], [999986, 1048576], [54318, 231], [234, 524], [54318, 4319], [8, 8], [530122, 9877], [521, 233], [172869, 54321], [1000004, 1000001], [999983, 530122], [54322, 54319], [8, 172869], [530121, 530121], [51, 54319], [1011, 1048576], [4319, 9875], [172870, 4323], [17, 530124], [1048576, 1048577], [1048578, 1048577], [172872, 18], [172873, 999997], [100001, 4322], [100018, 1008], [0, 1], [1, 1], [0, 2], [1, 2], [2, 2], [99, 2], [100, 2], [2, 1], [0, 100], [50, 1000000], [99999, 100000], [234, 523], [999999, 1048576], [530123, 234], [99997, 100000], [99997, 9877], [99997, 9878], [99997, 99997], [999999, 999983], [1048577, 172870], [99999, 100019], [234, 100], [101, 523], [99998, 99997], [7, 100], [17, 234], [54321, 172870], [999983, 99997], [17, 999984], [9876, 54322], [530124, 234], [50, 100019], [99997, 523], [17, 99997], [99999, 100020], [999982, 999982], [100, 7], [100000, 9876], [54322, 100], [16, 999984], [1000000, 1000001], [99, 7], [999998, 100019], [530124, 235], [234, 234], [9878, 1048576], [530124, 9878], [7, 234], [98, 99], [530123, 54321], [100, 99], [1000000, 234], [16, 523], [4321, 99997], [1048576, 530123], [999985, 999984], [172870, 999998], [101, 530122], [999982, 524], [999983, 524], [99, 101], [999998, 9878], [530123, 235], [1048576, 999982], [530123, 99997], [8, 7], [54322, 530125], [999982, 4321], [76, 100000], [7, 523], [99999, 16], [54322, 234], [999982, 999983], [101, 100], [530122, 524], [1048575, 46], [99999, 15], [999998, 76], [99, 100], [9876, 1010], [99998, 100000], [101, 99998], [999981, 4321], [1000000, 233], [9877, 1048576], [100020, 9878], [17, 1000000], [523, 522], [100, 9876], [54322, 99997], [999981, 1048577], [54322, 54321], [100000, 233], [4321, 999983], [1048575, 99], [98, 101], [530123, 99996], [98, 98], [999981, 4320], [523, 99997], [1048579, 1048577], [99996, 99997], [522, 523], [15, 54321], [98, 1048577], [17, 999999], [522, 1000000], [54321, 1000000], [999999, 100020], [99, 999981], [233, 54322], [530124, 99997], [9876, 522], [999998, 530122], [100019, 4321], [99996, 9877], [999985, 999985], [100020, 54322], [16, 9878], [1048576, 234], [235, 999998], [530123, 100], [234, 999999], [9876, 1048577], [235, 46], [15, 9878], [15, 523], [999999, 100018], [523, 99], [100020, 99], [97, 172870], [235, 999999], [101, 234], [8, 99], [1048575, 1048575], [530122, 99996], [999999, 4321], [100, 999981], [76, 76], [99997, 98], [1048576, 9876], [521, 1000000], [999999, 234], [530124, 530125], [54321, 4320], [1048574, 172870], [1048578, 1048576], [530124, 1048575], [1048576, 7], [1048576, 9877], [9879, 9878], [99998, 530122], [9876, 524], [524, 172870], [4320, 99997], [233, 1000000], [16, 1048576], [54322, 1048576], [98, 97], [9878, 530123], [523, 54321], [7, 172870], [99998, 1048576], [4320, 99999], [1011, 99997], [46, 235], [999983, 99999], [999998, 172870], [1000000, 999982], [100020, 50], [100020, 1048576], [101, 99997], [530125, 999982], [1048575, 100001], [4321, 1011], [9878, 521], [1011, 1011], [54322, 99998], [1010, 1010], [1048576, 522], [530122, 99995], [1000000, 100020], [97, 98], [172871, 9878], [101, 9878], [9876, 1048575], [9876, 530125], [54321, 100001], [999999, 530122], [234, 999998], [99997, 530125], [235, 99997], [234, 530125], [15, 101], [530122, 522], [1000001, 172872], [54322, 999984], [530125, 54321], [530122, 100], [88, 88], [99999, 999983], [1048577, 9878], [530124, 99999], [16, 1048577], [172870, 100019], [1048576, 99995], [1000001, 234], [17, 999985], [99999, 4321], [233, 99996], [1048577, 9877], [100021, 100021], [97, 9878], [100021, 54322], [100021, 99996], [7, 54321], [530122, 9878], [521, 17], [100019, 1048578], [1048574, 1048574], [235, 1000000], [521, 521], [1010, 8], [530122, 172871], [1000000, 15], [1048581, 1048580], [235, 8], [97, 76], [99998, 172872], [4319, 99999], [9878, 54321], [46, 1048575], [98, 999981], [98, 100018], [99996, 100000], [235, 521], [100020, 100020], [17, 1048578], [99998, 99998], [530124, 100000], [523, 1048575], [522, 999985], [14, 15], [999986, 999983], [99997, 97], [233, 523], [999985, 1048574], [99995, 99998], [100000, 100001], [1048578, 1048578], [99999, 1048578], [1048574, 100020], [99997, 1048576], [1048576, 100001], [4321, 99999], [99996, 99996], [17, 99998], [234, 530123], [530122, 1048576], [1048577, 1048576], [97, 99996], [522, 54321], [9879, 1048580], [4320, 100000], [999983, 100000], [9876, 77], [101, 99], [98, 4321], [98, 9876], [1048574, 999998], [235, 99999], [16, 9879], [99998, 234], [100018, 100000], [17, 99999], [15, 50], [99999, 99998], [530122, 530121], [172872, 4321], [100019, 100020], [235, 235], [49, 50], [100000, 14], [99996, 16], [999984, 100019], [233, 524], [76, 523], [100021, 530122], [99, 99997], [100020, 100021], [1048580, 99995], [523, 999983], [54321, 233], [1010, 101], [234, 232], [100018, 232], [100, 98], [100, 99998], [100020, 9879], [100020, 1048577], [76, 9878], [77, 9876], [76, 99999], [50, 49], [99996, 999999], [100020, 1048578], [1048576, 999983], [99999, 102], [4321, 530123], [1048577, 1048578], [46, 530122], [1048574, 100019], [530125, 99], [999999, 1000000], [1010, 999986], [235, 530123], [999981, 54322], [9879, 9880], [88, 89], [1000000, 54321], [999981, 999981], [4319, 999982], [76, 530125], [1048575, 1048576], [47, 47], [101, 102], [1048579, 100], [530122, 101], [100002, 100001], [9876, 4319], [1011, 521], [54321, 54322], [7, 100017], [4320, 9876], [99999, 9876], [97, 97], [99999, 1048579], [9880, 100000], [999985, 522], [54320, 54320], [234, 97], [76, 234], [89, 89], [7, 97], [99996, 172870], [9879, 999999], [1048575, 999985], [999984, 99999], [15, 1000001], [530122, 100021], [17, 523], [9876, 999981], [530122, 523], [999985, 98], [98, 530124], [999986, 999982], [46, 46], [1048580, 1048580], [16, 524], [101, 7], [530125, 47], [999999, 999984], [100, 100018], [1048574, 88], [54320, 1048578], [1012, 1011], [9878, 7], [14, 54321], [172871, 100019], [96, 172870], [4318, 1048576], [89, 100000], [530122, 999983], [1048575, 99997], [235, 530125], [8, 236], [999981, 172870], [89, 54322], [530125, 530124], [47, 89], [100002, 999998], [1048581, 46], [76, 530123], [1048576, 521], [7, 9880]]
    results = [3, 2, 1, 8, 1, 4, 3, 15, 12, 33, 73, 2, 16, 2, 1, 18, 52, 16, 2, 32, 2, 2, 176, 2, 12, 16, 1, 4, 8, 1, 64, 2, 7, 2, 50, 32, 8, 4, 27, 2, 2, 32, 11, 2, 4, 4, 16, 72, 0, 8, 2, 2, 2, 4, 36, 44, 16, 56, 16, 2, 22, 88, 1, 56, 16, 56, 56, 26, 2, 4, 4, 0, 104, 88, 0, 38, 92, 56, 0, 32, 32, 16, 4, 4, 3, 0, 136, 152, 16, 36, 2, 33, 16, 16, 36, 1, 8, 2, 72, 34, 32, 1, 76, 67, 78, 1, 40, 70, 4, 861, 2, 31228, 262144, 54811, 32374, 308, 0, 35, 2008, 15614, 283, 2, 2, 2, 2, 29066, 903088, 437504, 7499, 6, 68, 2, 123188, 128, 3499, 2, 4, 33053, 447752, 2, 128, 421982, 32, 1, 911, 2, 8, 94084, 61594, 110263, 28608, 145184, 8135, 0, 128, 119, 64, 163011, 31, 8, 2, 10, 4, 21761, 4, 12294, 15297, 61, 399680, 410752, 24, 87044, 4622, 84, 4, 172, 48, 146627, 7897, 4, 128, 4096, 822277, 6332, 469736, 432, 86436, 635826, 1, 8192, 8, 109376, 64748, 7159, 95825, 25463, 512, 1, 260, 278, 842301, 2314, 799360, 444663, 51398, 134, 5394, 8, 143246, 14304, 225, 293254, 0, 821504, 205, 89275, 8, 67654, 128, 8, 131072, 8, 4, 86777, 37, 686224, 256, 951536, 7, 128, 170680, 119651, 18, 31784, 43687, 286997, 2680, 148402, 6286, 2671, 1534, 421552, 9674, 4443, 2, 43522, 935, 168, 16, 2150, 8, 470600, 5002, 8, 1960, 337744, 5919, 16, 218752, 600001, 106304, 338375, 256, 128, 144745, 444, 993, 229673, 64, 14, 430, 16, 9302, 16, 142, 226, 64, 2, 828, 144, 692, 2, 348, 44, 711984, 3091, 95, 1047553, 52340, 444272, 2, 92, 210991, 9244, 204, 32370, 524288, 4, 8, 196, 443, 295394, 722128, 105352, 3616, 288, 505, 1, 94368, 1216, 24, 857523, 323788, 3, 2, 328, 52, 16, 350858, 2, 784, 151264, 10, 8, 10, 847970, 129656, 4, 88, 10, 52564, 2, 88, 913, 100, 72289, 504, 199840, 8, 262144, 1, 284714, 40, 117, 128, 4837, 121, 598721, 256, 1015809, 117232, 126, 1024, 2395, 64, 995, 870032, 57472, 131072, 60602, 2432, 8, 63375, 4, 399484, 7804, 45474, 75632, 147, 3, 0, 1326, 226, 608, 15, 579114, 19786, 3714, 295660, 484964, 2, 142792, 74, 9376, 1, 2, 2311, 589981, 1, 120, 26, 126, 47655, 0, 23040, 88717, 2464, 64, 32, 713, 2, 0, 32, 8, 480173, 28, 10, 65536, 85340, 97315, 1088, 256, 394018, 3872, 17956, 407, 32, 8, 7708, 2, 598552, 193504, 695957, 39934, 14199, 16, 80, 5, 128, 168, 6094, 20, 1, 18930, 112716, 151950, 28, 34427, 13, 4, 37832, 131072, 16, 4, 888544, 37504, 136558, 8726, 1, 8, 6028, 25, 193438, 3224, 0, 137720, 6970, 440812, 512, 15, 370, 65536, 20, 2686, 15424, 709, 206135, 783, 476, 4, 1, 379, 485468, 4170, 4, 16, 775373, 220, 88, 17000, 1024, 2048, 2, 524288, 404, 8, 190, 0, 141567, 0, 5176, 48, 164844, 524288, 51088, 0, 554894, 7, 24, 361780, 93142, 30, 94583, 618, 324, 10, 4, 512, 18, 0, 484, 6448, 217500, 131072, 204, 2, 1129, 16, 152150, 2048, 244291, 832, 942811, 321304, 70372, 262144, 8, 125549, 37802, 252, 32, 6264, 162, 227273, 2808, 1472, 813, 51014, 224, 0, 0, 524288, 8, 126697, 39306, 2, 120876, 118, 512, 507544, 189256, 19299, 7904, 356, 493216, 349484, 646266, 0, 16, 31650, 81, 21154, 512, 30896, 5420, 4, 598, 35912, 16, 8576, 960, 4, 152, 7807, 35580, 38119, 82976, 96, 114472, 4, 0, 190, 220, 491, 0, 3166, 117, 11051, 687927, 295362, 16, 256, 287684, 8727, 0, 8163, 1684, 131072, 65536, 262144, 10, 847027, 1676, 16, 0, 0, 1, 0, 0, 0, 0, 0, 1, 842624, 54688, 345, 0, 176, 88672, 2718, 1294, 82968, 131072, 70352, 17558, 84, 200, 65939, 28, 32, 147012, 73621, 131072, 52860, 118, 97608, 393, 31075, 84728, 11412, 2, 1696, 4, 65536, 605496, 1, 77415, 6, 64, 0, 7276, 128, 58, 22604, 34, 16, 161, 60213, 3903, 806192, 425228, 166814, 208, 416, 51, 2896, 3, 374496, 61421, 4, 496429, 2768, 19136, 128, 0, 88, 1, 52, 252, 24, 8, 28, 88, 586, 77344, 56946, 1384, 71, 0, 3576, 131072, 200, 4396, 68367, 1048575, 11785, 23, 879703, 98, 76, 2048, 18, 512, 44823, 524288, 41484, 1, 32768, 262144, 131072, 114304, 553152, 80408, 27431, 33676, 22845, 226, 514784, 2473, 1359, 939472, 42900, 6268, 16, 34814, 8, 898507, 983041, 16, 3134, 342, 56028, 74, 1, 156742, 797015, 32, 58, 32768, 1024, 3173, 54862, 16, 72, 3376, 57152, 8, 334716, 3392, 8794, 0, 16, 2, 1990, 7574, 371226, 172, 1656, 80105, 598592, 65536, 0, 4, 376566, 53753, 128, 0, 1, 46121, 189, 90167, 165464, 641166, 26, 0, 42062, 571348, 88395, 158, 391, 8, 73806, 14, 16, 88874, 60796, 58, 8340, 7086, 65536, 357261, 19637, 499446, 517406, 63172, 71157, 308309, 44, 196, 143672, 85936, 36095, 4, 80, 302459, 8730, 81073, 65536, 28531, 65536, 32, 131072, 2454, 20000, 3980, 6470, 7234, 31478, 30968, 128, 6758, 2, 8, 4, 394368, 2, 0, 41529, 1, 512, 0, 52, 66784, 50000, 16270, 64, 513706, 43990, 94336, 10, 64276, 131072, 4, 13216, 8, 928754, 4, 16, 44, 434, 32768, 25000, 1024, 64, 1048574, 42064, 0, 76789, 2, 40, 31074, 365381, 0, 0, 8972, 54037, 32768, 76576, 81408, 64, 68, 3015, 3568, 32008, 23420, 6262, 4, 62144, 31073, 18, 8, 45247, 2640, 82148, 173, 12, 2, 0, 19558, 372, 144, 234908, 60514, 3235, 48626, 684619, 16, 14, 96, 120, 72, 78472, 9868, 1048576, 438, 380, 93580, 11, 49960, 16, 496454, 26, 379898, 32, 17144, 58102, 65, 554688, 572628, 200639, 26008, 3128, 1, 9973, 512, 3976, 397136, 0, 2, 32, 88, 77, 4096, 1527, 196, 8978, 128, 1252, 848, 2, 481790, 14176, 452, 47856, 47, 16, 2, 31, 31876, 760040, 926108, 80335, 32768, 90415, 322, 444943, 376, 30, 384556, 182592, 4, 256, 36, 4, 12, 861056, 75942, 16, 262144, 16, 4, 16384, 57062, 164806, 0, 62112, 528756, 61739, 86493, 20, 163792, 18676, 351500, 8, 346584, 18, 203476, 228, 128]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(modp)