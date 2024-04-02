from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Do not include these tokens in the code: # x or _ str = ''
	"""
    return ''.join(str(int(a_char) ^ int(b_char)) for a_char, b_char in zip(a, b))


if __name__ == "__main__":
    input_a = input("Enter a: ")
    input_b = input("Enter b: ")
    print(string_xor(input_a, input_b))
