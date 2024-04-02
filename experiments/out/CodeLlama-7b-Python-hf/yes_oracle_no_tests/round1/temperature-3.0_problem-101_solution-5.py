def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
	words = s.replace(", ", " ")
	return words.split()


def extract_numbers(sentence):
    """
    You will be given a sentence as a string.
    The sentence will contain one or more numbers.
    Return a list of all of the numbers contained in the sentence in ascending order.
    
    For example:
    extract_numbers("My house is 2 km away from the train station") == [2]
    extract_numbers("I was traveling with my dog and we saw 3 monkeys") == [3]
    extract_numbers("There are 100 people at least in the room") == [100]
    """
    numbers = []
    for word in sentence.split():
        for char in word:
            if char.isdigit():
                numbers.append(int(char))
    return sorted(numbers)


def is_prime(n):
    """
    A prime number is a natural number greater than 1 that cannot be formed by
    multiplying two smaller natural numbers.
    
    Check if a given number is prime.
    
    For example:
    is_prime(2) == True
    is_prime(15) == False
    """
    if n == 2:
        return True
    elif n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def all_primes(n):
    """
    Write a function that returns all the prime numbers up to a specified number.
    Return them in an array.
    
    For example:
    all_primes(10) == [2, 3, 5, 7]
    """
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


def largest_prime(n):
    """
    Write a function that returns the largest prime number up to a specified number.
    
    For example:
    largest_prime(10) ==