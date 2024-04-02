def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge
	Do not include these tokens in the code: # The idea is to keep
	"""
    # pass
    # unique_digits = []
    # for num in x:
    #     if num > 0:
    #         num_str = str(num)
    #         num_list = list(num_str)
    #         for digit in num_list:
    #             if int(digit) % 2 == 0:
    #                 break
    #         else:
    #             unique_digits.append(num)
    # return sorted(unique_digits)

    # unique_digits = []
    # for num in x:
    #     if num > 0:
    #         num_str = str(num)
    #         num_list = list(num_str)
    #         for digit in num_list:
    #             if int(digit) % 2 == 0:
    #                 break
    #         else:
    #             unique_digits.append(num)
    # return sorted(unique_digits)

    # def judge(num):
    #     if num > 0:
    #         num_str = str(num)
    #         num_list = list(num_str)
    #         for digit in num_list:
    #             if int(digit) % 2 == 0:
    #                 return False
    #         else:
    #             return True
    # return sorted([num for num in x if judge(num)])

    def judge(num):
        if num > 0:
            num_str = str(num)
            num_list = list(num_str)
            for digit in num_list:
                if int(digit) % 2 == 0:
                    return False
            else:
                return True
    return sorted([num for num in x if judge(num)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
