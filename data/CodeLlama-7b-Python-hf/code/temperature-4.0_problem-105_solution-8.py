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
    """
    if arr is None or len(arr) <= 0: return []
    digits = arr.copy()
    if len(arr) >= 1: digits.sort(key=abs)

    # reverse all numbers in list
    for _ in range( digits.count(9)-1 ):
        digits.remove(9) # removes all '9' not just one
        digits.insert(-1,9)
    for i in reversed(digits):
        arr.insert( len(arr)-arr.index(i) , i )  # insert digits back in its place with reverse
    # translate arr to string using a dictionary hash table:
    return arr.translate( dict(( x , x.replace( str( x ) , eval( str( x ) + 'letter' ).upper() ) if ( x>=1 ) else x ) for x in range (1,10)))