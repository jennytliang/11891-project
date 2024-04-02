def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: This function will take a list of
	"""
    ans = 0
    for item in lst:
        n = lst.index(item)
        if ((n % 3) == 0 and n > 0 and n < len(lst)):
            ans += item * item
        elif (((n % 4) == 0) and (n > 0) and (n < len(lst))):
            ans += item * item * item
        else:
            ans += item
            
    return ans
    
print sum_squares( [1,2,3] )

            
# =============================================================================
# This function will take a list of integers and will return all values in the list which are a multiple of 3 and 4.
# =============================================================================
def fizz_buzz(lst):
    """
    FizzBuzz Test.
    """
    lst3 = lst
    for item in lst:
        if (item % 3 == 0) and (item % 4 == 0):
            lst3.remove(item)
            lst3.append('FizzBuzz')
    return lst3

# =============================================================================
# Expected to return true if the given number is a power of 3
# =============================================================================
def is_power_of_three(n):
    """
    This function takes an integer n and returns true if n is a power of 3, returns false if n 
    is a not a power of 3. 
    """
    return ((1162261467 % (n**3)) & n) == 0
   
# =============================================================================
# This function takes 2 integers x and y and returns a set of all intergers 
# which can be expressed as xn + y
# =============================================================================
def find_multiples(x, y):
    """
    From the set of all integers, select those integers which can be expressed 
    as the sum of an integer x and a integer y.
    
    Examples:
    For x = 2 and y = 5, the output should be [7, 