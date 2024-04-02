def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Do not include these tokens in the code: ans = [] # for example ,
	"""


def get_max_prime_factor(n):
    """write a function that takes in an integer 'n' and return the prime factor of 'n' that is the
    maximum. e.g:
    prime_fact_max(3150) => 31
    prime_fact_max(-34) => 3
    prime_fact_max(5) => 5
    Ex: n = a b c d => where a|b and a|c and a|d, b|c and b|d and c|d where | is 'divide without remainder'
    return the largest value 'a' that satisfies the above condition.
    """


def is_power_of_two (n):
    """write a function that takes in an integer 'n' and returns true if 'n' is a power of two.
    e.g:
    is_power_of_two(32) => true
    is_power_of_two(4) => true
    is_power_of_two(5) => false
    is_power_of_two(7) => false
    is_power_of_two(0) => false
    """


def fizz_buzz (n):
    """write a function that takes in an integer 'n' and returns the following string:
    if n is evenly divisible by 3 and 5, return 'Fizz Buzz'
    if n is evenly divisible by 3 , return 'Fizz'
    if n is evenly divisible by 5 , return 'Buzz'
    if n is not evenly divisible by 3 and 5, return n
    e.g:
    fizz_buzz(3) => 3
    fizz_buzz(5) => 'Buzz'
    fizz_buzz(6) => 'Fizz'
    fizz_buzz(15) =>  'Fizz Buzz'
    """


def sum_of_odd (num1):
    """write a function that takes in a single parameter 'x' and returns the sum of all the odd
    numbers in x's range e