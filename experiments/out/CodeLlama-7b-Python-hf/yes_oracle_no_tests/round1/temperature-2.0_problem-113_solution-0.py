def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    
	Include these tokens in the code: ans , template
	Do not include these tokens in the code: output
	"""
    # BEGIN PROBLEM 0
    return ["the number of odd elements %dn the str%dn the %dnput." % (len(lst[i])-lst[i].count("0"),i,i) for i in range(len(lst))]
    # END PROBLEM 0


def sum_of_numbers(s):
    """
    Given a string of space-separated integers, return the sum of the integers.

    >>> sum_of_numbers('1 2 3')
    6
    >>> sum_of_numbers('1 2 1')
    4
    >>> sum_of_numbers('10 12 15 1')
    46
    >>> sum_of_numbers('1 -2 1')
    0

    """
    # BEGIN PROBLEM 1
    return sum(int(i) for i in s.split())
    # END PROBLEM 1


def common_end(a, b):
    """Returns True if a and b share the same last element.

    >>> common_end('ab', 'abc')
    True
    >>> common_end('ab', 'bc')
    False
    >>> common_end('abc', 'abc')
    True
    >>> common_end('abc', 'axc')
    False
    >>> common_end('abc', 'axcx')
    False
    >>> common_end('', 'd')
    False
    >>> common_end('', '')
    True
    """
    # BEGIN PROBLEM 2
    return a[-1] == b[-1]
    # END PROBLEM 2


def common_end_iter(a, b):
    """Returns True if a and b share the same last element.

    >>> common_end('ab', 'abc')
    True
    >>> common_end('ab', 'bc')
    False
    >>> common_end('abc', 'abc')
    True
    >>> common_end('abc', 'axc')
    False
    >>> common_end('abc', 'axcx')
    False
    >>>