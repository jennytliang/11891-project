def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    
	Include these tokens in the code: return number - int ( number )
	"""
    return number - int(number)


def truncate_number_v2(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
	"""
    return number % 1


def count_positives_unsorted(numbers):
    """Return the count of positive numbers among the given sequence."""
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count


def count_positives_sorted(numbers):
    """Return the count of positive numbers among the given sequence.
    The sequence must be sorted."""
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count


def count_negatives_unsorted(numbers):
    """Return the count of negative numbers among the given sequence."""
    count = 0
    for number in numbers:
        if number < 0:
            count += 1
    return count


def count_negatives_sorted(numbers):
    """Return the count of negative numbers among the given sequence.
    The sequence must be sorted."""
    count = 0
    for number in numbers:
        if number < 0:
            count += 1
    return count


def first_is_odd(numbers):
    """Return True if the first element of the given sequence is odd."""
    return numbers[0] % 2 == 1


def first_is_odd_v2(numbers):
    """Return True if the first element of the given sequence is odd."""
    return numbers and numbers[0] % 2 == 1


def all_odd(numbers):
    """Return True if all elements of the given sequence are odd."""
    for number in numbers:
        if number % 2 == 