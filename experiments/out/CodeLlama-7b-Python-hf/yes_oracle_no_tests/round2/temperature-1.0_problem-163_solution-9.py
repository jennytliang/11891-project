def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Include these tokens in the code: a , b = b , a
	"""


    if  a <= b: # We make sure a is <= b which eliminates needing 
    	       # to use a token to switch a and b.
        a = b 

    for i in range(6):
    	for 
    	
    
    
    # TODO: fill this in



if __name__ == "__main__":
    print(generate_integers(2, 8))
    print(generate_integers(8, 2))
    print(generate_integers(10, 14))
    print(generate_integers(10, 10))
