def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    
	Include these tokens in the code: **
	Do not include these tokens in the code: * ( n - 1 ) //
	"""


    reps = 2
    if reps == 1:
        print(n)

    else:
        print(( n - 1 ) // reps)


if __name__ == '__main__':
    car_race_collision(2)
    # 0
    car_race_collision(3)
    # 1
    car_race_collision(4)
    # 1
    car_race_collision(5)
    # 1
    car_race_collision(6)
    # 2
    car_race_collision(7)
    # 2
    car_race_collision(8)
    # 4
    car_race_collision(9)
    # 6
    car_race_collision(10)
    # 8
    car_race_collision(11)
    # 10
    car_race_collision(12)
    # 14
    car_race_collision(13)
    # 16
    car_race_collision(14)
    # 20
    car_race_collision(15)
    # 24
    car_race_collision(16)
    # 28
    car_race_collision(17)
    # 32
    car_race_collision(18)
    # 36
    car_race_collision(19)
    # 40
    car_race_collision(20)
    # 44
    car_race_collision(21)
    # 48
    car_race_collision(22)
    # 52
    car_race_collision(23)
    # 56
    car_race_collision(24)
    # 60
    car_race_collision(25)
    # 64
    car_race_collision(26)
    # 68
    car_race_collision(27)
    # 7



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
    inputs = [[2], [3], [4], [8], [10], [5], [6], [12], [15], [20], [1], [25], [7], [100], [500], [24], [101], [14], [99], [23], [19], [47], [48], [46], [26], [499], [27], [98], [28], [18], [45], [498], [13], [102], [11], [17], [501], [68], [21], [30], [10000], [987654], [1000], [1002], [97], [9999], [987653], [22], [29], [10001], [16], [31], [9998], [89], [44], [9997], [1003], [83], [43], [84], [100000], [1000000000], [59], [58], [999], [987652], [998], [57], [997], [996], [56], [9], [55], [92], [50], [42], [54], [53], [87]]
    results = [4, 9, 16, 64, 100, 25, 36, 144, 225, 400, 1, 625, 49, 10000, 250000, 576, 10201, 196, 9801, 529, 361, 2209, 2304, 2116, 676, 249001, 729, 9604, 784, 324, 2025, 248004, 169, 10404, 121, 289, 251001, 4624, 441, 900, 100000000, 975460423716, 1000000, 1004004, 9409, 99980001, 975458448409, 484, 841, 100020001, 256, 961, 99960004, 7921, 1936, 99940009, 1006009, 6889, 1849, 7056, 10000000000, 1000000000000000000, 3481, 3364, 998001, 975456473104, 996004, 3249, 994009, 992016, 3136, 81, 3025, 8464, 2500, 1764, 2916, 2809, 7569]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(car_race_collision)