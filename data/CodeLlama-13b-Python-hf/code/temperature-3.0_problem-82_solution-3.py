def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    num_str = str(len(string))
    
    for i in range(2, len(num_str)):
        if num_str[0] == num_str[1] or num_str[0] == num_str[-1]:
            return True
    return False
        
    