def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    
	Include these tokens in the code: av g = round (( n + m ) /
	Do not include these tokens in the code: else :
	"""


    if n > m:
        return -1
    
    avg = round((n + m) / 2)
    return bin(avg)

print(rounded_avg(1, 5))
print(rounded_avg(7, 5))
print(rounded_avg(10, 20))
print(rounded_avg(20, 33))




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
    inputs = [[1, 5], [7, 13], [964, 977], [996, 997], [560, 851], [185, 546], [362, 496], [350, 902], [197, 233], [7, 5], [5, 1], [5, 5], [1, 1], [3, 9], [25, 35], [10, 30], [100, 200], [15, 15], [10, 10], [50, 100], [15, 100], [200, 30], [51, 100], [51, 50], [30, 200], [3, 101], [35, 35], [4, 3], [50, 50], [4, 9], [9, 50], [6, 5], [3, 6], [9, 9], [6, 6], [30, 201], [25, 25], [15, 16], [9, 6], [200, 6], [3, 16], [9, 3], [1, 200], [201, 200], [16, 30], [6, 7], [201, 25], [14, 15], [2, 9], [10, 6], [10, 4], [7, 30], [16, 5], [9, 10], [2, 2], [101, 16], [6, 4], [16, 16], [49, 49], [101, 200], [29, 30], [7, 3], [15, 14], [201, 31], [4, 2], [201, 201], [2, 7], [2, 10], [4, 1], [15, 25], [30, 16], [8, 31], [5, 3], [4, 4], [31, 30], [3, 1], [14, 32], [7, 10], [10, 5], [202, 25], [202, 15], [999999, 1000000], [10000, 12000], [54321, 98765], [123456, 789012], [1, 100000], [100, 1000], [3000, 5000], [99998, 100003], [10000, 20000], [3000, 20000], [100, 12001], [3000, 1000000], [3000, 3000], [1000, 100], [100000, 1], [100003, 100003], [3000, 1000001], [5000, 100003], [100003, 1], [3000, 999999], [101, 1], [123456, 20001], [1000000, 100], [1000, 10], [1000001, 20000], [20001, 100003], [54322, 54321], [3000, 3001], [2999, 3001], [20000, 20000], [19999, 20000], [1000, 1000], [1000000, 1000000], [999999, 3000], [3001, 3001], [999999, 999999], [3001, 1000000], [1, 12000], [789012, 100002], [75, 100003], [75, 12000], [1, 3001], [99, 100000], [999999, 1000], [10000, 98765], [100, 100], [999999, 1000001], [100003, 20000], [100, 99], [1000, 1000001], [100002, 3000], [99, 1], [54321, 100], [100000, 2], [99, 20000], [54321, 101], [99998, 100000], [100001, 1], [100002, 100003], [100001, 20000], [19999, 100001], [75, 75], [1000000, 999999], [5000, 5000], [2, 54322], [99, 99], [1000000, 54322], [19998, 100001], [54321, 54321], [10, 1], [20001, 99997], [101, 99997], [99997, 100], [999998, 999999], [54321, 54322], [54321, 12000], [999998, 12000], [10, 9], [100001, 789012], [123456, 98765], [20000, 99], [999997, 123456], [75, 99997], [100005, 789012], [99999, 99], [101, 100000], [101, 1000], [54322, 789012], [101, 100001], [10, 11], [999999, 12000], [3001, 99999], [5000, 3000], [99997, 99997], [789012, 789012], [1000000, 54321], [54321, 99], [1000000, 1000001], [3000, 75], [99999, 99998], [19997, 19998], [2999, 2999], [100, 98], [99998, 100], [98765, 98765], [123456, 99], [100, 99997], [1000000, 75], [10000, 2999], [11999, 12000], [100001, 100000], [5000, 100004], [3000, 12001], [999998, 999998], [54320, 54321], [12000, 1000000], [3001, 123456], [99999, 20000], [100001, 789013], [20000, 19998], [20001, 12001], [54323, 54321], [98, 12000], [12000, 12000], [999999, 100], [54320, 12000], [10000, 75], [3000, 99997], [100, 19997], [1000000, 2999], [2, 100000], [999997, 3001], [3001, 3000], [100005, 100003], [100001, 100001], [100000, 100000], [20001, 20001], [19999, 1], [2, 123456], [2, 1000], [10, 999998], [99998, 99], [3001, 2999], [12001, 12000], [98, 99], [3000, 2999], [100, 999998], [101, 101], [99999, 100], [100, 54320], [12000, 11998], [54321, 999998], [9999, 9999], [99997, 999999], [98, 100002], [54321, 1000000], [75, 11999], [98, 98], [10001, 10001], [12001, 12001], [789013, 789013], [19998, 1000001], [54320, 3001], [100, 99998], [73, 92], [100001, 100004], [54320, 54320], [100004, 100003], [1, 5000], [100000, 100001], [54322, 99], [20001, 54322], [100004, 99997], [3000, 3002], [789013, 100004], [789013, 1000000], [1000000, 1], [98765, 4999], [3001, 1], [99, 20001], [2999, 3000], [54321, 54323], [99997, 54323], [54320, 3002], [99999, 20001], [20001, 11998], [999999, 92], [19998, 20000], [100002, 19998], [1000, 3000], [10001, 100001], [3000, 789012], [1000000, 999998], [2, 1], [100001, 10], [3002, 3001], [99998, 99998], [10, 1000000], [100002, 10], [3001, 100003], [3001, 20000], [20000, 10000], [1, 2], [1, 19998], [1, 20001], [1000000, 789013], [1000001, 1000001], [100, 101], [2, 99], [20000, 100002], [9999, 3000], [2, 92], [100002, 100002], [4999, 20001], [54322, 54322], [12000, 19998], [1, 10], [9, 75], [789011, 789011], [2999, 54321], [54322, 100], [3001, 999999], [12000, 999999], [123456, 1000000], [3002, 75], [3000, 2998], [1000001, 73], [100001, 5000], [5000, 92], [100003, 5000], [100004, 100004], [20001, 123456], [99999, 100000], [1, 100], [20001, 20000], [20000, 3001], [1000000, 100004], [12001, 11998], [20001, 98765], [99, 100], [19997, 100000], [2999, 54322], [99997, 10001], [75, 20000], [3000, 99999], [101, 100], [100, 19998], [20002, 99997], [2998, 3001], [5001, 99998], [99998, 19999], [10, 99997], [98766, 98765], [100001, 100003], [3000, 12000], [20000, 12000], [100001, 999999], [2, 54323], [1000000, 10], [5001, 102], [1000000, 3000], [54320, 5000], [19998, 99], [2998, 2998], [98765, 75], [999997, 100004], [789011, 99997], [100000, 20001], [789014, 11998], [789014, 789014], [4999, 3000], [101, 54322], [98, 100003], [11999, 11998], [102, 5001], [4998, 4999], [100001, 1000], [10, 100], [12000, 999997], [100002, 3002], [100002, 99999], [75, 9999], [3000, 98], [11999, 11999], [3000, 98765], [1000001, 2998], [999997, 999998], [12001, 999999], [19997, 19996], [2, 999], [19997, 19997], [98, 11998], [99998, 98765], [1000000, 101], [100005, 20001], [74, 101], [4998, 1], [99, 19999], [123456, 75], [10, 789013], [3001, 3002], [102, 102], [100000, 1000001], [100000, 20002], [1, 3000], [98765, 19999], [19996, 20000], [19997, 100004], [54322, 12000], [11999, 1000000], [18, 98765], [5000, 100], [101, 99999], [5001, 100], [19999, 1000000], [999, 4999], [98765, 9999], [5000, 19997], [2999, 99], [54321, 20002], [1000001, 92], [100001, 54321], [1, 1000000], [99997, 100000], [100002, 99998], [100001, 54320], [54323, 3001], [19999, 999997], [92, 1000000], [12001, 75], [789013, 3000], [102, 1000], [123455, 99], [2999, 2998], [100001, 3001], [999, 10], [101, 11998], [100002, 74], [2998, 100002], [999997, 999997], [54322, 3000], [98, 10001], [789013, 789012], [102, 19998], [98765, 99997], [5000, 100001], [4999, 5000], [1, 1000001], [789012, 12001], [5001, 19999], [99997, 99998], [1000001, 1000000], [98, 10], [999998, 999997], [999, 7], [100005, 100], [19999, 19999], [999, 999], [789013, 789014], [123456, 123456], [10, 99998], [103, 100002], [1000000, 9999], [12002, 12001], [17, 98765], [73, 999999], [19997, 75], [75, 999999], [100001, 54323], [10, 20002], [99997, 99999], [789012, 54323], [999998, 1000], [11998, 11998], [100004, 75], [789012, 20001], [99999, 99999], [102, 101], [5002, 5001], [3001, 100002], [11, 10000], [1002, 1001], [99996, 99998], [789013, 98766], [100006, 12001], [54319, 3001], [54320, 999999], [102, 999], [100000, 999], [3000, 54322], [998, 998], [100005, 100006], [98766, 98766], [74, 11998], [999998, 12001], [11, 9], [54320, 99997], [999999, 999998], [123455, 100], [98765, 98766], [101, 10], [10, 98765], [102, 54320], [123455, 3000], [54320, 999], [20002, 998], [5002, 12000], [789012, 98766], [999, 3000], [100000, 99999], [1000000, 73], [10001, 998], [20001, 19998], [5001, 10000], [1, 73], [1003, 1000], [100006, 100003], [7, 2999], [12001, 20001], [3002, 123456], [19996, 19996], [19997, 1000001], [98, 10000], [100003, 54320], [2, 100003], [103, 10], [789012, 98], [2998, 20001], [99, 2999], [98765, 3001], [1001, 10], [998, 997], [93, 5001], [20001, 4999], [54322, 2998], [66, 66], [99998, 99999], [1000, 20000], [3000, 100000], [99998, 99997], [100000, 54321], [1000001, 100002], [54323, 54320], [100, 92], [9999, 5001], [5000, 998], [123455, 12001], [54323, 54323], [11, 100], [999, 1000], [999, 1001], [99998, 54320], [54320, 3000], [123455, 123456], [5000, 2], [1, 99998], [123456, 123455], [10000, 10000], [100, 789012], [98766, 1], [10002, 10000], [98765, 10000], [99998, 9999], [789012, 10000], [123455, 123457], [10000, 20001], [100, 1], [789012, 789011], [10001, 20000], [789011, 100000], [10003, 10003], [1, 98765], [123455, 100003], [123455, 123455], [123456, 789011], [789011, 1000000], [123456, 1000], [20000, 9999], [99999, 54321], [98765, 98764], [99999, 789012], [12000, 789012], [98764, 98765], [123454, 123455], [123456, 54321], [98765, 100003], [123457, 98766], [98764, 10000], [98762, 98763], [1000, 100003], [100, 98766], [10002, 789011], [98763, 123455], [123458, 98767], [98764, 123456], [10002, 20000], [123458, 1], [98763, 98763], [98764, 98764], [3000, 99], [10001, 2], [100000, 789011], [11999, 789011], [1000, 123456], [99999, 98765], [123457, 123457], [789011, 999999], [98766, 5000], [98764, 9999], [99999, 789011], [1000, 98767], [98764, 20000], [4999, 1], [2, 123455], [123456, 99998], [20000, 54320], [10001, 9999], [789011, 12000], [100, 20002], [12001, 789012], [1001, 1001], [20001, 19999], [20001, 100000], [21, 6], [98767, 98767], [99999, 789013], [10002, 10002], [12001, 100003], [5001, 5001], [10001, 10000], [20002, 100000], [99999, 1000], [98765, 10002], [123456, 999999], [4999, 20002], [1001, 100], [1001, 1002], [12000, 789011], [5001, 5000], [101, 54321], [98764, 10002], [98765, 1000], [10002, 54321], [10000, 54321], [123456, 20000], [20001, 98764], [789013, 54320], [19999, 5001], [12000, 68], [98766, 5], [1002, 1003], [99999, 123457], [10003, 123456], [10002, 98766], [98764, 1001], [5001, 99], [98763, 98762], [9999, 10000], [1000, 10002], [123454, 98765], [10000, 100003], [98764, 100], [12000, 1001], [1002, 98763], [10001, 10002], [12001, 68], [789013, 54319], [123458, 99], [4998, 19999], [5, 54321], [98765, 789012], [98763, 99998], [98764, 99998], [99998, 1002], [1001, 123456], [999999, 54321], [789013, 789011], [6, 2], [123455, 54321], [54320, 1000], [10003, 54321], [20000, 3000], [98762, 3000], [54319, 3000], [10000, 123455], [1002, 1002], [999, 9999], [98767, 98763], [5, 98763], [99, 98], [5002, 98764], [10000, 10002], [98764, 10001], [20002, 20002], [10003, 5001], [123454, 98764], [10003, 10002], [98766, 99], [10002, 1000], [10000, 54320], [1002, 1], [98762, 98762], [10002, 5000], [123454, 123454], [98766, 54320], [5000, 99], [54320, 98765], [10003, 5002], [98766, 10000], [19999, 100003], [789010, 789010], [98765, 5000], [20002, 10002], [1, 1002], [101, 20002], [1, 98763], [100, 19999], [789013, 54318], [98763, 99], [98762, 10001], [5002, 99], [54321, 5000], [68, 98762], [100, 789010], [98762, 123455], [100, 98765], [1003, 1003], [54318, 54318], [5001, 100000], [123458, 123458], [789014, 100000], [5003, 5002], [789012, 9999], [68, 98769], [68, 67], [9999, 789012], [5001, 12000], [10001, 54321], [20001, 3000], [123457, 123456], [999, 99999], [10000, 11999], [67, 67], [1, 6], [98762, 9999], [1, 5001], [12000, 54320], [10001, 789011], [2, 5], [54322, 98764], [5001, 99999], [5001, 123456], [1000000, 67], [5002, 100000], [1002, 11999], [12000, 98767], [123455, 123454], [21, 99], [98761, 100003], [1000, 67], [99998, 101], [54322, 2], [1000, 999], [2, 5003], [20001, 10002], [123457, 5], [5, 1003], [21, 7], [100003, 54321], [9999, 98762], [789012, 1], [54321, 1000001], [98769, 98769], [98, 1], [99999, 5], [1000001, 1000002], [5003, 100000], [54318, 10002], [100, 789009], [123455, 5000], [10001, 10004], [20001, 98769], [123456, 101], [10004, 99998], [9999, 98763], [20002, 1], [9999, 54320], [9999, 10003], [12002, 68], [123454, 100003], [10003, 100001], [100, 1001], [54318, 54321], [100, 20000], [20002, 20001], [123454, 11999], [123456, 3000], [100003, 3000], [1003, 1004], [100004, 99998], [1000, 1002], [1, 20002], [1000, 99996], [100003, 100002], [68, 101], [1002, 2], [9998, 10003], [789009, 98767], [9998, 6], [68, 789009], [10001, 11999], [12000, 12001], [1000002, 1000002], [1000001, 789013], [123458, 123456], [54321, 20001], [54322, 99998], [998, 20002], [789011, 54319], [2, 4], [22, 20002], [98762, 123457], [123454, 12000], [98769, 10001], [999999, 4999], [54321, 20000], [123456, 123457], [100004, 20001], [99996, 99999], [20000, 10001], [100001, 10004], [789013, 20000], [54323, 98764], [123455, 123458], [123457, 54321], [10001, 123456], [98765, 12000], [54323, 5], [123458, 123455], [100002, 9999], [99996, 100001], [98, 999999], [789011, 101], [100000, 100004], [10001, 98], [54319, 54319], [54321, 99999], [100003, 10002], [10003, 67], [998, 11999], [102, 9998], [1, 54320], [98766, 98761], [100005, 1004], [54321, 123455], [98763, 10001], [10004, 10004], [98766, 10004], [123457, 101], [789013, 20001], [1003, 54320], [1003, 3001], [4999, 789010], [1, 100003], [98767, 98766], [9998, 999], [789010, 1000], [100003, 2999], [2, 54320], [3000, 20001], [10001, 99999], [10002, 66], [101, 20000], [98765, 1003], [98766, 789013], [4999, 4999], [123457, 100001], [54319, 101], [54323, 98763], [21, 5], [123454, 54321], [54322, 99997], [789011, 1001], [99999, 20002], [5003, 5001], [789015, 123455], [10003, 2], [5002, 5002], [789012, 11999], [99996, 22], [98763, 98764], [54319, 789009], [1002, 1000], [7, 999], [101, 123456], [11999, 1002], [12000, 9998], [100, 4], [20002, 98762], [1004, 98764], [1000002, 10003], [54317, 54316], [100004, 4998], [21, 98765], [9997, 10003], [1000, 98761], [5000, 5001], [67, 1000000], [24, 98764], [99996, 1000000], [54322, 123457], [999999, 789012], [3000, 100003], [9999, 9998], [98763, 5001], [54319, 100001], [789013, 5001], [1, 99996], [54320, 4998], [99999, 102], [5002, 1000], [7, 7], [102, 12000], [98, 1000000], [99998, 10003], [99998, 54319], [100004, 1004], [100001, 12000], [1, 98766], [20002, 5], [123455, 100004], [98770, 10001], [99, 1000], [123457, 20002], [999, 20002], [19999, 20001], [99998, 123457], [98, 98764], [98765, 4998], [123457, 98770], [1000, 54318], [22, 101], [123458, 10003], [54320, 1000000], [100003, 100004], [10003, 54315], [100, 54319], [67, 999999], [67, 999998], [98765, 10004], [99999, 5001], [12002, 12002], [99995, 1003], [54320, 20001], [10004, 5001], [98, 123457], [7, 6], [54317, 2], [123456, 9997], [9998, 789010], [99999, 1000001], [99998, 20001], [789009, 123458], [97, 97], [1000002, 98766], [4997, 19999], [11998, 12000], [1000, 123457], [19999, 789012]]
    results = ['0b11', '0b1010', '0b1111001010', '0b1111100100', '0b1011000010', '0b101101110', '0b110101101', '0b1001110010', '0b11010111', -1, -1, '0b101', '0b1', '0b110', '0b11110', '0b10100', '0b10010110', '0b1111', '0b1010', '0b1001011', '0b111010', -1, '0b1001100', -1, '0b1110011', '0b110100', '0b100011', -1, '0b110010', '0b110', '0b11110', -1, '0b100', '0b1001', '0b110', '0b1110100', '0b11001', '0b10000', -1, -1, '0b1010', -1, '0b1100100', -1, '0b10111', '0b110', -1, '0b1110', '0b110', -1, -1, '0b10010', -1, '0b1010', '0b10', -1, -1, '0b10000', '0b110001', '0b10010110', '0b11110', -1, -1, -1, -1, '0b11001001', '0b100', '0b110', -1, '0b10100', -1, '0b10100', -1, '0b100', -1, -1, '0b10111', '0b1000', -1, -1, -1, '0b11110100001001000000', '0b10101011111000', '0b10010101011111111', '0b1101111011000101010', '0b1100001101010000', '0b1000100110', '0b111110100000', '0b11000011010100000', '0b11101010011000', '0b10110011101100', '0b1011110100010', '0b1111010011011111100', '0b101110111000', -1, -1, '0b11000011010100011', '0b1111010011011111100', '0b1100110100010110', -1, '0b1111010011011111100', -1, -1, -1, -1, -1, '0b1110101001100010', -1, '0b101110111000', '0b101110111000', '0b100111000100000', '0b100111000100000', '0b1111101000', '0b11110100001001000000', -1, '0b101110111001', '0b11110100001000111111', '0b1111010011011111100', '0b1011101110000', -1, '0b1100001101110111', '0b1011110010110', '0b10111011101', '0b1100001110000010', -1, '0b1101010001101110', '0b1100100', '0b11110100001001000000', -1, -1, '0b1111010001100010100', -1, -1, -1, -1, '0b10011101000010', -1, '0b11000011010011111', -1, '0b11000011010100010', -1, '0b1110101001100000', '0b1001011', -1, '0b1001110001000', '0b110101000011010', '0b1100011', -1, '0b1110101001100000', '0b1101010000110001', -1, '0b1110101001011111', '0b1100001110000001', -1, '0b11110100001000111110', '0b1101010000110010', -1, -1, -1, '0b1101100100001011010', -1, -1, -1, '0b1100001101110100', '0b1101100100001011100', -1, '0b1100001110000010', '0b1000100110', '0b1100110111100100011', '0b1100001110000011', '0b1010', -1, '0b1100100100101100', -1, '0b11000011010011101', '0b11000000101000010100', -1, -1, '0b11110100001001000000', -1, -1, '0b100111000011110', '0b101110110111', -1, -1, '0b11000000111001101', -1, '0b1100001110000000', -1, -1, '0b10111011100000', -1, '0b1100110100010110', '0b1110101001100', '0b11110100001000111110', '0b1101010000110000', '0b1111011100010010000', '0b1111011011111100', -1, '0b1101100100001011011', -1, -1, -1, '0b1011110100001', '0b10111011100000', -1, -1, -1, '0b1100100100101010', '0b10011101000000', -1, '0b1100001101010001', -1, -1, -1, '0b11000011010100001', '0b11000011010100000', '0b100111000100001', -1, '0b1111000100100001', '0b111110101', '0b1111010000100100100', -1, -1, -1, '0b1100010', -1, '0b1111010000101010001', '0b1100101', -1, '0b110101001001010', -1, '0b10000000101100111000', '0b10011100001111', '0b10000110010001101110', '0b1100001110000010', '0b10000000101100111000', '0b1011110010101', '0b1100010', '0b10011100010001', '0b10111011100001', '0b11000000101000010101', '0b1111100100000110000', -1, '0b1100001110000001', '0b1010010', '0b11000011010100010', '0b1101010000110000', -1, '0b100111000100', '0b11000011010100000', -1, '0b1001000100101010', -1, '0b101110111001', -1, '0b11011010011000101010', -1, -1, -1, '0b10011101000010', '0b101110111000', '0b1101010000110010', -1, -1, -1, -1, -1, '0b100111000011111', -1, '0b11111010000', '0b1101011011011001', '0b1100000101011100110', -1, -1, -1, -1, '0b11000011010011110', '0b1111010000100100101', -1, '0b1100100100101110', '0b10110011101100', -1, '0b10', '0b10011100010000', '0b10011100010001', -1, '0b11110100001001000001', '0b1100100', '0b110010', '0b1110101001100001', -1, '0b101111', '0b11000011010100010', '0b11000011010100', '0b1101010000110010', '0b11111001111111', '0b110', '0b101010', '0b11000000101000010011', '0b110111111110100', -1, '0b1111010011011111100', '0b1111011100010010000', '0b10001001001001000000', -1, -1, -1, -1, -1, -1, '0b11000011010100100', '0b10001100000110000', '0b11000011010100000', '0b110010', -1, -1, -1, -1, '0b1110011111110111', '0b1100100', '0b1110101001011110', '0b110111111110100', -1, '0b10011100110110', '0b1100100100101100', -1, '0b10011101000001', '0b1110101001100000', '0b101110111000', '0b1100110100010100', -1, '0b1100001101010100', -1, '0b11000011010100010', '0b1110101001100', -1, '0b10000110010001110000', '0b110101000011010', -1, -1, -1, -1, -1, '0b101110110110', -1, -1, -1, -1, -1, '0b11000000101000010110', -1, '0b110101001001100', '0b1100001110000010', -1, '0b100111111000', '0b1001110000110', -1, '0b110111', '0b1111011100010001110', -1, -1, '0b1001110101101', -1, '0b10111011011111', '0b1100011011000010', -1, '0b11110100001000111110', '0b1111011100010010000', -1, '0b111110100', '0b100111000011101', '0b1011110100000', -1, -1, -1, '0b1011000', -1, '0b10011101000001', -1, '0b1100000010100010000', '0b101110111010', '0b1100110', '0b10000110010001110000', -1, '0b10111011100', -1, '0b100111000011110', '0b1110101001100000', -1, '0b1111011100010010000', '0b1100000011110000', -1, '0b1100001110000010', -1, '0b1111100100000110000', '0b101110110111', -1, '0b11000011010010', -1, -1, -1, -1, '0b1111010000100100000', '0b11000011010011110', -1, -1, -1, '0b1111100100000101110', '0b1111010000101001110', -1, -1, '0b1000100111', -1, -1, -1, -1, '0b1011110100010', -1, '0b1100100100101100', '0b11110100001000111101', -1, '0b1001110111010', -1, '0b10011101000010', '0b11000010000110101', '0b1100110100010100', '0b1001110001000', '0b1111010000100100001', -1, '0b11000011010100', '0b11000011010011110', -1, -1, -1, -1, -1, '0b100111000011111', '0b1111100111', '0b11000000101000010110', '0b11110001001000000', '0b1100001101010100', '0b1100001110000100', -1, -1, '0b1100000011101111', '0b1111010000101000100', -1, '0b1111010000101000101', -1, '0b10011100010110', '0b11000011010011110', -1, -1, '0b10111011011110', -1, -1, '0b11000011010011111', -1, -1, '0b1100100100101110', '0b1001110001110', -1, '0b11000011010011101', -1, -1, -1, '0b10000000101100111000', '0b1000100110', -1, '0b110111111110101', '0b1111100110', '0b11000011010100110', '0b11000000111001110', '0b1011110010100', -1, -1, '0b10010110101100110', -1, -1, '0b11000000111001110', -1, '0b1100000011101100', '0b110101001001011', -1, -1, -1, '0b10000100110101', -1, '0b11111010000', -1, -1, -1, -1, '0b1110101001100', '0b100101', -1, -1, '0b10111011111', '0b11111010000001', '0b1111011011111101', '0b100111000011100', '0b1111100100000101111', '0b1001110111001', -1, '0b1100001101010010', -1, -1, '0b10110011101100', '0b11000001101', -1, -1, -1, '0b100111110011', -1, -1, '0b1000010', '0b11000011010011110', '0b10100100000100', '0b1100100100101100', -1, -1, -1, -1, -1, -1, -1, -1, '0b1101010000110011', '0b111000', '0b1111101000', '0b1111101000', -1, -1, '0b11110001001000000', -1, '0b1100001101010000', -1, '0b10011100010000', '0b1100000010100111100', -1, -1, -1, -1, -1, '0b11110001001000000', '0b11101010011000', -1, -1, '0b11101010011000', -1, '0b10011100010011', '0b1100000011100111', -1, '0b11110001000111111', '0b1101111011000101010', '0b11011010011000101010', -1, -1, -1, -1, '0b1101100100001011010', '0b1100001110001111010', '0b11000000111001100', '0b11110001000111110', -1, '0b11000010000111000', -1, -1, '0b11000000111001010', '0b1100010101000110', '0b1100000100011001', '0b1100001100010010010', '0b11011001000000101', -1, '0b11011001000000110', '0b11101010011001', -1, '0b11000000111001011', '0b11000000111001100', -1, -1, '0b1101100100001011010', '0b1100001110001111001', '0b1111001100010100', -1, '0b11110001001000001', '0b11011010011000101001', -1, -1, '0b1101100100001011001', '0b1100001011011100', -1, -1, '0b1111000100100000', -1, '0b1001000100101000', -1, -1, '0b10011101000011', '0b1100001110001111010', '0b1111101001', -1, '0b1110101001100000', -1, '0b11000000111001111', '0b1101100100001011010', '0b10011100010010', '0b1101101011000010', '0b1001110001001', -1, '0b1110101001100001', -1, -1, '0b10001001001001000000', '0b11000011010100', -1, '0b1111101010', '0b1100001110001111010', -1, '0b110101001001011', -1, -1, '0b111110110100010', '0b111110110100000', -1, '0b1110011111110110', -1, -1, -1, -1, '0b1111101010', '0b11011010001110000', '0b10000010010101010', '0b1101010001110000', -1, -1, -1, '0b10011100010000', '0b1010101111101', -1, '0b1101011011011010', -1, -1, '0b1100001011011010', '0b10011100010010', -1, -1, -1, '0b11000011010010', '0b110101000011011', '0b1101100010111110000', '0b11000010000110100', '0b11000010000110101', -1, '0b1111001100010100', -1, -1, -1, -1, -1, '0b111110110100010', -1, -1, -1, '0b10000010010101000', '0b1111101010', '0b1010101111011', -1, '0b1100000011101000', -1, '0b1100101010101011', '0b10011100010001', -1, '0b100111000100010', -1, -1, -1, -1, -1, '0b111110110100000', -1, '0b11000000111001010', -1, '0b11110001000111110', -1, -1, '0b10010101011111110', -1, -1, '0b1110101001100001', '0b11000000101000010010', -1, -1, '0b111110110', '0b10011101000100', '0b1100000011100110', '0b10011101000010', -1, -1, -1, -1, -1, '0b1100000100000111', '0b1100000010100111011', '0b11011001000000100', '0b1100000100011000', '0b1111101011', '0b1101010000101110', '0b1100110100010100', '0b11110001001000010', -1, -1, -1, '0b1100000100001010', -1, '0b1100001100010010010', '0b10000100110100', '0b111110110100001', -1, -1, '0b1100010101000011', '0b10101011111000', '0b1000011', '0b100', -1, '0b100111000101', '0b1000000110001000', '0b1100001100010010010', '0b100', '0b10010101011111111', '0b1100110100010100', '0b1111101011100100', -1, '0b1100110100010101', '0b1100101100100', '0b1101100001011000', -1, '0b111100', '0b11000010000110110', -1, -1, -1, -1, '0b100111000110', -1, -1, '0b111111000', -1, -1, '0b1101010001101100', -1, '0b10000000101100111001', '0b11000000111010001', -1, -1, '0b11110100001001000010', '0b1100110100010110', -1, '0b1100000010100111010', -1, '0b10011100010010', '0b1110011111111001', -1, '0b1101011011011001', '0b1101010001101101', -1, '0b111110110100000', '0b10011100010001', -1, -1, '0b1101011011011010', '0b1000100110', '0b1101010000110000', '0b10011101000010', -1, -1, -1, -1, '0b1111101100', -1, '0b1111101001', '0b10011100010010', '0b1100010101000010', -1, '0b1010100', -1, '0b10011100010000', -1, -1, '0b1100000010100101010', '0b10101011111000', '0b10111011100000', '0b11110100001001000010', -1, -1, -1, '0b10010110101101000', '0b10100100000100', -1, '0b11', '0b10011100011100', '0b11011001000000110', -1, -1, -1, -1, '0b11110001001000000', -1, '0b11000011010011110', -1, -1, -1, '0b10010101100000000', '0b11110001001000000', -1, '0b10000010010101000', -1, -1, -1, -1, '0b11000011010011110', '0b1111010000101010000', -1, '0b11000011010100010', -1, '0b1101010000101111', '0b10010110101101000', -1, -1, '0b1100101100010', '0b1001110111010', '0b110101000011000', -1, -1, '0b10101101100111000', -1, '0b10011100010100', -1, -1, -1, '0b110110000001110', '0b11111010010', '0b1100000111011001100', '0b1100001101010010', -1, -1, -1, -1, '0b110101000011001', '0b10110011101100', '0b1101011011011000', -1, '0b10011101000010', -1, '0b1101100010111110010', '0b1001110000111', -1, -1, '0b10010101011111111', -1, -1, '0b10010110101101000', -1, -1, -1, -1, -1, '0b1001110001010', -1, -1, '0b11000000111001100', '0b1100110111100100000', -1, '0b111110111', '0b1111000101010010', -1, -1, -1, '0b1110011111110110', '0b1100001011011100', -1, -1, -1, '0b1100000011110001', '0b10011100010000', '0b1100001011011000', '0b1001110001000', '0b1111010000101000010', '0b1100000011110010', '0b10000110010001101110', '0b10101101100111010', -1, '0b1100100100101110', -1, -1, '0b10010110101101000', -1, '0b1100001101001110', -1, -1, -1, '0b111', '0b1011110100011', '0b1111010000101010001', -1, -1, -1, -1, '0b1100000011101000', -1, -1, -1, '0b1000100110', -1, '0b10100100000100', '0b100111000100000', '0b11011010001110000', '0b1100000100010111', -1, -1, '0b110110000001011', '0b111110', -1, '0b10000000101100111000', '0b11000011010100100', '0b111110110011111', '0b110101001001010', '0b1111010000101000001', '0b1111010000101000000', -1, -1, '0b10111011100010', -1, -1, -1, '0b1111000101010010', -1, -1, -1, '0b1100001100010010000', '0b10000110010001110000', -1, -1, '0b1100001', -1, '0b11000011010010', '0b10111011011111', '0b1111001100010100', '0b1100010110000011010']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(rounded_avg)