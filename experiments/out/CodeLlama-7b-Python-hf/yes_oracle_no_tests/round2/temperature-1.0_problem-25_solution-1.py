from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    
	Include these tokens in the code: import math
	"""
    result = [i for i in range(2, n + 1) if n % i == 0]
    result.append(n)
    return result


def make_pi() -> List[int]:
    """ Generate prime numbers less than 100
    
	Include these tokens in the code: import itertools, import random
	"""
    primes = []
    non_primes = [0, 1]
    for num in (range(1, 100, 2)):
        for prime in primes:
            if prime > int(math.sqrt(num)) + 1:
                break
            if num % prime == 0:
                non_primes.append(num)
                break
        if num in non_primes[:-1]:
            continue
        primes.append(num)
    return primes


def longest_increasing_subsequence(v: List[int]) -> int:
    """ Calculate length of longest strictly increasing subsequence of given sequence .
    For example, if the input is [10, 5, 7, 8, 12, 6], the output should be 3,
    as [5, 7, 8] is the longest sub-sequence that is strictly increasing
    Inputs numbers shouldn't repeat
    
	"""

    v = [0] + v
    v_incr = [False for _ in range(len(v))]     # v_incr[i] == True iff value in v[i] is included in LIS, otherwise all elements are False
    for i in range(len(v) - 1):
        for j in range(i):
            if v[i] > v[j]:
                v_incr[i] = True
    for i in range(len(v) - 1, 0, -1):
        if v_incr[i]:
            return i


def longest_palindromic_subsequence(s: str) -> str:
    """ Calculate longest palindromic subsequence of given string.
    Should return the sequence with length of