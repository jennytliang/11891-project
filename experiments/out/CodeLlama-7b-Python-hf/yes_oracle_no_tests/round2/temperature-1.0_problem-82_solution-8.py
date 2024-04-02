def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # First , make a list of
	"""

    #code goes here
    list_str=[]
    list_str=list(string)
    if not isinstance(string,str) or string== '':
        return None
        raise TypeError("It is not a string , it is {}".format(string, type(string)))
        #raise NotImplementedError()
    elif len([i for i in range(2,len(list_str)+1) if len(list_str)% i == 0]) == 4:
        return False
    elif len([i for i in range(2,len(list_str)+1) if len(list_str)% i == 0]) == 2 and list_str.isalnum():
        return True
    elif len([i for i in range(2,len(list_str)+1) if len(list_str)% i == 0]) == 3 and list_str.isalnum():
        for i in range(0,4):
            del list_str[0] 
        return True
    else:
        return False