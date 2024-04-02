from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join (
	Do not include these tokens in the code: r = [
	"""
    r = [int(x) ^ int(y) for x, y in zip(a, b)]
    return " ".join(str(i) for i in r)


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '010'], ['110', '110'])
    ['100', '100']
    
	Include these tokens in the code: return [" ".join(
	Do not include these tokens in the code: r = [
	"""
    r = [int(x) ^ int(y) for x, y in zip(a, b)]
    return [" ".join(str(i) for i in r)]


if __name__ == "__main__":
    a = "010"
    b = "110"
    print(string_xor(a, b))
    print(string_xor_list([a, a], [b, b]))
