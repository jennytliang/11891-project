from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    
	Include these tokens in the code: ()
	Do not include these tokens in the code: ( reverse = False )
	"""


    number_pair = []
    min_dist = min([abs(numbers[i] - numbers[i + 1]) for i in range(len(numbers) - 1)])
    res_index = [(numbers[i], numbers[i + 1])  for i in range(len(numbers) - 1) if numbers[i] + numbers[i + 1] == min_dist]
    min_dist = min([abs(numbers[i + 1] - numbers[i]) for i in range(len(numbers) - 1)])
    res_index += [(numbers[i + 1], numbers[i])  for i in range(len(numbers) - 1) if numbers[i + 1] + numbers[i] == min_dist]
    return sorted(res_index, key = lambda x: x[0])[-1]
		
		
	return sorted([(numbers[i], numbers[i + 1]) for i in range(len(numbers) - 1)])[-1]
		# [(min(numbers[i], numbers[i + 1]), max(numbers[i], numbers[i + 1])) for i in range(len(numbers) - 1)]
		
		
	# num = sorted(numbers)[1:] + [sorted(numbers)[0]]
    # return min([abs(num[i] - num[i + 1]) for i in range(len(num) - 1)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
