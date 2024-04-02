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
    
	Do not include these tokens in the code: # 1 st solution :
	"""
    def get_digit(num):
        if num == 1:
            return 'One'
        if num == 2:
            return 'Two'
        if num == 3:
            return 'Three'
        if num == 4:
            return 'Four'
        if num == 5:
            return 'Five'
        if num == 6:
            return 'Six'
        if num == 7:
            return 'Seven'
        if num == 8:
            return 'Eight'
        if num == 9:
            return 'Nine'

    def get_number(num):
        if num == 1:
            return 1
        if num == 2:
            return 2
        if num == 3:
            return 3
        if num == 4:
            return 4
        if num == 5:
            return 5
        if num == 6:
            return 6
        if num == 7:
            return 7
        if num == 8:
            return 8
        if num == 9:
            return 9

    def by_length(arr):
        if len(arr) == 0:
            return []
        arr.sort()
        arr.reverse()
        arr_new = []
        for i in arr:
            if i >= 1 and i <= 9:
                arr_new.append(get_digit(i))
        return arr_new

    def get_number(num):
        if num == 1:
            return 1
        if num == 2:
            return 2
        if num == 3:
            return 3
        if num == 4:
            return 4
        if num == 5:
            return 5
        if num == 6:
            return 6
        if num == 7:
            return 7
        if num == 8:
            return 8
        if num == 9:
            return 9

    def get_digit(num):
        if num == 1:
            return '