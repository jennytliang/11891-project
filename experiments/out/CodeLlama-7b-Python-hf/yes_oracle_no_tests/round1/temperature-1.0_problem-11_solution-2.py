from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return "".join(str(int(a_digit) ^ int(b_digit)) for a_digit, b_digit in zip(a, b))


def get_message_from_cipher_list(cipher_list: List[str]) -> str:
    """ Input is a list of strings representing ciphertexts.
    The ciphertexts have the same length and are all 0s and 1s.
    These may or may not be encrypted with XOR cipher,
    and that should be decoded from the texts themselves.
    Return message obtained by decrypting cipher_list, a list of ciphertexts.

    >>> cipher_1 = '001001001010111010111101'
    >>> cipher_2 = '0001010010110010010111101'
    >>> get_message_from_cipher_list([cipher_1,cipher_2])
    'hello'
    """
    message = ""
    len_cipher = len(cipher_list[0])

    if len(cipher_list) > 1:
        for index, char_list in enumerate(string_xor(cipher_list[0], cipher_list[1]).split()):
            xor_value = reduce(lambda x, y: x | y, (int(char) for char in char_list), 0)
            message += chr(xor_value)

    return message


if __name__ == "__main__":
    doctest.testmod()
