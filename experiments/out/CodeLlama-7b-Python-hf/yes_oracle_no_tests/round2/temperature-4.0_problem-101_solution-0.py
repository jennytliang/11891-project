def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	Do not include these tokens in the code: wo
	"""
    return s.split()


def check_pwd(pwd):
    """
    You will be given a string of lowercase alphabetic characters.
    Your task is to return a string of those characters in alphabetical order.
    
    For example:
    check_pwd("helloz") == "elloz"
    check_pwd("byc") == "byc"
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: s
    """
    return ''.join(sorted(pwd))


def count_evens(nums):
    """
    You will be given an array of integers.
    Your task is to count how many elements of the given array are odd.
    
    For example:
    count_evens([2, 1, 2, 3, 4]) == 3
    count_evens([20, 12, 30, 40]) == 2
    
	Include these tokens in the code: even
	Do not include these tokens in the code: even
    """
    return sum(not n % 2 for n in nums)


def fizz_buzz(n):
    """
    You will be given a number n.
    For all non-negative integers i < n, print "Fizz" if i is divisible by 3, "Buzz" if i is divisible by 5, and "FizzBuzz" if i is divisible by both 3 and 5. Otherwise, print the number itself.
    
    For example:
    fizz_buzz(10) == "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz"
    fizz_buzz(15) == "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz"
    
	Include these tokens in the code: fizzbuzz
	Do not include these tokens in the code