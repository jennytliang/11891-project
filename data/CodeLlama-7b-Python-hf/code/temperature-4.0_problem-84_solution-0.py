def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    def get_bin(num):
        """Gets binary of num
        """    
        i = 2
        val = ""
    
        while(num/i > 0):
            remainder = num % i
            num = num / i
    
            # print("%i remainder is: %i, %i" %(j, num, j*(int)(num) % 100000) )  
            # print(" %i: %i" %((i), num) )  
            
            val += str( 1 if remainder > 0 else 0 )
           
            i *= 2
    

        return val  
    
    
    bin_num = get_bin(N)
    out = str(sum(int(i) for i in bin_num) - len(bin_num))

    return bin_num if get_sum() != N else out


if __name__ =="__main__":