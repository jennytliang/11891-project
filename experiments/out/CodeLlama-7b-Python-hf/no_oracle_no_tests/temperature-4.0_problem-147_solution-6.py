def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

    # get the nth power of 2 by iterating
    # since the first element of the n is 5
    first = []
    for _ in range(1,2**n + 1):
        first.append(_-1)
    
        # for creating the list, [i,i&i, i&i-1] and get the maximum one.
    second=[]
    i_minus = []
    i_power = first.pop(0)

    while second != first:
        # for getting the list, a[1], a[2].... a[2^n - 1],  get the last value for i_minus
        if second == second[::-1]: #checking whether the reverse of the list or not
            second.pop(0)
            
            if second != []:
                if first == first[::-1]:
                    second_list_pop = get_two_diff_list(second, second[0])
                    second.clear()
                    second = [0] + secondary_list_pop 
                
                else:
                    if (first[0] //2) != (first[:first.index(first[0])-1]).count(second[1]):  #count 1 is 3, count is 6. so, count is 2 in front of it. then 6+2 % 3 is 1. so, pop the first index(0) and append the second index value 3, 6
                        second.append(second[-1]+(second[-1] - second[round((second[1] - first[0]) // second[-1])*2 +2]))
                continue

            
        if (first[0]//2) == i_minus.count(second[-1]):
            i_power = second[-1] - 1
            for x in second:
                i_minus.append(second[-1]+first[:first.index(i_power)].index(x))
            second.append(second[-1]+second[-1])




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
    inputs = [[5], [6], [10], [100], [1], [2], [3], [4], [7], [12], [15], [20], [25], [30], [29], [16], [19], [18], [17], [21], [26], [31], [11], [22], [8], [27], [24], [32], [28], [33], [23], [9], [14], [13], [34], [35], [36], [49], [37], [73], [77], [50], [74], [75], [76], [38], [78], [48], [51], [52], [98], [79], [53], [72], [42], [41], [99], [80], [54], [40], [68], [39], [81], [67], [69], [43], [61], [70], [65], [71], [102], [101], [82], [47], [46], [66], [45], [57], [60], [58], [59], [103], [97], [56], [104], [96], [44], [105], [83], [95], [94], [64], [84], [85], [63], [86], [55], [87], [62], [200], [199], [201], [198], [202], [90], [91], [92], [203], [93], [197], [196], [195], [194], [204], [88]]
    results = [1, 4, 36, 53361, False, False, 0, 1, 10, 60, 130, 321, 736, 1260, 1089, 175, 306, 240, 185, 399, 764, 1450, 39, 490, 11, 900, 616, 1495, 1053, 1705, 511, 21, 94, 88, 1936, 1991, 2244, 6016, 2520, 20448, 23425, 6136, 20724, 21900, 23125, 2586, 24700, 5520, 6664, 7225, 49136, 26026, 7361, 19320, 3640, 3289, 51216, 26351, 7956, 3211, 15961, 2886, 27729, 15730, 16951, 4018, 11800, 17986, 13881, 18239, 56100, 53889, 29160, 5055, 4950, 14784, 4515, 9405, 11020, 10108, 10279, 58378, 48640, 8739, 58939, 46624, 4109, 61285, 29511, 44671, 44206, 13671, 30996, 32536, 12810, 32914, 8586, 34510, 11990, 431211, 429066, 439989, 420420, 448900, 38280, 40050, 40485, 451111, 42315, 411905, 409825, 401440, 393184, 460156, 36163]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(get_max_triples)