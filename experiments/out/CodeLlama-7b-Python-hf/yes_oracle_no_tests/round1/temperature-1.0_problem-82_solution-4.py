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
    length = len(string)
    count = 0
    for num in range(1,length):
        if length % num == 0:
            count+=1
        print(f'num = {num}, count={count}')
            
            
    
    length = len(string)
    count = 0
    for num in range(1,len(string)):
        if len(string) % num == 0:
            count+=1
        return count



    

if __name__ == '__main__':
    prime_length('Hello') == 1
    prime_length('abcdcba') == 2
    prime_length('kittens') == 1
    prime_length('orange') == False