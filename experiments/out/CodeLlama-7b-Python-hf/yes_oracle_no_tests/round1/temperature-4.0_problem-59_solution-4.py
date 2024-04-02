def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    
	Include these tokens in the code: is prime
	Do not include these tokens in the code: largest _ div or
	"""
    "*** YOUR CODE HERE ***"
    largest = 1
    for i in range(2, n):
        if n % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                largest = i
    return largest


def sum_of_digits(s):
    """Returns the sum of the digits in string s.
    >>> sum_of_digits('789')
    24
    >>> sum_of_digits('')
    0
    >>> sum_of_digits('Jimmy John')
    10
    
	Include these tokens in the code: int str
	Do not include these tokens in the code: sum
	"""
    "*** YOUR CODE HERE ***"
    total = 0
    for i in range(len(s)):
        total += int(s[i])
    return total

def num_e(s):
    """Returns the number of e's in string s (either lowercase or uppercase)
    >>> num_e('Hello')
    1
    >>> num_e('Elle')
    1
    >>> num_e('e')
    1
    >>> num_e('')
    0
    >>> num_e('Heeolole')
    3
    
	Include these tokens in the code: lower
	Do not include these tokens in the code: num
	"""
    "*** YOUR CODE HERE ***"
    total = 0
    for i in range(len(s)):
        if s[i].lower() == 'e':
            total += 1
    return total

def has_no_e(s):
    """Returns True if string s has no e's (either lowercase or uppercase)
    >>> has_no_e('jklol')
    True
    >>> has_no_e('jklOl')
    True
    >>> has_no_e('eliminate')
