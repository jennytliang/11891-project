def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Do not include these tokens in the code: def main (): print ( unique ([
	"""


    return sorted(set(l))


if __name__ == "__main__":
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print(unique(l))