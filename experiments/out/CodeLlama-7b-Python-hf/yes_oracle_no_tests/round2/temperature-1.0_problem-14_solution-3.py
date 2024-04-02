from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Do not include these tokens in the code: return [ s for s in
	"""
    result = []
    for i in range(len(string)):
        result += [string[:i+1]]
    return result


# tests
import os
import random
import string

random.seed(1234)
N = 10000
STRING_INPUTS = [
    "".join(random.choices(string.ascii_uppercase, k=10))
    for _ in range(N)
]

tests_dir = os.path.dirname(__file__)
populated_tests_dir = os.path.join(tests_dir, 'test_data')

single_input_data = os.path.join(populated_tests_dir, 'input_int.txt')
single_result_data = os.path.join(populated_tests_dir, 'output_int.txt')


def test():
    # tests from question description
    q1 = all_prefixes("")
    assert q1 == [""]

    q2 = all_prefixes("a")
    assert q2 == ["a", ""]

    q3 = all_prefixes("bac")
    assert q3 == ["b", "ba", "bac", "c", "ca", ""]

    # some larger test cases
    with open(single_input_data, 'r') as data:
        inputs = data.readlines()
        with open(single_result_data, 'r') as result:
            for (i, (li, lr)) in enumerate(zip(inputs, result)) :
                s, expected_result = li.strip(), lr.strip()
                assert all_prefixes(s) == expected_result.split(" ")


if __name__ == "__main__":
    test()
