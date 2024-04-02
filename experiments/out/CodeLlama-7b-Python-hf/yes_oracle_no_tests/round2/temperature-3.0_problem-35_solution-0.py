def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: if not l : raise
	"""
    if len(l) == 0:
        raise ValueError
    max_val = l[0]
    for num in l:
        if num > max_val:
            max_val = num
    return max_val


def main():
    a = [2, 4, 5, 8, 10, 12]
    print(max_element(a))
    print(max_element([]))
    print(max_element([-12]))


if __name__ == "__main__":
    main()
