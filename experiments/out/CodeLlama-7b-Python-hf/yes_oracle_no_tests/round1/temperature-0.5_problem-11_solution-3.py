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


def string_xor_list(s: str) -> List[str]:
    """ Input is a string s consisting only of 1s and 0s.
    Perform binary XOR on this input and return result as a list of strings.
    >>> string_xor_list('110')
    ['100', '010', '001']
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return [string_xor(s, s[::-1]) for s in [s, s[::-1]]]


def string_xor_dict(s: str) -> dict:
    """ Input is a string s consisting only of 1s and 0s.
    Perform binary XOR on this input and return result as a dictionary.
    >>> string_xor_dict('110')
    {'010': '100', '100': '010', '110': '001'}
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return {s: string_xor(s, s[::-1]) for s in [s, s[::-1]]}


def string_xor_set(s: str) -> set:
    """ Input is a string s consisting only of 1s and 0s.
    Perform binary XOR on this input and return result as a set.
    >>> string_xor_set('110')
    {'001', '100', '010'}
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return {string_xor(s, s[::-1]) for s in [s, s[::-1]]}


if __name__ == "__main__":
    import doctest

    doctest.test