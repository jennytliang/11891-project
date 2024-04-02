def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Include these tokens in the code: return number -
	Do not include these tokens in the code: integer =
	"""

    # ==========================================================================
    # TODO: 1. Replace the pass statement below with your code.
    # ==========================================================================
    return number - int(number)
    # ==========================================================================
    # HINT: For this problem, you can assume that the input number is positive.
    # ==========================================================================


def main():
    """ Calls the truncate_number function to test your answer. """
    print("truncate_number(3.5) returns", truncate_number(3.5))
    print("truncate_number(3.9) returns", truncate_number(3.9))


# -----------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()