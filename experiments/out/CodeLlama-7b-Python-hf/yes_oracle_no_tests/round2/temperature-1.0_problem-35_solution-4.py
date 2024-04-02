def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: def max _ element _ v 2 ( l
	"""


    return maax(l, 0, len(l)-1)

def maax(l, left, right):
    if left == right:
        return l[left]
    mid = (left + right) // 2
    left_maax = maax(l, left, mid)
    right_maax = maax(l, mid+1, right)
    if left_maax > right_maax:
        return left_maax
    else:
        return right_maax

print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))

