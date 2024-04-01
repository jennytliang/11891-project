def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return False
    for i in range(2, len(string)):
        if len(string) % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(prime_length('Hello'))
    print(prime_length('kittens'))
    print(prime_length('orange'))
