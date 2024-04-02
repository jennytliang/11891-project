def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    
	Include these tokens in the code: return ( n +
	"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


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
    inputs = [[1], [6], [11], [30], [100], [2], [3], [4], [7], [15], [20], [25], [50], [75], [1000], [14], [5], [16], [26], [92], [19], [93], [94], [999], [51], [17], [21], [22], [8], [74], [52], [23], [91], [76], [24], [90], [18], [13], [27], [998], [55], [65], [66], [73], [89], [56], [57], [997], [996], [77], [28], [87], [88], [72], [54], [53], [86], [85], [78], [67], [29], [58], [79], [995], [49], [71], [994], [59], [37], [80], [48], [47], [38], [64], [60], [992], [40], [993], [81], [12], [84], [39], [9], [63], [10], [83], [62], [991], [61], [36], [45], [35], [68], [990], [1001], [69], [95], [34], [70], [96], [1000000], [500000], [532178], [215], [217], [214], [216], [499998], [532179], [499995], [213], [499997], [499999], [43], [212], [532177], [499996], [999999], [500001], [499994], [1000001], [532180], [999998], [44], [532181], [500002], [42], [1000002], [999997], [218], [532182], [1000003], [46], [1000004], [41], [211], [999996], [532176], [219], [220], [500003], [532183], [499993], [532184], [532175], [500004], [1002], [532174], [210], [209], [499992], [532173], [1003], [532185], [221], [82], [1000005], [1000006], [1004], [1005]]
    results = [1, 21, 66, 465, 5050, 3, 6, 10, 28, 120, 210, 325, 1275, 2850, 500500, 105, 15, 136, 351, 4278, 190, 4371, 4465, 499500, 1326, 153, 231, 253, 36, 2775, 1378, 276, 4186, 2926, 300, 4095, 171, 91, 378, 498501, 1540, 2145, 2211, 2701, 4005, 1596, 1653, 497503, 496506, 3003, 406, 3828, 3916, 2628, 1485, 1431, 3741, 3655, 3081, 2278, 435, 1711, 3160, 495510, 1225, 2556, 494515, 1770, 703, 3240, 1176, 1128, 741, 2080, 1830, 492528, 820, 493521, 3321, 78, 3570, 780, 45, 2016, 55, 3486, 1953, 491536, 1891, 666, 1035, 630, 2346, 490545, 501501, 2415, 4560, 595, 2485, 4656, 500000500000, 125000250000, 141606977931, 23220, 23653, 23005, 23436, 124999250001, 141607510110, 124997750010, 22791, 124998750003, 124999750000, 946, 22578, 141606445753, 124998250006, 499999500000, 125000750001, 124997250015, 500001500001, 141608042290, 499998500001, 990, 141608574471, 125001250003, 903, 500002500003, 499997500003, 23871, 141609106653, 500003500006, 1081, 500004500010, 861, 22366, 499996500006, 141605913576, 24090, 24310, 125001750006, 141609638836, 124996750021, 141610171020, 141605381400, 125002250010, 502503, 141604849225, 22155, 21945, 124996250028, 141604317051, 503506, 141610703205, 24531, 3403, 500005500015, 500006500021, 504510, 505515]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(sum_to_n)