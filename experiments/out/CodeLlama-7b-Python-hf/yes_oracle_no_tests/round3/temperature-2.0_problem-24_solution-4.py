def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    
	Do not include these tokens in the code: fo obar = 0
	"""
    #fo = 0
    #obar = 0
    #for i in range(1, n + 1):
        #if n % i == 0:
            #fo = i
            #obar = n // fo
            #if fo > obar:
                #return fo
            #else:
                #return obar
    #return 0
    return n//(max([i for i in range(1, n + 1) if n%i == 0]))

def test_bench():
    test_data = [15, 12, 4]

    for i in test_data:
        print(largest_divisor(i))

if __name__ == "__main__":
    test_bench()
