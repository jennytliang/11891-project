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
    return answer, n/answer if n/answer != answer else 1





import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[15], [27], [63], [330], [13195], [100], [256], [500], [873], [9999], [121], [1764], [4096], [243], [1024], [4097], [1765], [120], [501], [4095], [10000], [255], [1025], [4094], [242], [1763], [254], [9998], [872], [9997], [502], [119], [9996], [874], [253], [252], [1762], [122], [4098], [871], [1023], [9995], [870], [99], [98], [118], [1761], [117], [123], [10001], [87], [92], [869], [1766], [93], [875], [244], [9994], [1767], [1760], [124], [245], [116], [9], [88], [10], [86], [246], [85], [115], [247], [1022], [91], [248], [125], [94], [10002], [249], [1768], [876], [38], [868], [1020], [8], [1026], [90], [866], [39], [867], [9993], [1027], [9992], [1029], [1028], [40], [18], [60], [49], [95], [48], [114], [96], [72], [1030], [9991], [13433], [456745], [568623], [32767], [4], [6], [12], [21], [13432], [13434], [22], [32766], [13435], [20], [456744], [568622], [81], [456743], [456742], [13431], [32765], [80], [456741], [456746], [32764], [32763], [568621], [82], [568624], [32768], [13430], [456740], [13429], [456739], [32762], [32769], [456747], [14], [32761], [32770], [568620], [24], [52], [568625], [51], [456738], [30], [50], [32760], [13428], [13427], [1000000], [16], [25], [13436], [456749], [13437], [26], [456748], [568626], [13438], [13439], [456750], [456751], [456752], [28], [32759], [84], [456753], [65], [64]]
    results = [5, 3, 7, 11, 29, 5, 2, 5, 97, 101, 11, 7, 2, 3, 2, 241, 353, 5, 167, 13, 5, 17, 41, 89, 11, 43, 127, 4999, 109, 769, 251, 17, 17, 23, 23, 7, 881, 61, 683, 67, 31, 1999, 29, 11, 7, 59, 587, 13, 41, 137, 29, 23, 79, 883, 31, 7, 61, 263, 31, 11, 31, 7, 29, 3, 11, 5, 43, 41, 17, 23, 19, 73, 13, 31, 5, 47, 1667, 83, 17, 73, 19, 31, 17, 2, 19, 5, 433, 13, 17, 3331, 79, 1249, 7, 257, 5, 3, 5, 7, 19, 3, 19, 3, 3, 103, 103, 101, 547, 17231, 151, 2, 3, 3, 7, 73, 2239, 11, 127, 2687, 5, 19031, 284311, 3, 919, 1597, 37, 6553, 5, 2671, 113, 8191, 163, 6389, 41, 5077, 2, 79, 557, 1033, 401, 16381, 331, 152249, 7, 181, 113, 13, 3, 13, 4549, 17, 76123, 5, 5, 13, 373, 463, 5, 2, 5, 3359, 5503, 1493, 13, 1283, 94771, 6719, 151, 29, 691, 28547, 7, 47, 7, 13841, 13, 2]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(largest_prime_factor)