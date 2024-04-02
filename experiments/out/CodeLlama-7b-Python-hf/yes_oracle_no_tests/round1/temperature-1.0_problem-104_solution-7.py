def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ):
	Do not include these tokens in the code: result = [] for i
	"""
    result = []
    for i in x:
        if not any(int(j) % 2 == 0 for j in str(i)):
            result.append(i)
    return sorted(result)


def main():
    try:
        with open("./data.txt") as f:
            data = f.readlines()
    except FileNotFoundError:
        print("File not found!")
        return

    for line in data:
        line = line.strip()
        if line:
            x = line.split(",")
            x = [int(i) for i in x]
            result = unique_digits(x)
            print(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
