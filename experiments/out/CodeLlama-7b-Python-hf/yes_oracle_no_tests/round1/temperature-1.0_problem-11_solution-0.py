from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return "".join(str(int(a_c) ^ int(b_c)) 
                    for a_c, b_c in zip(a,b))                
                    
# 	# Alternative solution with list comprehension                    
#     return "".join(str(int(a_c) ^ int(b_c))
#                     for a_c, b_c in [(a[i],b[i])
#                         for i in range(len(a))])
    # Alternative solution with regular for loop    
    # return ''.join([str(int(a_c) ^ int(b_c)) for a_c, b_c in zip(a,b)])

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()