def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    # sorted_l = sorted(l)
    # if len(sorted_l) % 2 == 1:
    #     return sorted_l[len(sorted_l) // 2]
    # else:
    #     return (sorted_l[len(sorted_l) // 2] + sorted_l[len(sorted_l) // 2 - 1]) / 2
    return sorted(l)[len(l) // 2]


def main():
    print('Answers to the Median problems:')
    print('Should return 3:', median([3, 1, 2, 4, 5]))
    print('Should return 15.0:', median([-10, 4, 6, 1000, 10, 20]))


if __name__ == '__main__':
    main()
