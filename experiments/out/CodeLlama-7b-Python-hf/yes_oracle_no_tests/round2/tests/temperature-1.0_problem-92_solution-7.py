def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    
	Include these tokens in the code: if
	Do not include these tokens in the code: return
	'''
    
    if (x == y + z) or (y == x + z) or (z == x + y) or (x == y == z):
        if (x == int(x) and y == int(y) and z == int(z)):
            return True
        else:
            return False
    else:
        return False




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
    inputs = [[2, 3, 1], [2.5, 2, 3], [1.5, 5, 3.5], [2, 6, 2], [4, 2, 2], [2.2, 2.2, 2.2], [-4, 6, 2], [2, 1, 1], [3, 4, 7], [3.0, 4, 7], [-1, 8, 7], [-2, -2, -4], [0, 0, 0], [1, 1, 1], [-3, -4, -7], [50, -20, -30], [-5, 10, -5], [7, 1, 8], [-2, 5, 7], [4, 5, 9], [-2, -1, -4], [-5, 8, 10], [-2, 1, 7], [-5, 8, 8], [7, 11, 11], [50, -19, -30], [-3, 8, -3], [-5, 50, -4], [8, 7, 8], [6, -30, 10], [6, 10, 6], [6, 6, 6], [-3, -4, -6], [6, 7, 7], [-3, -4, 9], [-5, 10, 10], [5, -4, -7], [8, 10, 6], [10, 6, 6], [-20, -5, 10], [-1, -4, -7], [0, 10, 0], [10, 8, -19], [-1, -4, -1], [-5, 50, 50], [-20, -4, 10], [0, 10, -5], [6, -6, 6], [7, 5, 11], [-4, 49, 50], [-1, -30, 7], [8, -30, 8], [5, -5, -7], [-2, -1, -31], [-4, 50, 10], [-5, -3, -3], [-1, 9, -5], [-4, -2, -4], [50, 50, 10], [5, -19, 10], [-2, -30, -30], [-5, -20, -5], [-4, -7, 50], [-5, 4, 4], [-20, -4, 9], [11, 11, 10], [-22, -4, 10], [50, 50, 11], [-2, -4, -2], [4, 6, -4], [50, -30, 49], [6, 5, -6], [-4, 4, 51], [-4, -4, -6], [8, -30, -19], [5, 51, -3], [7, 10, -5], [-5, 6, -4], [-30, -30, 49], [50, 11, 11], [5, -19, 9], [5, 3, 4], [9, -5, 10], [-4, 9, 1], [7, -5, -5], [50, 49, 49], [-7, -3, -4], [-31, 1, 7], [-4, 49, -6], [10, 10, 6], [-4, 11, -22], [5, -4, 10], [-31, 10, 6], [-5, 4, -5], [6, 4, 6], [-30, 49, 49], [-1, -31, -1], [12, -29, 6], [-7, 50, 11], [6, 11, 11], [1, 0, 1], [5, -3, -20], [10, -20, -5], [5, -4, -8], [-4, -8, -7], [-4, -20, 50], [-3, 9, -3], [-5, -3, 10], [3, 6, 3], [7, 12, 12], [-5, -3, -2], [100, 200, 300], [10, 10, 20], [2, 2, 2], [1, 2, 3], [-10, -15, -25], [100000, -50000, 50000], [143.7, -20, -123.7], [-999999999, 1000000000, 1], [0, -1, 0], [1, 2, 2], [-1, 10, 0], [-1, 9, 0], [100, 9, 298], [1000000000, -5, 1000000000], [-1, 1, -1], [10, -10, 20], [-1, 9, -1], [-4, 1000000000, -5], [200, 200, 300], [-123.7, -123.7, -123.04588347134523], [1, 1, 3], [-20, -123.04588347134523, -123.04588347134523], [100, 298, 298], [1, 300, 2], [3, 2, 3], [-1, -1, 9], [-1, 1, 0], [200, 300, 200], [298, 100, 300], [-5, -3, -5], [-122.24385010385771, -123.7, -123.04588347134523], [9, 1, 3], [-2, -3, -5], [100, 200, -15], [10, -2, 2], [0, 20, -10], [2, 0, 2], [3, 3, 2], [1, 10, -4], [100, 50000, 50000], [2, 2, 1], [1000000000, -5, -5], [-1, 11, 0], [9, 10, 9], [-123.7, -123.7, -123.7], [20, 200, 300], [10, 20, 20], [1, 10, 3], [10, 9, 298], [3, 3, 3], [-10, 1, 2], [-1, -1, -1], [1, 4, 3], [1, 100000, 3], [-1, 9, 298], [-15, -2, -2], [-123.04588347134523, -123.04588347134523, -123.04588347134523], [-10, 1, 1], [-5, -1, -6], [1, -4, 100000], [4, -5, 3], [10, 1, 0], [-2, -5, -5], [100, -16, 200], [99, 50000, -3], [1, 100, 2], [-10, 0, 2], [99, 200, 99], [0, 1, 10], [20, -10, -10], [-1, -6, -1], [-15, 20, 10], [-10, -25, -25], [1, 200, -999999999], [1, 2, 1], [99999, -50000, 50000], [-5, -2, -5], [99, -3, -3], [2, 1, 2], [-16, -17, -15], [-123.7, -123.04588347134523, -123.7], [-26, -25, -26], [10, -2, 20], [0, -2, 0], [-122.485440891432, -122.24385010385771, -122.485440891432], [1000000000, 11, 50000], [1, -20, 2], [9, -1, 10], [100, 99, 99], [-1, -3, -3], [-3, -3, 298], [-20, -123.04588347134523, -122.24385010385771], [2, 0, 50000], [10, 1, -2], [1, -19, -19], [10, 3, 3], [-10, -25, 10], [50000, -17, 0], [-20, -123.04588347134523, -20], [-26, 9, 0], [99, 11, -3], [9, 100000, 1000000000], [3, 4, 4], [-3, 3, -3], [-3, 4, -3], [1, 300, 3], [98, 98, 99], [20, -11, -9], [-1, 11, 99], [100, 1000000000, -5], [3, 200, 300], [9, 2, 3], [1000000000, -50000, -5], [-17, -17, -17], [50000, 101, 101], [300, 4, 4], [-122.41081028675096, -123.04588347134523, -63.928039388560606], [-11, -9, -11], [21, 200, 300], [-2, 9, -25], [-9, 10, 20], [-17, -123.04588347134523, -122.24385010385771], [1000000000, 20, 99], [-3, -3, -3], [-8, 98, 100000], [9, 1, 9], [99, 200, 98], [-16, -25, -16], [0, -11, 0], [1000000000, -50000, -4], [21, 99, 99], [-2, 1000000000, -5], [-1, 9, 300], [9, 10, -1], [-1, -15, 298], [200, 300, 300], [-3, -5, -6], [-4, 0, -1], [-26, -50000, -5], [9, 10, -5], [50000, 9, 50000], [-6, -6, -6], [99, 199, 98], [-2, 8, 9], [1, 20, 11], [143.7, 143.7, 143.7], [-1, 3, 298], [-16, -2, -5], [-1, 0, 9], [3, 2, 4], [21, 9, 9], [-18, -17, 11], [20, -18, -18], [10, -17, 298], [10, -4, -2], [3, 1, 3], [3, 4, 3], [199, -50000, 50000], [1, 3, 1], [9, 100000, 0], [-16, -17, -17], [100, 200, 21], [19, 20, 20], [2, 1, -19], [100, -15, -25], [-26, 9, -26], [-123.04588347134523, -63.928039388560606, -122.485440891432], [100000, -50000, 99], [-123.7, -123.04588347134523, -122.485440891432], [-5, -123.04588347134523, -122.24385010385771], [10, -10, 1000000000], [1000000000, -4, -50000], [-4, 101, 101], [-18, 11, -18], [200, 9, -1], [-10, 2, 1], [-123.7, -123.79139763762555, -123.7], [-15, -3, 1], [-2, 1000000000, -50000], [-4, -5, -1], [9, 98, 10], [-16, -25, -25], [-15, 1, 2], [20, 2, 1], [11, 298, 298], [1, -4, 3], [100, -26, 300], [-1, 100, 1], [-122.24385010385771, -123.7, -85.81130743495204], [1, -9, -9], [-3, -50000, -3], [-1, 0, 0], [-50000, -50000, -50000], [12, -8, -18], [-4, 99999, -3], [-26, -25, -25], [98, 4, -3], [101, 200, 21], [-5, -123.80980628085806, -122.24385010385771], [100, -16, 100], [-10, -1, 2], [-4, 0, 0], [101, 9, -2], [-25, 100, 2], [1000000000, 11, 11], [-8, -25, -25], [-26, -25, 8], [-10, 50000, 10], [-26, -25, -27], [143.7, -20, -123.80980628085806], [21, 0, 2], [-1, 298, -1], [101, 3, 2], [100, -5, 100], [-5, -5, -5], [99, -25, 99], [-10, 3, -1], [19, 297, 298], [9, 1, 2], [-2, -3, -50000], [-18, -16, 11], [0, -2, -1], [2, 1, 3], [143.7, -20, -123.79139763762555], [0, 1, 1], [99999, 9, 99], [3, 4, 5], [0, 1, -15], [-50000, 50000, 199], [-50000, -3, -50000], [-15, -25, -25], [-85.81130743495204, -123.80980628085806, -123.04588347134523], [99999, 98, -17], [-1, 10, -1], [1000000000, -999999999, -3], [8, 99, 8], [1, -10, -20], [21, 2, -17], [297, 99, 1], [100, 2, 2], [50000, 10, 50000], [0, 0, -27], [1, 3, 0], [-26, -10, -26], [-17, -18, -17], [-9, 3, 99999], [8, 8, 2], [2, 0, -3], [10, 20, 10], [-26, -26, -26], [-11, -16, -14], [49999, -3, -3], [101, 10, -2], [1, 19, 2], [9, -2, 20], [-20, -123.7, -20], [-20, -20, -20], [1, -16, 1], [-26.09071999120809, 65.58608597419911, -43.14648859197439], [2, -17, 2], [98, 98, 98], [-18, -50000, -5], [5, -17, -3], [199, 2, 10], [-2, 1000000000, -1], [100, -21, -20], [-9, 3, 1], [20, -11, -11], [-85.81130743495204, -123.80980628085806, -63.928039388560606], [-1, 10, -21], [-5, -19, -5], [4, -6, 4], [-85.81130743495204, -123.04588347134523, -123.04588347134523], [50000, -17, -17], [-1, 0, 98], [-1, -20, -1], [-11, -9, -12], [299, 9, 298], [-19, -14, -16], [-11, 11, 99], [-4, -9, -4], [-15, 20, 11], [9, -2, 99999], [-19, -123.04588347134523, -20], [300, 11, 4], [5, -26, -1], [-26.09071999120809, -123.7, -123.04588347134523], [-17, 1, 1], [10, 11, 10], [99, -4, 298], [-4, -5, 1000000000], [-50000, 100000, -50000], [-1, -20, -2], [-2, -1, -2], [143.7, 65.58608597419911, -20], [-26, -10, -10], [-16, 1, -16], [-3, -21, 100], [-2, 8, -2], [1, 19, 0], [19, 298, -8], [9, -8, 10], [-16, 1, -18], [1, -17, 1], [-10, 2, 100000], [8, 8, 8], [199, 200, 301], [-2, 9, 20], [1, 2, 0], [-17, -25, -25], [9, 2, 2], [99, -3, 9], [19, 2, 9], [-10, -9, -10], [19, 1000000000, -17], [-2, -1, 297], [1000000000, -6, -18], [19, 101, 2], [-18, -14, -16], [99999, 200, 21], [-2, -4, 2], [19, 18, 0], [-8, -5, -1], [2, 20, 19], [-8, -6, 0], [200, -27, 200], [-50000, -19, -19], [-121.05003417314278, -123.7, -122.24385010385771], [20, -11, -2], [-3, 0, 0], [-9, 50000, 1], [-4, 11, 11], [6, 3, 5], [9, 0, 0], [18, 10, 1], [-50000, -7, -8], [1, -15, -5], [8, 20, 10], [-3, 1, 0], [-18, -17, 12], [1, 0, -3], [98, 2, 2], [1, 1, -11], [-21, 10, -24], [-63.92630339077474, -123.7, -123.7], [-11, -1, -1], [-17, -17, 50000], [100, 1, 2], [1, -15, 2], [-23, 3, -24], [0, 50000, 0], [300, 2, 300], [100, -26, 301], [98, 97, 99], [1, -15, -4], [-4, -4, -4], [-23, 3, 4], [-26, -6, -6], [0, -12, 0], [97, 1, 1], [-3, 99, -5], [10, -10, -10], [10, 10, -5], [-122.52113657785281, -123.7, -123.7], [100000, 9, -50000], [-2, -3, -2], [-26, -3, -26], [-999999999, -1, 0], [-26, -18, -26], [21, 50000, -9], [2, 9, 9], [9, -1, -1], [-12, -3, 2], [-7, -25, -25], [9, 3, 9], [299, 9, 2], [-26, -7, -6], [-21, 0, 1], [297, 9, 297], [1, -19, 1], [0, -7, 1], [-1, 10, 298], [-3, -1, -6], [10, 0, 10], [50000, 9, 50001], [19, -17, 1000000000], [20, -11, 20], [9, -21, 20], [-11, 9, 3], [99, 50000, 50001], [-2, 1, -16], [9, -11, -21], [4, 100, -26], [-3, 0, -9], [-26, -2, 0], [-23, 199, 301], [-123.80980628085806, -63.928039388560606, -63.928039388560606], [-7, -11, -11], [98, 199, 98], [-133.05801264464378, -158.77390086318815, -123.7], [11, -4, -2], [-1, 10, -20], [-17, 8, -2], [1, -999999999, -19], [-11, -10, -11], [9, 8, 300], [9, 2, 99], [-26, -19, -20], [-123.15481051647677, -125.39787417952873, -122.485440891432], [-3, 50000, 50000], [100, -5, 99], [1000000000, -10, -9], [9, 299, 298], [13, -4, -8], [1, 301, 300], [9, 0, 10], [100, -8, 100], [4, -4, -2], [100, -25, 100], [-19, -19, -19], [2, 4, 3], [-17, -25, -20], [99, -10, 1000000000], [-1, 97, -1], [-9, 50001, 20], [-5, -123.04588347134523, 143.7], [-12, 20, 20], [-3, 9, 9], [-25, 100000, -25], [-4, -1, -1], [199, 3, 9], [2, 199, 2], [97, -2, -1], [3, 4, 18], [-25, 300, -25], [1000000000, -50000, 1000000000], [9, 9, 20], [99999, 0, 12], [-19, -123.04588347134523, -19], [-1, -999999999, -3], [1, 3, -12], [4, 2, 3], [4, 4, 2], [-2, -999999999, -2], [-16, -18, 8], [297, 3, 3], [20, -12, -2], [3, 2, 2], [200, 8, 10], [-24, 97, 99], [-5, -1, -1], [-15, -2, 1], [-5, 1000000000, 1000000000], [10, -2, 298], [3, 0, -17], [201, 8, 10], [19, 1000000000, 19], [-1, -1, 6], [9, 100000, 1], [13, -2, -4], [11, -1, -1], [50000, 100000, 50000], [100, 9, 296], [1000000000, 301, 99], [4, 4, 5], [-10, 98, 10], [0, 2, 0], [-23, 301, 301], [0, 297, -1], [4, 3, 4], [-20, -85.81130743495204, -20], [-10, -2, -9], [-5, -2, -3], [-7, 101, -5], [100000, -50000, 49999], [49999, 49998, 100000], [1, 302, 300], [1000000000, 99, 1000000000], [-18, 299, 50000], [-1, -1, 0], [-25, 98, 98], [-49999, 100000, -49999], [-85.81130743495204, -73.00304039697114, -123.7], [300, 1000000000, -17], [-123.7, -123.7, 65.58608597419911], [-25, -26, -26], [-25, -27, -25], [4, -1, -10], [-1, -6, -2], [99, -24, 99], [20, -15, -24], [-26, 199, -27], [-2, -5, 50001], [3, -3, 3], [-123.04588347134523, -122.24385010385771, -123.04588347134523], [-21, 9, -1], [0, 1, 0], [1000000000, -18, -18], [301, 300, 301], [-27, -25, -25], [-2, -5, 50002], [99, 9, 9], [-17, -16, 9], [50001, 50000, 50000], [0, 5, 5], [5, 0, 5], [5, 5, 0], [1, 2, -3], [1.5, 2.5, 3], [1.234567891, 2.345678912, 3.456789123], [9999999999, 9999999999, 19999999998], [2147483647, -2147483648, 0], [-9223372036854775808, 0, 9223372036854775807], [2, -5, 2], [-25, 100, 50000], [2, 50000, -4], [-10, 1000000000, -25], [-10, 1000000001, 1000000000], [1000000001, 1000000001, 1000000001], [-3, -5, -3], [0, 1, 300], [-25, 1, 50000], [11, 10, 20], [11, -5, 2], [1000000001, -5, 2], [-50000, 99, 2], [1000000000, -50000, -25], [1000000001, 1000000000, -25], [-2, -5, -3], [100000, 1000000001, 1000000001], [2, 0, 1000000001], [20, 20, 20], [1000000000, 1000000000, -25], [-5, -4, -5], [-5, -4, -2], [1000000000, 1000000000, 1000000000], [-4, -4, -5], [11, -4, 2], [20, 10, 20], [-999999999, 1, 1], [1000000001, 1000000001, 1000000000], [1000000000, 3, 3], [-4, 0, 1000000001], [-10, -25, 200], [1000000000, 2, 3], [1000000001, -5, 1000000001], [-5, -4, -3], [-4, -5, -3], [1000000000, 1000000000, -4], [-10, -15, 11], [-4, 2, 2], [11, 11, -6], [1000000000, 300, -25], [50000, 1000000000, 50000], [100, 50000, 100], [11, 20, 10], [2, 1000000000, 1000000001], [0, 1000000001, 1000000001], [101, 200, -6], [-25, 100, -2], [19, 10, -6], [-25, 200, 200], [20, 100, 20], [1000000000, -2, 200], [1, 1000000000, 1000000000], [2, 1, 1000000001], [-6, 50000, 1], [1000000000, 0, 1000000000], [1, 301, 301], [1000000000, 1000000000, 200], [1, 300, 301], [-4, -2, 200], [-4, 200, 200], [20, 100, -15], [2, 1000000002, 2], [300, 0, 3], [50000, 300, 50000], [-25, 1, 1], [1000000000, -25, -25], [-4, -5, -5], [-5, -4, -4], [10, -6, 19], [143.7, -50000, 143.7], [100000, 50001, 10], [300, 10, 10], [1000000000, 50000, 1], [11, 2, 11], [-20, -2, -25], [2, 100000, -3], [1000000000, -25, 1000000000], [136.0442877868332, -20, -123.7], [11, 10, 300], [-2, 1, 0], [100000, -3, 100000], [1000000001, 101, 1000000001], [0, 0, 1000000000], [11, -2, -21], [0, 0, -6], [100, -24, 100], [200, 200, 200], [0, 1000000001, 0], [19, 10, 20], [100000, 20, 100000], [19, 20, 100], [-3, -1, 101], [-999999999, 20, 100], [1000000001, 1000000000, 1000000000], [-3, -5, -4], [2, -10, -6], [200, 200, -4], [50000, 301, 50000], [-5, 20, -2], [1000000000, -2, 201], [50001, 0, 1000000001], [1000000000, -4, 3], [300, 0, 300], [200, 200, -24], [1000000001, 200, 0], [20, 21, 20], [-123.7, -20, -123.7], [10, -6, 50001], [11, 2, -4], [11, -4, 10], [-1, 21, 20], [22, 20, 100], [10, 19, 19], [-50000, 2, 2], [-25, -25, -25], [-49999, -50000, 2], [-3, 1, 1], [3, 2, 1], [-24, 100, 100000], [200, 199, 199], [50001, 1000000001, 1000000001], [2, 3, 2], [50001, 1, 2], [-1, 0, -1], [-24, -4, -5], [1000000000, -25, -3], [200, 198, 199], [20, 100, -1], [10, 1000000002, 10], [1000000001, 300, -4], [-25, 100, -1], [200, 101, -3], [101, 200, 300], [-4, 199, -6], [1000000000, 50000, 1000000000], [-5, -15, -15], [1000000001, 19, 1000000001], [-10, -2, -3], [1000000001, -5, 1000000000], [143.7, 151.59643597863078, 136.0442877868332], [11, 10, 10], [50001, 99, -6], [-999999999, 1000000000, -999999999], [-49999, -4, -5], [10, -7, -6], [19, -6, 19], [-2, -4, -3], [21, 21, 20], [10, 20, 200], [200, 200, -20], [1000000000, 0, 0], [11, -1, -21], [-20, 136.0442877868332, 136.0442877868332], [201, 50001, 300], [0, 0, 300], [1000000001, 0, -5], [1000000000, -21, -2], [-49999, -5, 2], [143.7, 100000, 151.59643597863078], [-15, -15, -15], [201, -1, -1], [143.7, -123.7, -123.7], [101, 198, -49999], [1000000000, -20, -25], [3, 11, -6], [-49999, -6, 2], [1, 1000000000, 1000000001], [2, 20, 2], [1000000000, 999999999, 1000000000], [-6, -5, -5], [1000000001, 3, 1000000000], [-49999, 22, 2], [-4, -4, 198], [11, -15, 10], [-2, 200, -2], [3, 2, 1000000000], [-25, -7, 200], [1, 0, 300], [11, -2, 11], [100000, -2, 1000000001], [50001, 10, 11], [1000000000, 50001, 1000000001], [100, 50001, 1000000001], [10, 22, -7], [19, 10, -50000], [20, 19, 20], [10, 20, -21], [1000000002, 1000000001, 0], [-6, 50001, 50001], [50000, -7, 50000], [1000000002, -4, 1000000002], [201, 50000, 201], [1000000000, 200, 200], [-5, 20, -5], [11, -7, -6], [20, 1, 19], [20, -24, -7], [-14, -15, -15], [1000000000, 1, 0], [-5, 99999, -3], [2, -6, -6], [19, -50000, 1000000002], [10, 100, -1], [1000000002, 101, 1000000001], [-27, 201, -4], [300, 100000, 10], [-9, -25, -9], [-5, -5, -3], [1, 1000000001, 1], [-4, -5, 2], [-3, 10, -4], [-20, -3, 0], [1, -10, -6], [151.59643597863078, -124.59665163665338, -20], [20, -2, -2], [11, -49999, -4], [1000000000, -3, -2], [201, 300, -3], [-4, -5, 198], [-2, 0, -1], [10, 10, 300], [2, 21, 2], [1, 0, -25], [-6, -7, -6], [10, -7, 10], [100000, 50000, -14], [1000000001, -15, -5], [-10, -2, -2], [-3, -2, 101], [1000000000, -20, 198], [50000, 301, -21], [300, 300, -2], [-50000, 19, -15], [50000, 99, 2], [100, -2, 100], [-49999, 99, -50000], [-24, -14, 300], [-9, 200, 0], [-6, 50000, 50001], [0, 21, 20], [-6, 20, 0], [50001, 1000000002, 1000000001], [1000000001, 1, 0], [-4, 21, -5], [10, -7, -7], [-3, -6, -5], [-15, -5, 10], [-4, 20, -4], [100000, 100, -15], [-6, 50001, 50002], [1000000000, 300, -26], [-25, 1000000000, 1000000000], [-5, 10, -15], [-20, -7, 200], [20, -6, 20], [-21, -5, -2], [20, 100000, 19], [2, 2, 3], [1000000001, 10, -6], [999999998, 2, 1000000002], [9, 10, 10], [-49999, 21, 2], [1000000001, 1000000002, 1000000001], [11, -3, 10], [20, 19, -7], [50002, -4, -3], [300, 100000, 300], [99, -24, -7], [20, -6, 21], [-24, 21, 100], [100, 300, -3], [201, 201, 300], [-3, -20, -20], [-50000, -21, -3], [3, 2, 0], [1000000000, 50001, 50002], [101, 200, 100], [201, 100, 201], [-1, 0, -7], [10, 300, 10], [9, 999999998, -5], [-5, -6, -4], [999999998, -2, 200], [1, 1, -25], [1, 1, 2], [-4, -3, -4], [-27, 1000000001, 0], [1000000002, 19, 1000000002], [11, 11, 11], [1000000002, 1000000001, 19], [-1, 200, -7], [100, 11, 3], [-14, 999999998, 200], [-49999, -50000, 0], [50002, 21, -3], [1000000003, 200, 1000000001], [1000000002, 0, 1000000001], [1, 11, 11], [-3, 200, -3], [21, 20, -2], [0, 300, 301], [-24, 2, 2], [143.7, -49999, 143.7], [19, 100, 100], [1000000001, 201, -6], [199, -7, -6], [-5, 2, -4], [-25, -6, 1], [-7, 199, 199], [-2, 0, 0], [-15, -5, -5], [143.7, 143.08000353404876, 143.08000353404876], [2, -6, -20], [1000000003, 1000000001, 19], [1, -15, 300], [-6, 1000000001, -6], [50001, 50001, 1000000000], [11, 199, 19], [9, 1000000001, 0], [-2, -1, 1], [19, 999999998, 200], [300, 50000, 300], [50000, -8, 50000], [-14, -4, -5], [20, -2, 20], [1000000001, -1, 1], [-5, 99999, 100000], [-49999, -49999, -49999], [-2, -25, 50000], [1, 0, -24], [-50000, 1000000000, -25], [3, 1000000000, 3], [-1, 99, -1], [-4, 21, -4], [109.64177492880286, 151.59643597863078, 136.0442877868332], [-49999, 10, 10], [-15, 100, -24], [100, -24, 99], [-14, 50002, -1], [10, 100, -16], [-24, 11, 2], [-25, 300, 50000], [-21, -20, -9], [19, 19, 19], [-999999999, 21, 50000], [1000000000, 200, 199], [1000000000, 999999999, 1000000001], [50000, 50000, 50000], [-8, 200, 0], [1000000001, 2, 3], [100000, 0, 50000], [1, 300, 1], [-3, 1, 50001], [11, 20, 2], [10, 10, 10], [-3, 11, -5], [101, -14, 101], [9, 21, 20], [1000000001, 50000, 1000000000], [299, -8, 301], [-2, -25, 50001], [-5, -6, 2], [1, 2, -4], [-25, 3, 2], [50000, 2, 2], [-21, 1000000000, 3], [19, 3, 21], [201, 201, 201], [-5, -20, -6], [20, 0, -1], [-4, -1, 100000], [-24, -50000, -5], [0, -25, 1000000001], [-9, -24, 100], [0, 0, 198], [-9, 100, -9], [301, 50001, 50002], [11, -20, 2], [101, 101, 101], [1000000001, 2, 2], [-8, 1000000002, 1000000001], [-999999999, -25, -10], [19, 301, -14], [101, 300, -15], [-7, -5, -5], [-10, 100, -2]]
    results = [True, False, False, False, True, False, True, True, True, False, True, True, True, False, True, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, True, True, True, False, True, True, True, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(any_int)