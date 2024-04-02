def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    
	Include these tokens in the code: av
	Do not include these tokens in the code: rounded Av
	"""


    if n > m:
        return -1
    else:    
        return bin(int(round((m-n + 1)/2 ,0)))
      
def round_up_to_even(n):
    """Rounds n up to the nearest even integer. If n is already even, it should be left as it is.
    
    - You may assume that n fits into a 32-bit signed integer.
    - If the result will fit into a 32-bit signed integer, return the result as an integer.
    - If the result will not fit into a 32-bit signed integer, return the result as a long integer.
    - If the result will not fit into either of the above, return the result as a long long integer.
    - If the answer is not possible under the above rules, return -1.
    - Note that the number returned will not necessarily be an integer, and it might be out of range.
    - If a floating point is returned, the conversion will cause it to be rounded towards -inf.
    - Note: this is not the same as casting to int.

    Example:
       round_up_to_even(7) returns 8
       round_up_to_even(11) returns 12
       round_up_to_even(12345) returns 12344
       round_up_to_even(2395904) returns 2395904
       round_up_to_even(94767966) returns 94767968
       round_up_to_even(53475) returns 53480
    """
    import math
    #################################
    # YOUR CODE HERE
    t = int(math.ceil(n / 2.0) * 2)
    if t > 2147483647:
        return -1
        ###############################
#        import math
#        t = int(math.ceil(n / 2.0) * 2)
#        t = math.fabs(t)
#        if t ==