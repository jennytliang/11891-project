def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    
	Include these tokens in the code: "
	Do not include these tokens in the code: f '
	"""

    r = ""
    a = 0
    b = 1
    while (decimal > 0):
        a = decimal % 2
        r = r + str(a)
        decimal = decimal // 2
    r = "db" + r + "db"
    return r


if __name__ == '__main__':
    print("Example:")
    print(decimal_to_binary(15))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decimal_to_binary(15) == "db1111db", "First"
    assert decimal_to_binary(32) == "db100000db", "Second"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")




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
    inputs = [[0], [32], [103], [15], [100001], [255], [999999999], [1000000000000], [7], [1023], [1], [2], [3], [4], [1000000000], [6], [1000000001], [1000000000002], [5], [100002], [100000], [1022], [8], [1000000002], [1024], [100003], [1000000000001], [999999998], [999999999999], [256], [257], [1021], [259], [1000000000003], [1000000004], [1000000000004], [1000000000005], [1000000005], [9], [1000000000006], [260], [1000000000007], [100004], [999999999998], [999999999997], [258], [1000000000008], [1000000006], [45], [100005], [99999], [1025], [999999997], [999999996], [1000000003], [44], [43], [1000000007], [42], [999999995], [46], [47], [254], [10], [999999994], [28], [1000000000009], [100007], [41], [1020], [27], [1026], [23], [999999999996], [253], [100006], [38], [100008], [39], [100009], [1027], [261], [26], [1019], [1000000008], [11], [251], [1018], [48], [22], [99998], [21], [40], [37], [20], [100011], [262], [25], [1028], [24], [999999993], [274877906943], [9223372036854775807], [10000000000000000000000000000001], [8892743], [1000], [274877906942], [10000000000000000000000000000002], [8892742], [8892740], [8892744], [10000000000000000000000000000003], [8892745], [8892741], [999], [8892739], [274877906941], [274877906940], [998], [9223372036854775806], [10000000000000000000000000000000], [274877906939], [1001], [1002], [9223372036854775808], [274877906938], [8892737], [8892746], [8892747], [274877906944], [1003], [9223372036854775805], [252], [8892748], [997], [274877906937], [8892736], [274877906945], [9223372036854775809], [274877906936], [274877906946], [8892735], [8892738], [1004], [10000000000000000000000000000004], [996], [10000000000000000000000000000005], [8892750], [8892749], [1006], [8892751], [99], [98], [9999999999999999999999999999999], [92], [1005], [9999999999999999999999999999998], [8892752], [1007], [9223372036854775804], [995], [16], [263], [53], [30], [274877906947], [29], [9223372036854775810], [67], [66], [9223372036854775811], [9999999999999999999999999999997], [63], [9999999999999999999999999999996], [81], [82], [80], [68], [9223372036854775812], [31], [83], [79], [62], [61], [84], [65], [60], [9223372036854775813], [250], [249], [9999999999999999999999999999995], [85], [89], [9223372036854775814], [49], [78], [50], [88], [33], [90]]
    results = ['db0db', 'db100000db', 'db1100111db', 'db1111db', 'db11000011010100001db', 'db11111111db', 'db111011100110101100100111111111db', 'db1110100011010100101001010001000000000000db', 'db111db', 'db1111111111db', 'db1db', 'db10db', 'db11db', 'db100db', 'db111011100110101100101000000000db', 'db110db', 'db111011100110101100101000000001db', 'db1110100011010100101001010001000000000010db', 'db101db', 'db11000011010100010db', 'db11000011010100000db', 'db1111111110db', 'db1000db', 'db111011100110101100101000000010db', 'db10000000000db', 'db11000011010100011db', 'db1110100011010100101001010001000000000001db', 'db111011100110101100100111111110db', 'db1110100011010100101001010000111111111111db', 'db100000000db', 'db100000001db', 'db1111111101db', 'db100000011db', 'db1110100011010100101001010001000000000011db', 'db111011100110101100101000000100db', 'db1110100011010100101001010001000000000100db', 'db1110100011010100101001010001000000000101db', 'db111011100110101100101000000101db', 'db1001db', 'db1110100011010100101001010001000000000110db', 'db100000100db', 'db1110100011010100101001010001000000000111db', 'db11000011010100100db', 'db1110100011010100101001010000111111111110db', 'db1110100011010100101001010000111111111101db', 'db100000010db', 'db1110100011010100101001010001000000001000db', 'db111011100110101100101000000110db', 'db101101db', 'db11000011010100101db', 'db11000011010011111db', 'db10000000001db', 'db111011100110101100100111111101db', 'db111011100110101100100111111100db', 'db111011100110101100101000000011db', 'db101100db', 'db101011db', 'db111011100110101100101000000111db', 'db101010db', 'db111011100110101100100111111011db', 'db101110db', 'db101111db', 'db11111110db', 'db1010db', 'db111011100110101100100111111010db', 'db11100db', 'db1110100011010100101001010001000000001001db', 'db11000011010100111db', 'db101001db', 'db1111111100db', 'db11011db', 'db10000000010db', 'db10111db', 'db1110100011010100101001010000111111111100db', 'db11111101db', 'db11000011010100110db', 'db100110db', 'db11000011010101000db', 'db100111db', 'db11000011010101001db', 'db10000000011db', 'db100000101db', 'db11010db', 'db1111111011db', 'db111011100110101100101000001000db', 'db1011db', 'db11111011db', 'db1111111010db', 'db110000db', 'db10110db', 'db11000011010011110db', 'db10101db', 'db101000db', 'db100101db', 'db10100db', 'db11000011010101011db', 'db100000110db', 'db11001db', 'db10000000100db', 'db11000db', 'db111011100110101100100111111001db', 'db11111111111111111111111111111111111111db', 'db111111111111111111111111111111111111111111111111111111111111111db', 'db1111110001101111011111000100000001000101100000010010001010010110010011010000000000000000000000000000001db', 'db100001111011000101000111db', 'db1111101000db', 'db11111111111111111111111111111111111110db', 'db1111110001101111011111000100000001000101100000010010001010010110010011010000000000000000000000000000010db', 'db100001111011000101000110db', 'db100001111011000101000100db', 'db100001111011000101001000db', 'db1111110001101111011111000100000001000101100000010010001010010110010011010000000000000000000000000000011db', 'db100001111011000101001001db', 'db100001111011000101000101db', 'db1111100111db', 'db100001111011000101000011db', 'db11111111111111111111111111111111111101db', 'db11111111111111111111111111111111111100db', 'db1111100110db', 'db111111111111111111111111111111111111111111111111111111111111110db', 'db1111110001101111011111000100000001000101100000010010001010010110010011010000000000000000000000000000000db', 'db11111111111111111111111111111111111011db', 'db1111101001db', 'db1111101010db', 'db1000000000000000000000000000000000000000000000000000000000000000db', 'db11111111111111111111111111111111111010db', 'db100001111011000101000001db', 'db100001111011000101001010db', 'db100001111011000101001011db', 'db100000000000000000000000000000000000000db', 'db1111101011db', 'db111111111111111111111111111111111111111111111111111111111111101db', 'db11111100db', 'db100001111011000101001100db', 'db1111100101db', 'db11111111111111111111111111111111111001db', 'db100001111011000101000000db', 'db100000000000000000000000000000000000001db', 'db1000000000000000000000000000000000000000000000000000000000000001db', 'db11111111111111111111111111111111111000db', 'db100000000000000000000000000000000000010db', 'db100001111011000100111111db', 'db100001111011000101000010db', 'db1111101100db', 'db1111110001101111011111000100000001000101100000010010001010010110010011010000000000000000000000000000100db', 'db1111100100db', 'db1111110001101111011111000100000001000101100000010010001010010110010011010000000000000000000000000000101db', 'db100001111011000101001110db', 'db100001111011000101001101db', 'db1111101110db', 'db100001111011000101001111db', 'db1100011db', 'db1100010db', 'db1111110001101111011111000100000001000101100000010010001010010110010011001111111111111111111111111111111db', 'db1011100db', 'db1111101101db', 'db1111110001101111011111000100000001000101100000010010001010010110010011001111111111111111111111111111110db', 'db100001111011000101010000db', 'db1111101111db', 'db111111111111111111111111111111111111111111111111111111111111100db', 'db1111100011db', 'db10000db', 'db100000111db', 'db110101db', 'db11110db', 'db100000000000000000000000000000000000011db', 'db11101db', 'db1000000000000000000000000000000000000000000000000000000000000010db', 'db1000011db', 'db1000010db', 'db1000000000000000000000000000000000000000000000000000000000000011db', 'db1111110001101111011111000100000001000101100000010010001010010110010011001111111111111111111111111111101db', 'db111111db', 'db1111110001101111011111000100000001000101100000010010001010010110010011001111111111111111111111111111100db', 'db1010001db', 'db1010010db', 'db1010000db', 'db1000100db', 'db1000000000000000000000000000000000000000000000000000000000000100db', 'db11111db', 'db1010011db', 'db1001111db', 'db111110db', 'db111101db', 'db1010100db', 'db1000001db', 'db111100db', 'db1000000000000000000000000000000000000000000000000000000000000101db', 'db11111010db', 'db11111001db', 'db1111110001101111011111000100000001000101100000010010001010010110010011001111111111111111111111111111011db', 'db1010101db', 'db1011001db', 'db1000000000000000000000000000000000000000000000000000000000000110db', 'db110001db', 'db1001110db', 'db110010db', 'db1011000db', 'db100001db', 'db1011010db']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(decimal_to_binary)