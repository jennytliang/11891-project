def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return
	Do not include these tokens in the code: if
	"""
    
    x=0
    y=n-2
    for i in range(int((n/2)+1)):
        print(i)
        for j in range(int((y/2)+1)):
            print(j)
            if x+y==n:
                return True
            else:
                x+=2
                y-=2
    return False

def is_equal_to_sum_div_4(n):
    """Evaluate whether given number n can be written as the sum of exactly 4 positive integers divisible by 4
    Example is_equal_to_sum_div_4(4) == False
    is_equal_to_sum_div_4(8) == True
    is_equal_to_sum_div_4(10) == False
    Do not include these comments in the code: """
    """""""""
    """ is_equal_to_sum_div_4(n) == F
     
                                F"""
    if n%4==0:
        x=2
        y=n-2
        for i in range(int((n/2)+1)):
            print(i)
            for j in range(int((y/2)+1)):
                print(j)
                if x+y==n:
                    if(i>0 and j>0):
                        return True
                else:
                    x+=4
                    y-=4
    return False
def is_equal_to_sum_powers_of_2(n):
    """Evaluate whether given number n can be written as the sum of exactly 4 positive integers a,b,c and d where a=2^k with k>0,b=2^l with l>0,c=2^m with m>0, and d=2^n with n>0
    
    Example is_equal_to_sum_powers_of_2(0) == (False,(0,0,0,0))
    is_equal_to_sum_powers_of_2(4) == (False,(0,4,0,0))
	is