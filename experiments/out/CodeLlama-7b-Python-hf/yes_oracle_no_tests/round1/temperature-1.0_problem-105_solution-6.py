def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    
	Include these tokens in the code: def to _ word ( x : int ) ->
	"""
	result = []
	for a in range(4, 10):
		result.append(str((by_number(a))))
	result.reverse()
	return result

def by_number(num):
	if num is 4:
		return "Four"
	if num is 5:
		return "Five"
	if num is 6:
		return "Six"
	if num is 7:
		return "Seven"
	if num is 8:
		return "Eight"
	if num is 9:
		return "Nine"

def test_by_length():
	assert by_length([]) == []
	assert by_length([1, 1, 2, 2, 3, 4, 5, 8]) == ["One", "One", "Two", "Two", "Three", "Four", "Five", "Eight"]
	assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
	assert by_length([1, -1, 55]) == ['One']
	assert by_length([2]) == ['Two']
	assert by_length([1, 2, 100, 4]) == ['One', 'Two']
	assert by_length([1, 12, 44, 4, 78]) == ['One', 'One', 'Four', 'Four', 'Seven', 'Eight']
