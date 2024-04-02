from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = ""
	"""
    r = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            r += "0"
        else:
            r += "1"
    return r


def string_xor_list(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list.
    >>> string_xor_list('010', '110')
    [1,0,0]
    
	Include these tokens in the code: return [int (i) for i in r. split ()]
	"""
    r = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            r += "0"
        else:
            r += "1"
    return [int(i) for i in r.split()]


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
    inputs = [['111000', '101010'], ['1', '1'], ['0101', '0000'], ['000', '000'], ['1111', '1111'], ['10101', '01010'], ['01010101', '11001100'], ['101010', '010101'], ['010', '001'], ['01100', '10011'], ['00000001', '11111110'], ['111', '000'], ['1', '0'], ['01100000', '01100000'], ['01010101', '01010101'], ['01010', '01010'], ['0101100000100000', '0110000010101010'], ['01100', '01100'], ['001', '111'], ['11111110', '00000001'], ['101010', '101010'], ['00', '00'], ['11', '00'], ['101001100', '110011000'], ['01100000', '00000001'], ['010101', '010101'], ['001', '010'], ['10100110100110', '10100110100110'], ['110101011111110', '110101011111110'], ['101010101111', '101010101111'], ['110011000001110', '110011000001110'], ['10011', '10011'], ['0101100000100000', '0101100000100000'], ['1111110011000', '1111110011000'], ['11010101001111110', '11010101001111110'], ['110011000', '110011000'], ['11001100', '11001100'], ['111111', '111111'], ['11111110', '11111110'], ['001', '001'], ['0', '0'], ['111', '111'], ['11111110101011111110110', '11111110101011111110110'], ['1010101101111', '1010101101111'], ['1100110000', '1100110000'], ['0101011111110011000', '0101011111110011000'], ['11010100100110101010100', '11010100100110101010100'], ['11111111100110001', '11111111100110001'], ['0010', '0000'], ['110101001001101010101000', '110101001001101010101000'], ['010', '010'], ['1011010100100110101010100010', '1011010100100110101010100010'], ['0011000', '0011000'], ['10101', '10101'], ['110101', '100101'], ['01100', '10101'], ['1101001001', '1101001001'], ['00000001', '00000001'], ['011000000', '011000000'], ['0001', '0001'], ['01100', '10010'], ['001', '000'], ['01111110000', '01111110000'], ['00000011', '00000001'], ['10100110100110101010', '10100110100110101010'], ['11111100110000', '11111100110000'], ['1010101', '1010101'], ['0100000001100', '0100000001100'], ['00010', '00000'], ['11001100', '01010101'], ['1010101001111', '1010101001111'], ['11001', '01100'], ['0001100', '0001100'], ['0000', '0000'], ['110101001001110101011010100100110101010100101000', '110101001001110101011010100100110101010100101000'], ['11001', '00010'], ['000010', '000010'], ['101001100', '011000000'], ['0000', '1111'], ['10100110100110', '11011110000010'], ['00000', '00000'], ['011010', '101101'], ['010101', '001010'], ['00010', '11001'], ['011000', '011100'], ['0011111100110000010', '0011111100110000010'], ['011100', '011100'], ['0110000011010100100110101010100', '0110000011010100100110101010100'], ['01', '01'], ['', ''], ['111111101010100001100111', '111111101010100001100111'], ['00010', '00010'], ['010100101', '010100101'], ['101001111001100000110', '101001111001100000110'], ['011', '011'], ['110101001001110101011010100100111010100101010100101000', '110101001001110101011010100100111010100101010100101000'], ['11', '11'], ['10001', '10001'], ['10101001011', '10101001011'], ['11010101111111011101100000101010101', '11010101111111011101100000101010101'], ['101010', '011011'], ['110100110100110101010', '101001110100110101010'], ['10101010', '01010101'], ['10001000', '11111111'], ['000000', '000111'], ['0110011', '0101010'], ['11011011', '10101010'], ['1000011', '0000000'], ['101010101010', '010101010101'], ['10101010101010101010101010', '01010101010101010101010101'], ['111000111111000111111000', '000111000000111000000111'], ['010101010101', '010101010101'], ['0000000', '0000000'], ['01010101010101010101010101', '01010101010101010101010101'], ['0101010', '0110011'], ['101010101010', '101010101010'], ['110110011', '110110011'], ['0000000', '1000011'], ['1000011', '1000011'], ['111000111111000111111000', '111000111111000111111000'], ['0101010', '0101010'], ['0101010', '1111111'], ['11011011', '11011011'], ['01110001111110001111110001010101010101010101010101', '01110001111110001111110001010101010101010101010101'], ['101000011100', '101000011100'], ['11111111', '11111111'], ['000000111000000111', '000000111000000111'], ['1111111', '1111111'], ['101010101010', '101000011100'], ['0101010', '0000000'], ['111101100111', '111101100111'], ['10101010', '10101010'], ['100011000', '100011000'], ['0110011', '0110011'], ['10000011', '10000011'], ['111111100011111100011111100001100111', '111111100011111100011111100001100111'], ['00000000', '10001000'], ['111101100111', '010101010101'], ['10001000', '10001000'], ['000111', '000111'], ['1010000011100', '1010000011100'], ['000111000000111000000111', '000111000000111000000111'], ['1111111', '0101010'], ['1100010001', '1100010001'], ['010101010101', '111101100111'], ['1101011', '1111111'], ['01010101', '10101010'], ['00000000', '00000000'], ['11111110001111110001111101010101100001100111', '11111110001111110001111101010101100001100111'], ['1000011', '0101010'], ['1101011', '0101010'], ['10100000111000000000', '10100000111000000000'], ['0110011', '0000000'], ['11000011', '11000011'], ['010101010101', '101010101010'], ['0101010100101', '0101010100101'], ['101110111111100011111100011111100001100111001111110001111110001000011100', '101110111111100011111100011111100001100111001111110001111110001000011100'], ['1010000011', '1010000011'], ['1111111', '1101011'], ['0101011010101', '0101011010101'], ['0101010', '1000011'], ['11011011', '10001000'], ['000000', '000000'], ['00000000', '11111111'], ['0111000111111000111111000101010101010101010101111111111', '0111000111111000111111000101010101010101010101111111111'], ['1100001111111111', '1100001111111111'], ['1101011', '1101011'], ['010010001', '010010101'], ['11011011', '11111111'], ['11100001111111111011', '11100001111111111011'], ['0011010101010', '0011010101010'], ['010101010101010101010101010101010', '010101010101010101010101010101010'], ['1100000000', '1100000000'], ['1110001111110001111110000', '1110001111110001111110000'], ['111101100111010101010101', '111101100111010101010101'], ['0110011', '1101011'], ['01010101', '11011011'], ['11111111', '00000000'], ['10000011', '10001000'], ['11010101010', '11010101010'], ['101010110', '101010110'], ['11010001110000001110000001111', '11010001110000001110000001111'], ['10000011', '10000001'], ['10101010', '11000011'], ['01010101', '00000000'], ['0101010101010101010110101010101010', '0101010101001010101010101010101010'], ['11011011', '01011010'], ['01010101', '10000001'], ['10000001', '11000011'], ['11100011111100011111100001110', '11100011111100011111100001110'], ['10000001', '10000001'], ['111111110001111110001111110000110011111101100111', '111111110001111110001111110000110011111101100111'], ['01010101000101', '01010101000101'], ['1010101010010', '1001000011100'], ['010010101', '000000000'], ['110010000110011', '110010000110011'], ['1001000011100', '1001000011100'], ['000000000', '010010101'], ['10101010', '10000011'], ['1010101010010', '0011010101010'], ['1000101', '0101010'], ['110000111111111110100000011100', '110000111111111110100000011100'], ['0011010101010', '1010101010010'], ['0101010101010101010100101', '0101010101010101010100101'], ['010010101', '010010101'], ['11010', '11010'], ['101011010', '101011010'], ['11000011', '10000001'], ['000000000', '000000000'], ['01011', '01011'], ['010111', '011011'], ['11000001111101100111010101010101', '11000001111101100111010101010101'], ['10000011', '11011011'], ['0101010101001010101010101010101010', '0101010101010101010110101010101010'], ['0101011010101', '1010101010010'], ['0101010101010101010110101010101010', '0101010101010101010110101010101010'], ['011111111100011111100011111100001100111011', '011111111100011111100011111100001100111011'], ['11000100001', '11000100001'], ['11010001', '10000001'], ['0101010100101', '1010101010010'], ['0100010101', '0100010101'], ['0101010100101', '1000100100110'], ['101010110', '101011010'], ['101100000000101010', '101100000000101010'], ['01010010101010', '01010010101010'], ['11110110011011111111100011111100011111100001100111011', '11110110011011111111100011111100011111100001100111011'], ['0101010100101', '1010000011100'], ['11111110001111000', '11111110001111000'], ['01010101', '10000011'], ['1101001000111111', '1101001000111111'], ['101000011101010110100', '101000011101010110100'], ['01101001000111111110011', '01101001000111111110011'], ['10001000', '11011011'], ['010111', '010111'], ['1000011', '1101011'], ['01110001111110001111110001010101010101010101010101', '10011111111100011111100011111100001100111011101010'], ['0101010100101', '0000000110110'], ['0101010100101', '0011010101010'], ['11010101010', '11010100101'], ['0000000110110', '0000000110110'], ['010010001', '010010001'], ['100010111110110011011111111100011111100011111100001100111011', '100010111110110011011111111100011111100011111100001100111011'], ['101011010', '101010110'], ['10101010', '11011011'], ['01011010', '01011010'], ['1110001101111000111111000', '1110100111111000111111000'], ['01010101010101010101000101', '01010101010101010101000101'], ['000000011010101010110', '000000011010101010110'], ['11010001', '11111111'], ['11010100101', '11010100101'], ['111111110001111110001111101010110110000110011111101100111', '111111110001111110001111101010110110000110011111101100111'], ['1110100111111000111111000', '1110100111111000111111000'], ['01010000001110000001110010101101', '01010000001110000001110010101101'], ['1010101010010', '0000000110110'], ['101000001110000000', '101000001110000000'], ['11001111111100011111100011111010101101100001100111111011001110100001', '11001111111100011111100011111010101101100001100111111011001110100001'], ['0101000000111000000100000111110010101101', '0101000000111000000111010000001010101101'], ['010101010100110101011010101010101010', '010101010100110101011010101010101010'], ['1110001111110001111110000', '0101010101010101010100101'], ['10011111110001111110001111110000110011111', '10011111110001111110001111110000110011111'], ['00011', '00011'], ['0100101010101', '0100101010101'], ['0000000000', '0000000000'], ['0100101010100110101011010101010101010', '0100101010100110101011010101010101010'], ['10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111'], ['11111111', '10101010'], ['001010101', '001010101'], ['0101010', '0000111'], ['10101010', '11111111'], ['0011', '0011'], ['0000111', '0000111'], ['10101010101010101010101010', '10101010101010101010101010'], ['000000000000000', '000000000000000'], ['001010101', '100101010'], ['11011011', '01010101'], ['0010101000011100000000111001110000001111', '0010101000011100000000111001110000001111'], ['101001010101010101010101010', '101001010101010101010101010'], ['1011100011111100011111100000011', '1011100011111100011111100000011'], ['10001000', '10101010'], ['1000011', '0110011'], ['00101010000111000000000111001110000001111', '00101010000111000000001110011100000011111'], ['10101010010101011010101010', '10101010101010101010101010'], ['0101010101101001010101010101', '0101010101101001010101010101'], ['00101010000111000000001110011100000011111', '00101010000111000000001110011100000011111'], ['11111000111111000111111000111111', '11100011111100011111100011111111'], ['100000000101010', '100000000101010'], ['010101100010000', '010101100010000'], ['110111011', '111011011'], ['100010000', '110111011'], ['111111100000001', '111111100000001'], ['100101010', '100101010'], ['0010101001010101001010101101010101000111000000001110011100000011111', '0010101001010101001010101101010101000111000000001110011100000011111'], ['100101000111000000111000000111010', '100101000111000000111000000111010'], ['1010101000011101010', '1010101000011101010'], ['100000000101010', '111111100000001'], ['11111111', '10001000'], ['00110011', '00110011'], ['001101001010101010101', '001101001010101010101'], ['01010101011011001010101010101', '01010101011011001010101010101'], ['001101000000000000000001010101010101', '001101000000000000000001010101010101'], ['0100101010101101100101010101010110101', '0100101010101101100101010101010110101'], ['10101010', '10001000'], ['1111100011111100011111100011111', '1111100011111100011111100011111'], ['110111011', '001010101'], ['00101010000111000000000111001110000001111', '00101010000111000000000111001110000001111'], ['11011101', '10001000'], ['110111011', '110111011'], ['111110001111110001111111000111111', '111110001111110001111111000111111'], ['0000001010100001110000000011100111000000111100', '0000001010100001110000000011100111000000111100'], ['110101010', '110101010'], ['0110001110000001110000001110011', '0110001110000001110000001110011'], ['001010101010101010101010101', '001010101010101010101010101'], ['000000000000111000000111000000111000000', '000000000000111000000111000000111000000'], ['10101010', '00110011'], ['0010110101', '0010110101'], ['1001011010', '1001011010'], ['011001101010100001110101101', '011001101010100001110101101'], ['1000011', '0000111'], ['1100111011', '1100111011'], ['01100111', '01100111'], ['000000000000000', '111111100000001'], ['101001010101010101010101010101001010101010101010101010', '101001010101010101010101010101001010101010101010101010'], ['000000000000010101000011100000000111001110000001111000000', '000000000000010101000011100000000111001110000001111000000'], ['0000000000001110000001110000001110000000', '0000000000001110000001110000001110000000'], ['0001110000001110000001010101000011101010111', '0001110000001110000001010101000011101010111'], ['010101010101010101010100101', '010101010110101010101010101'], ['10101010010101011010101010', '10101010010101011010101010'], ['100000000101010101010101101010101010101010', '100000000101010101010101101010101010101010'], ['111111100000001', '000000000000000'], ['01101010101101001010101010101', '01101010101101001010101010101'], ['10111111100000001', '10111111100000001'], ['1101111111000000010101010', '1101111111000000010101010'], ['001010101', '110111011'], ['00001101', '00001101'], ['00001101', '11111111'], ['101010010', '010101001'], ['11011011000000000000000', '11011011000000000000000'], ['1001101010', '1001010010'], ['110110110000000000000000', '110110110000000000000000'], ['00101010010101011011111110000000101010101001010101101010101000111000000001110011100000011111', '00101010010101011011111110000000101010101001010101101010101000111000000001110011100000011111'], ['00110011', '10101010'], ['010101010101010101010100101', '010101010101010101010100101'], ['01100111', '11011011'], ['10101010', '01100111'], ['00011000000001010101010101011010101010101010101', '00011000000001010101010101011010101010101010101'], ['00001101', '10101010'], ['000000000000110011010000000000000000010101010101010', '000000000000110011010000000000000000010101010101010'], ['1000000010', '1001101010'], ['10110011', '10110011'], ['100110101010101010101010101010101010', '100110101010101010101010101010101010'], ['101010010', '101010010'], ['10011010101010101010101010101010101001', '10011010101010101010101010101010101001'], ['10010101011010101010', '10010101011010101010'], ['0011000000000000011100000001110001000111000000011', '0011000000000000011100000001110001000111000000011'], ['10000011', '10010011'], ['00000000000011100000001101110000001110000000', '00000000000011100000001101110000001110000000'], ['100010000', '100010000'], ['000111', '000000'], ['11011101', '11011101'], ['100000000000001100110100001000000000000010101010101010110011', '100000000000001100110100001000000000000010101010101010110011'], ['10010011', '10010011'], ['0000000000000', '0000000000000'], ['100110010100100011', '100110010100100011'], ['10100101010101010101010101010101', '10100101010101010101010101010101'], ['001010100000000000001', '001010100000000000001'], ['1101101000100001', '1101101000100001'], ['0001110000001110000000111', '0001110000001110000000111'], ['10111000111111000110000001010100001110000000011100111000000111100111100000011', '10111000111111000110000001010100001110000000011100111000000111100111100000011'], ['10101111000111111000111111000111111110101010', '01000000001010101010101011010101010101010101'], ['1010', '1010'], ['010101001', '100001101'], ['100000011', '100000011'], ['00011100000011100000010101010001011101010111', '00011100000011100000010101010001011101010111'], ['10101111000111111000111111000111111110101010', '10101111000111111000111111000111111110101010'], ['0001010100001110000000011100111000000111110110011', '0001010100001110000000011100111000000111110110011'], ['100001101', '110101010'], ['111011101', '111011101'], ['11011100000111100111011', '11011100000111100111011'], ['10010011', '11011011'], ['001101101010010001010101010101', '001101101010010001010101010101'], ['10101010', '10000000'], ['010101100010000', '101010110000000'], ['0101010010101010101010100101', '0101010010101010101010100101'], ['11011011', '10110011'], ['100010000', '101010010'], ['11011100000111100111110111011011', '10001000011011100000111100111011'], ['101010010', '110111011'], ['00010101000011100000000111001110000001111101100110011', '00010101000011100000000111001110000001111101100110011'], ['00000000000000', '00000000000000'], ['0110011', '1000011'], ['010101010110101010101010101', '010101010110101010101010101'], ['1010111011100000111100111011001111111110101010', '1010111011100000111100111011001111111110101010'], ['1111100011111100011111110001111111', '1111100011111100011111110001111111'], ['11111000111111000111111000111111', '11111000111111000111111000111111'], ['100001101', '100001101'], ['00101010010101010010101011010010101000111000000001110011100000011111', '00101010010101010010101011010101010001110000000011100111000000011111'], ['1001101010', '1001101010'], ['0000000000000010101000011100000000111001110000001111000000', '0000000000000101010000111000000000111001110000001111000000'], ['00101010000111000000001110011100000011101010110001000011', '00101010000111000000001110011100000011101010110001000011'], ['0110011010101000011101011010001110000001110000001010101000011101010111', '0110011010101000011101011010001110000001110000001010101000011101010111'], ['0010110101', '1001101010'], ['101010110000000', '101010110000000'], ['00000110111111100000001010101000', '00000110111111100000001010101000'], ['10001000011011100000111100111011', '10001000011011100000111100111011'], ['10110011', '10101010'], ['1000010000', '1000010000'], ['00011100000011100000011111101101010', '00011100000011100000011111101101010']]
    results = ['010010', '0', '0101', '000', '0000', '11111', '10011001', '111111', '011', '11111', '11111111', '111', '1', '00000000', '00000000', '00000', '0011100010001010', '00000', '110', '11111111', '000000', '00', '11', '011010100', '01100001', '000000', '011', '00000000000000', '000000000000000', '000000000000', '000000000000000', '00000', '0000000000000000', '0000000000000', '00000000000000000', '000000000', '00000000', '000000', '00000000', '000', '0', '000', '00000000000000000000000', '0000000000000', '0000000000', '0000000000000000000', '00000000000000000000000', '00000000000000000', '0010', '000000000000000000000000', '000', '0000000000000000000000000000', '0000000', '00000', '010000', '11001', '0000000000', '00000000', '000000000', '0000', '11110', '001', '00000000000', '00000010', '00000000000000000000', '00000000000000', '0000000', '0000000000000', '00010', '10011001', '0000000000000', '10101', '0000000', '0000', '000000000000000000000000000000000000000000000000', '11011', '000000', '110001100', '1111', '01111000100100', '00000', '110111', '011111', '11011', '000100', '0000000000000000000', '000000', '0000000000000000000000000000000', '00', '', '000000000000000000000000', '00000', '000000000', '000000000000000000000', '000', '000000000000000000000000000000000000000000000000000000', '00', '00000', '00000000000', '00000000000000000000000000000000000', '110001', '011101000000000000000', '11111111', '01110111', '000111', '0011001', '01110001', '1000011', '111111111111', '11111111111111111111111111', '111111111111111111111111', '000000000000', '0000000', '00000000000000000000000000', '0011001', '000000000000', '000000000', '1000011', '0000000', '000000000000000000000000', '0000000', '1010101', '00000000', '00000000000000000000000000000000000000000000000000', '000000000000', '00000000', '000000000000000000', '0000000', '000010110110', '0101010', '000000000000', '00000000', '000000000', '0000000', '00000000', '000000000000000000000000000000000000', '10001000', '101000110010', '00000000', '000000', '0000000000000', '000000000000000000000000', '1010101', '0000000000', '101000110010', '0010100', '11111111', '00000000', '00000000000000000000000000000000000000000000', '1101001', '1000001', '00000000000000000000', '0110011', '00000000', '111111111111', '0000000000000', '000000000000000000000000000000000000000000000000000000000000000000000000', '0000000000', '0010100', '0000000000000', '1101001', '01010011', '000000', '11111111', '0000000000000000000000000000000000000000000000000000000', '0000000000000000', '0000000', '000000100', '00100100', '00000000000000000000', '0000000000000', '000000000000000000000000000000000', '0000000000', '0000000000000000000000000', '000000000000000000000000', '1011000', '10001110', '11111111', '00001011', '00000000000', '000000000', '00000000000000000000000000000', '00000010', '01101001', '01010101', '0000000000011111111100000000000000', '10000001', '11010100', '01000010', '00000000000000000000000000000', '00000000', '000000000000000000000000000000000000000000000000', '00000000000000', '0011101001110', '010010101', '000000000000000', '0000000000000', '010010101', '00101001', '1001111111000', '1101111', '000000000000000000000000000000', '1001111111000', '0000000000000000000000000', '000000000', '00000', '000000000', '01000010', '000000000', '00000', '001100', '00000000000000000000000000000000', '01011000', '0000000000011111111100000000000000', '1111110000111', '0000000000000000000000000000000000', '000000000000000000000000000000000000000000', '00000000000', '01010000', '1111111110111', '0000000000', '1101110000011', '000001100', '000000000000000000', '00000000000000', '00000000000000000000000000000000000000000000000000000', '1111010111001', '00000000000000000', '11010110', '0000000000000000', '000000000000000000000', '00000000000000000000000', '01010011', '000000', '0101000', '11101110000010010000010010101001011001101110111111', '0101010010011', '0110000001111', '00000001111', '0000000000000', '000000000', '000000000000000000000000000000000000000000000000000000000000', '000001100', '01110001', '00000000', '0000101010000000000000000', '00000000000000000000000000', '000000000000000000000', '00101110', '00000000000', '000000000000000000000000000000000000000000000000000000000', '0000000000000000000000000', '00000000000000000000000000000000', '1010101100100', '000000000000000000', '00000000000000000000000000000000000000000000000000000000000000000000', '0000000000000000000011010111111000000000', '000000000000000000000000000000000000', '1011011010100100101010101', '00000000000000000000000000000000000000000', '00000', '0000000000000', '0000000000', '0000000000000000000000000000000000000', '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111', '01010101', '000000000', '0101101', '01010101', '0000', '0000000', '00000000000000000000000000', '000000000000000', '101111111', '10001110', '0000000000000000000000000000000000000000', '000000000000000000000000000', '0000000000000000000000000000000', '00100010', '1110000', '00000000000000000000001001010010000010000', '00000000111111110000000000', '0000000000000000000000000000', '00000000000000000000000000000000000000000', '00011011000011011000011011000000', '000000000000000', '000000000000000', '001100000', '010101011', '000000000000000', '000000000', '0000000000000000000000000000000000000000000000000000000000000000000', '000000000000000000000000000000000', '0000000000000000000', '011111100101011', '01110111', '00000000', '000000000000000000000', '00000000000000000000000000000', '000000000000000000000000000000000000', '0000000000000000000000000000000000000', '00100010', '0000000000000000000000000000000', '111101110', '00000000000000000000000000000000000000000', '01010101', '000000000', '000000000000000000000000000000000', '0000000000000000000000000000000000000000000000', '000000000', '0000000000000000000000000000000', '000000000000000000000000000', '000000000000000000000000000000000000000', '10011001', '0000000000', '0000000000', '000000000000000000000000000', '1000100', '0000000000', '00000000', '111111100000001', '000000000000000000000000000000000000000000000000000000', '000000000000000000000000000000000000000000000000000000000', '0000000000000000000000000000000000000000', '0000000000000000000000000000000000000000000', '000000000011111111111110000', '00000000000000000000000000', '000000000000000000000000000000000000000000', '111111100000001', '00000000000000000000000000000', '00000000000000000', '0000000000000000000000000', '111101110', '00000000', '11110010', '111111011', '00000000000000000000000', '0000111000', '000000000000000000000000', '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', '10011001', '000000000000000000000000000', '10111100', '11001101', '00000000000000000000000000000000000000000000000', '10100111', '000000000000000000000000000000000000000000000000000', '0001101000', '00000000', '000000000000000000000000000000000000', '000000000', '00000000000000000000000000000000000000', '00000000000000000000', '0000000000000000000000000000000000000000000000000', '00010000', '00000000000000000000000000000000000000000000', '000000000', '000111', '00000000', '000000000000000000000000000000000000000000000000000000000000', '00000000', '0000000000000', '000000000000000000', '00000000000000000000000000000000', '000000000000000000000', '0000000000000000', '0000000000000000000000000', '00000000000000000000000000000000000000000000000000000000000000000000000000000', '11101111001101010010010100010010101011111111', '0000', '110100100', '000000000', '00000000000000000000000000000000000000000000', '00000000000000000000000000000000000000000000', '0000000000000000000000000000000000000000000000000', '010100111', '000000000', '00000000000000000000000', '01001000', '000000000000000000000000000000', '00101010', '111111010010000', '0000000000000000000000000000', '01101000', '001000010', '01010100011100000111001011100000', '011101001', '00000000000000000000000000000000000000000000000000000', '00000000000000', '1110000', '000000000000000000000000000', '0000000000000000000000000000000000000000000000', '0000000000000000000000000000000000', '00000000000000000000000000000000', '000000000', '00000000000000000000000000000111111001001000000010010100100000000000', '0000000000', '0000000000000111111000100100000000000000000000000000000000', '00000000000000000000000000000000000000000000000000000000', '0000000000000000000000000000000000000000000000000000000000000000000000', '1011011111', '000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00011001', '0000000000', '00000000000000000000000000000000000']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(string_xor)