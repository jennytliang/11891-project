def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def is _ prime ( a ):
	"""
    def is_prime(a):
        if a < 2:
            return False 
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    return is_prime(len(string))



    # def longest(s1, s2):
    #     """This function takes 2 strings as arguments and returns the longer strings

    #     Use 'is' to do the comparison

    #     Example: longest('longer','long')
    #     >>> 'longest'
    #     """
    #     if s1 is s2:
    #         return s1
    #     elif len(s1) > len(s2):
    #         return s1
    #     elif len(s2) > len(s1):
    #         return s2
    #     else:
    #         return s1
    
    #     def prime_length(string):
    #     """Write a function that takes a string and returns True if the string
    #     length is a prime number or False otherwise
    #     Examples
    #     prime_length('Hello') == True
    #     prime_length('abcdcba') == True
    #     prime_length('kittens') == True
    #     prime_length('orange') == False
    #     
    # 	Include these tokens in the code: def is _ prime ( a ):
    #     """
    #     def is_prime(a):
    #         if a < 2:
    #             return False 
    #         for i in range(2, a):
    #             if a % i == 0:
    #                 return False
    #         return True
    #     return is_prime(len(string))