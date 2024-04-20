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
    def to_word(n):
        return {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }.get(n, 'Invalid')

    if arr:
        return list(map(to_word, sorted(filter(lambda x: x in range(1, 10), arr), reverse=True)))
    else:
        return []


if __name__ == '__main__':
    print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
    print(by_length([2, 1, 1, 4, 5, 8, 2, 3, 6]))
    print(by_length([]))
    print(by_length([1, -1, 55]))
    print(by_length([2, 2, 2, 2, 1, 1, 1, 1]))