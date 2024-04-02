def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    
	Include these tokens in the code: s = sum
	Do not include these tokens in the code: assert ( is instance ( N ,
	"""
    # 1. split integer to list of integers
    # 2. convert each integer to binary
    # 3. sum all binary integers
    # 4. convert sum to binary
    # 5. return binary number
    # 6. use bin function
    # 7. use int function
    # 8. use str function
    # 9. use sum function
    # 10. use map function
    # 11. use list function
    # 12. use int function
    # 13. use str function
    # 14. use sum function
    # 15. use int function
    # 16. use str function
    # 17. use bin function
    # 18. use int function
    # 19. use str function
    # 20. use sum function
    # 21. use int function
    # 22. use str function
    # 23. use bin function
    # 24. use int function
    # 25. use str function
    # 26. use sum function
    # 27. use int function
    # 28. use str function
    # 29. use bin function
    # 30. use int function
    # 31. use str function
    # 32. use sum function
    # 33. use int function
    # 34. use str function
    # 35. use bin function
    # 36. use int function
    # 37. use str function
    # 38. use sum function
    # 39. use int function
    # 40. use str function
    # 41. use bin function
    # 42. use int function
    # 43. use str function
    # 44. use sum function
    # 45. use int function
    # 46. use str function
    # 47. use bin function
    # 48. use int function
    # 49. use str function
    # 50. use sum function
    #



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
    inputs = [[1000], [150], [147], [333], [963], [1], [10], [101], [1111], [5000], [9999], [819], [15], [75], [820], [818], [16], [1112], [17], [9998], [9997], [821], [2], [1110], [1113], [74], [11], [14], [10000], [100], [73], [27], [35], [817], [1114], [9996], [1115], [12], [18], [816], [13], [36], [28], [1109], [96], [97], [5001], [76], [1116], [9], [815], [822], [26], [814], [72], [4999], [95], [8], [102], [25], [3], [9995], [1107], [33], [19], [4], [1117], [20], [1118], [5], [24], [94], [23], [34], [77], [812], [4998], [6], [84], [4997], [813], [29], [103], [98], [78], [37], [83], [93], [21], [1108], [1119], [31], [1120], [9994], [85], [79], [7], [30], [71], [9993], [32], [52], [90], [91], [8888], [7777], [6666], [5555], [4444], [3333], [2222], [1010], [7776], [8889], [3332], [6667], [6668], [2223], [2224], [22], [7779], [3331], [7778], [5554], [6665], [6669], [2221], [8887], [5553], [4443], [7780], [57], [5556], [6664], [56], [5557], [5552], [3334], [6670], [4445], [2219], [2225], [60], [5551], [8886], [1009], [2220], [1011], [3330], [55], [2218], [5550], [58], [1012], [3329], [59], [7775], [6671], [6672], [2227], [8885], [70], [1007], [54], [1008], [2228], [2226], [5547], [4442], [2230], [2231], [1013], [5548], [7782], [44], [7783], [3328], [2232], [2233], [6673], [53], [5549], [2234], [69], [6663], [7774], [7773], [7772], [3335], [7771], [8884], [1014], [3336], [3337], [4441], [8883], [5558], [3327], [65], [66], [63], [7770], [5559], [5560], [7769], [5561], [8890], [3338], [8882], [8891], [7768], [62], [5562], [8881], [64], [7767]]
    results = ['1', '110', '1100', '1001', '10010', '1', '1', '10', '100', '101', '100100', '10010', '110', '1100', '1010', '10001', '111', '101', '1000', '100011', '100010', '1011', '10', '11', '110', '1011', '10', '101', '1', '1', '1010', '1001', '1000', '10000', '111', '100001', '1000', '11', '1001', '1111', '100', '1001', '1010', '1011', '1111', '10000', '110', '1101', '1001', '1001', '1110', '1100', '1000', '1101', '1001', '11111', '1110', '1000', '11', '111', '11', '100000', '1001', '110', '1010', '100', '1010', '10', '1011', '101', '110', '1101', '101', '111', '1110', '1011', '11110', '110', '1100', '11101', '1100', '1011', '100', '10001', '1111', '1010', '1011', '1100', '11', '1010', '1100', '100', '100', '11111', '1101', '10000', '111', '11', '1000', '11110', '101', '111', '1001', '1010', '100000', '11100', '11000', '10100', '10000', '1100', '1000', '10', '11011', '100001', '1011', '11001', '11010', '1001', '1010', '100', '11110', '1010', '11101', '10011', '10111', '11011', '111', '11111', '10010', '1111', '10110', '1100', '10101', '10110', '1011', '10110', '10001', '1101', '10011', '10001', '1110', '1011', '110', '10000', '11110', '1010', '110', '11', '1001', '1010', '1101', '1111', '1101', '100', '10001', '1110', '11010', '10100', '10101', '1101', '11101', '111', '1000', '1001', '1001', '1110', '1100', '10101', '1110', '111', '1000', '101', '10110', '11000', '1000', '11001', '10000', '1001', '1010', '10110', '1000', '10111', '1011', '1111', '10101', '11001', '11000', '10111', '1110', '10110', '11100', '110', '1111', '10000', '1101', '11011', '10111', '1111', '1011', '1100', '1001', '10101', '11000', '10000', '11101', '10001', '11001', '10001', '11010', '11010', '11100', '1000', '10010', '11001', '1010', '11011']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(solve)