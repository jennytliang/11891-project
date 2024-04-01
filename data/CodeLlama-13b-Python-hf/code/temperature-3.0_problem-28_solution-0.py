from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)


TEST_CONCATENATE_1 = [
    {
        'input': [],
        'expected': '',
    },
    {
        'input': ['a', 'b', 'c'],
        'expected': 'abc',
    },
]


def common_endpoint(endpoints: List[str]) -> str:
    """ Get longest prefix shared by all strings

    >>> common_endpoint([])
    ''
    >>> common_endpoint(['/home/user1', '/home/user2', '/home/user3'])
    '/home/'
    >>> common_endpoint(['/home/user', '/home/user/'])
    '/home/user/'
    """

    def longest_common_prefix(strings: List[str]) -> str:
        if not strings or len(strings) == 1:
            return strings[0]

        prefix = ''
        for i, char in enumerate(strings[0]):
            for string in strings:
                if i == len(string) or string[i] != char:
                    return prefix
            prefix += char

        return prefix

    return longest_common_prefix(strings=endpoints)
