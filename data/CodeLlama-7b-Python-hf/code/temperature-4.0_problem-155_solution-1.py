def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # your code here
    def count(num, type):
        count = 0
        while type(num) != 0:
            if num == type:
                return 1
            else:
                return count + count(num//10, type)
    return (even_count(num), other_count(num)) 
      
       
         

