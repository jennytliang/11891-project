def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    answer = 2
    divider = answer if answer == 1 else 2
    while divider ** 2 < n + 1:
        # Check if a factor is not a multiple of any integer before d and itself
        if n % divider != 0 and n % answer != 0:
            # Try the next larger odd number as the new candidate
            divider = divisor_if_prime(answer + divider)
        # If we hit another prime we are ready to set a new max prime and start
        # searching for smaller divisors
        if answer != n and is_prime(-answer):
            # If we hit this point then the largest prime found is our answer so we
            # should just set the answer and step out of the while loop
            return answer
        # We're not prime but still have a factor. Add to the divisor/max prime and repeat
        # the search until we are done searching
        if is_prime(divider):
            # If our previous max was divisible by the present candidate, update our answer
            if n % divider == 0:
                answer = divider
            # Only update our candidate and move on if we did not divide our number above.
            divider = divisor_if_prime(answer + int(divider))
        elif answer != 2:
            # If we had a candidate before, move on to see if the 2 was a real factor
            # by adding 1 to make it odd and searching for that as our next max
            # If that candidate was already odd, we have no 2 candidate.
            divider = int(divider + 2)
    return answer