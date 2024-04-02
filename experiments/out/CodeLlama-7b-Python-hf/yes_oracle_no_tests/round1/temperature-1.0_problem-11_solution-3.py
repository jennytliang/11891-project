from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return "".join(str(int(a_i) ^ int(b_i)) for a_i, b_i in zip(a, b))


if __name__ == "__main__":
    # print("110", "010")
    res = string_xor("111", "101")
    print(res)
    # assert(res == "010")

    # assert(string_xor('010', '100') == '110')
    # assert(string_xor('111', '001') == '110')
    # assert(string_xor('11111110', '00100001') == '11010110')
    # assert(string_xor('1010011', '1001011') == '0010000')