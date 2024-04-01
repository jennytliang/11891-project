from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    result_closest = min(numbers[1:], key=abs) - numbers[0]
    for num in numbers[1:-1]:
        if min(min(numbers[-1], abs(num - numbers[0])) - num, result_closest) != result_closest:
            result_closest = num
        if num != numbers[0] and abs(max(numbers[-1], num - numbers[0])) - abs(min(num, numbers[0])) \
                == min(max(numbers[-1], abs(num - numbers[0])) - abs(num), 0):
            break
    return (min(abs(num - numbers[0]) if num < 0 or numbers[0] < 0 else num, numbers[0]) if num != numbers[0]
            else 0, min(abs(num - numbers[0]) if num > 0 or numbers[0] > 0 else num, numbers[0])
            if num != numbers[0] else numbers[1]) if result_closest >= min(2 * numbers[-1], abs(numbers[0])) else (
        numbers[-1] if num == min(abs(num), numbers[-1]) and result_closest != abs(numbers[-1] - num) else 0,
        (numbers[-2] if number == min(abs(num), numbers[-2])
         else max(abs(result_closest - numbers[-1]), numbers[-2])) if num == numbers[-1] else 0)
