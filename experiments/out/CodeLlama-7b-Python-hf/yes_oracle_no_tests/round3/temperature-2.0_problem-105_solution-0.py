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
    
	Include these tokens in the code: word
	Do not include these tokens in the code: w
	"""


    d = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }

    def sort_func(x):
        if x > 9 or x < 1:
            return -10
        return x

    def reverse_func(x):
        if x == -10:
            return -10
        return 10 - x

    def convert_func(x):
        return d[x] if x in d else str(x)

    return list(map(convert_func, sorted(arr, key=reverse_func, reverse=True)))


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([1, -1, 55]))
print(by_length([]))