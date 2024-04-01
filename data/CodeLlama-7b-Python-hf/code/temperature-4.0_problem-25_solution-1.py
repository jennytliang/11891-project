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
    """
    # ============== YOUR CODE =================
    return None
    # =========== END OF YOUR FUNCTION ===========


if __name__ == '__main__':
    # ------------ HOW TO RUN TASK ----------
    # 1. Do necessary imports
    import numpy as np  # Library for scientific-computation

    # 2a. Run doctests - All tests (if this line failed, then doctest "passed" with this line is not complete or some
    #     function definition in task code is not completed properly!)
    print('Doctest started!')
    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)
    print('Doctest finished! All examples was type checked and passed!')
    # 2b. Run your doctest examples
    # 3. Write your examples of how your function works in doctests (name of the test starts with '>>> ' and the answer
    #    should be in new line starts with '>>> ' too