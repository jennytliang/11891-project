from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    
    numbers_list = numbers.split(" ")
    numbers_list = filter(lambda x: x, numbers_list)
    numbers_list = set(numbers_list)
    
    num_dict = {"zero": 0,
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9}
    
    numbers_lst2 = []  
    
    for num in numbers_list:
        for k, v in num_dict.items():
            if num == k:
                numbers_lst2.append(v)
    
    numbers_lst3 = list(map(str, sorted(numbers_lst2)))
    num_dict = {v: k for k, v in num_dict.items()}

    return " ".join([num_dict[int(num)] for num in numbers_lst3])

    # numbers_lst = []
    # numbers_lst.append([int(x) for x in numbers.split()])
    
    # numbers_lst2 = sorted(numbers_lst)

    # return numbers_lst2

    # numbers_lst = list(map(int, numbers.split()))
    # numbers_lst.sort()
    # return " ".join(map(str, numbers_lst))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
