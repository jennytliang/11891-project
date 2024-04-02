from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    digits = []

    for k, v in map(lambda x: x.split(), numbers.strip().split()).items():
        digits.append((k, " ".join(v)))

    return " ".join(sorted([x_y[1] for x_y in digits if x_y[0].isdigit()]))


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        sort_numbers("One seven four two one two five three four six")
        == "One two two three four four five seven"
    ), "Sorted"
    assert (
        sort_numbers(
            "Five six three two eight nine ten seven one Five six three two eight nine ten seven"
        )
        == "Two three two five six seven seven eight eight nine nine ten"
    ), "Upside down"
    assert (
        sort_numbers("A four two one six three seven four three two one")
        == "One one two two three three four four six"
    ), "Out of order"
    assert (
        sort_numbers(
            "A four two one six three seven four three two one A four two one six three seven four three two one"
        )
        == "One one two two three three four four six"
    ), "I'm not in the string"
    assert (
        sort_numbers(
            "four one three two six four two one two two five four two three three four six"
        )
        == "two two two three three four four four five six"
    ), "A tie"
    assert (
        sort_numbers("") == ""
    ), "Empty"
    assert (
        sort_numbers("one") == "one"
    ), "One"
