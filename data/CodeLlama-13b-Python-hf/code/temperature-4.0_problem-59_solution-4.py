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
            divider = int(divider + 1)
            while divider in (1, 4, answer, 2 * answer):
                # Divider + 1 will be even. This means that dividing it by the
                # answer/candidate or by half of the answer will result in a non-prime
                # and will always give another candidate to try if it does hit a prime
                tmp = (divider + int(answer / 2)) % int(2 * answer) if answer % 2 == 0 \
                    else (divider + answer + int(answer / 2)) % int(2 * answer)
                if tmp % int(2 * answer) < divider % int(2 * answer):
                    # This next line is important: it means we've found a candidate
                    # but we also need to make sure to update the number
                    # that this candidate was calculated from so we don't end up with
                    # any duplication
                    dev = tmp if tmp < divider else (tmp + int(answer)
                                                     if (answer - divider) < tmp else tmp + answer)
                    # Check to be sure that next candidate is prime (or odd if the last candidate was 2)
                    if n % dev != 0 and is_prime(dev):
                        # If we found a prime, update the answer
                        answer = dev
                divider = int((divider + answer - 1 if divider + answer > 2 * divider else divider + answer + 1)
                              / (answer - 1) + answer)
        # If the max factor we find does not divide it, our answer will be the same. Just repeat the test
                if answer != n and not (n/answer % answer) % answer:
                    # If we are not done and answer does not divide into the original number, we can bail.
                    # If we find out answer does divide it, we have found a larger prime factor and must move
                    # to find the largest of that prime's factors instead
                    break  # exit loop if answer does divide or answer hits our current max, (2 * answer)
                divider = divider_by_multiples_of_three_or_five(n, int(divider + 1), answer)

    # If no other dividers are given (or no numbers have been found to check for prime) we should
    # have already returned. If that wasn't the case in the case of an exception we should print that.
    # If we are done searching for divisors but no number was found that satisfies our criteria
    # return our most recently calculated answer, as it may be prime if no previous answer was
    return answer