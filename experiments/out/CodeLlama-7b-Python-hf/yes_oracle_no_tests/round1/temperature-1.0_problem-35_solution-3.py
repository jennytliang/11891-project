def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return max(l)


print("Example:")
print(max_element([1, 2, 3]))

# These "asserts" are used for self-checking and not for an auto-testing
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0]) == 9
assert max_element([-5, -7, -3]) == -3
assert max_element([3, 3, 5, 3, -3, -5, -3, 3]) == 5

print("Coding complete? Click 'Check' to earn cool rewards!")
