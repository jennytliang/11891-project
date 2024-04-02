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
    arr2 = [one_word(x) if abs(x) <= 9 else one_word_no_order(abs(x)) for x in sorted(arr, reverse = True)]
    return [a for a in arr2 if a is not None]

def one_word_no_order(i):
    lookup = {1: "One",
              2: "Two",
              3: "Three",
              4: "Four",
              5: "Five",
              6: "Six",
              7: "Seven",
                8: "Eight",
                9: "Nine"}
    res = lookup.get(i)
    if res is not None:
        return res

def one_word(i):
    lookup = {1: "One",
              2: "Two",
              3: "Three",
              4: "Four",
              5: "Five",
              6: "Six",
              7: "Seven",
                8: "Eight",
                9: "Nine",
               10: "Ten",
               11: "Eleven",
               12: "Twelve",
               13: "Thirteen",
               14: "Fourteen",
               15: "Fifteen",
               16: "Sixteen",
               17: "Seventeen",
               18: "Eighteen",
               19: "Nineteen"}
    res = lookup.get(i)
    if res is not None:
        return res
    
    lookup2 = {10: "Ten",
               20: "Twenty",
               30: "Thirty",
               40: "Forty",
               50: "Fifty",
               60: "Sixty",
               70: "Seventy",
               80: "Eighty",
               90: "Ninety"}
    res2 = lookup.get(i - 10)
    res = lookup2.get(i - int(not not (i % 10)))
    if