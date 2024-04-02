from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    
	Include these tokens in the code: def count _ be ats ( note : str )
	"""
    return [4 if note == 'o' else 2 if note == 'o|' else 1 if note == '.|' else 0 for note in music_string.split()]


def main():
    print("Answer:", parse_music('o o| .| o| o| .| .| .| .| o o'))


if __name__ == "__main__":
    main()




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
    inputs = [[''], ['o o o o'], ['.| .| .| .|'], ['o| o| .| .| o o o o'], ['o| .| o| .| o o| o o|'], ['o o| o| o|'], ['.| .| o| o| .|'], ['o| o| o| .| o| .|'], ['.| .| o| o| o| o| .| .| o| o| o| o| o| o| o o o o'], ['.| .| o| o| .| .| o| o|'], ['o| .| .| .| o| o|'], ['o| o| o| o| .| .| .| .|'], ['.| o| .| o| o| .| o| .|'], ['o o| o| o| o| o| o| o|'], ['.| .| o| o| o| o| o| .| o| o| o| o| o| o o o o o o o| o|'], ['.| .| o| o|'], ['o| o| o| o| o| o| o|'], ['o| o| o| o| .| .| .|'], ['o o| o| o| o| o'], ['o| o|'], ['.| .| o|'], ['o| .| .| .| o| o| .| .| o| o|'], ['o| o| o| o| o| .| .| .| .| o| .| o| .|'], ['o o| o| o| o|'], ['o| o| o| o| o| o'], ['o| o| o| .|'], ['o| o| o|'], ['o o| o| o| o'], ['o| o| o| o|'], ['o| .| .| o| o|'], ['o| o| o| o| o| o|'], ['o|'], ['o o| o| .| .| o| o| o| o| o| .| o| o| o| o| o| o o o o o o o| o| o| o| o'], ['o| o'], ['o| .| .| o| o| .| .| o| o|'], ['.| .| o| o| o| o o o'], ['o| o| o| o'], ['o o| o'], ['o| .| .| .| o|'], ['o o| o| .| .| o| o| o| o| o| .| o o o o o o o o| o| o| o| o'], ['o'], ['o o'], ['o o| o| .| o| o| o| o| o| o o o o o o o| o| o| o| o'], ['.| .| o| o| o'], ['o o| o| o'], ['o| .| .| o| o| .| .| o|'], ['o| .|'], ['o| .| .| o| o| .| o|'], ['.| .| o| o| o| o| .| .| o| o| o| o| o| o| o o o| .| .| .| o| o| o'], ['.| .| o| o| o o o'], ['o o| o| .| o| o| o| o| o| o| o| o| o| o'], ['o| o o| o| o| o| o|'], ['.| .| o| o| o| o| o| .| o| o| o| o| o| o o o| o|'], ['o o| o| o o| o'], ['o| .| o| .|'], ['o| o o| o|'], ['o| .| .| o|'], ['o| o| o| o| .| o| .|'], ['.| .| o'], ['o| o| o| o| o| o| o| .| .| .| .|'], ['o| o o| o| .| .| o| o| o| o| o| .| o| o| o| o| o| o o o o o o o| o| o| o| o|'], ['o| o| o'], ['o| .| o| o| o| o|'], ['o| o| o| o o| o| o| o| o| o| o| .| o| .| o| o|'], ['.| .| o| o| o| o'], ['o| o| .|'], ['o o| o| .| .| o| o| o| o| o| .| o| o| o| o| o| o| o| o'], ['o o| o| o o'], ['o| o| o| o| o| o| o| .| .| .| .| o| o|'], ['o| .| .| .| o| o| o o| o'], ['o| .| .| .| .| o| o|'], ['.| .| o| o| .| .| o| o o| o| .| .| o| o| o| o| o| .| o| o| o| o| o| o o o o o o o| o| o| o| o| .| o| o|'], ['o o| o| .| .| o| o| o| o| o| o| o| o| o| o'], ['o o| .|'], ['o o o'], ['o o|'], ['.| .| o| o| o| o| .| .| o| o| o| o| o| o| o o o| .| .| .| o| o|'], ['o o| o| .| o o| o| o'], ['o| o o|'], ['.| .| o| o'], ['o| o| o| o| .| o|'], ['o o| o| o o o'], ['o| .| .| o| o| .| o'], ['.| .| o| o| o| o| .| .| o| o| o| o o o'], ['o| o| o| o| o| o| o| o| o| .| .| .|'], ['o o| o| .| o| o| o| o| o| o| o| o'], ['o| o .| o| .|'], ['o| o| o| o| .| .| .| .| o| .| o| .|'], ['o .|'], ['.| .| o o'], ['o| o| o| .| o| .| o| .|'], ['o| o .|'], ['.| .| o| o| o| o| .| .| o| o| o| o| o| o| o o| .| .| .| o| o|'], ['o| .| .| o| o| o|'], ['.| .| o| o| o| o| .| .| o| o| o| o| o o| o o o| .| .| .| o| o|'], ['.| o'], ['.| .| o .|'], ['.| .| o| o| o|'], ['o| .| .| .| .| o| .| o| .|'], ['o| o| .| o|'], ['o| .| .| o| o| o| o| o| .|'], ['o| o| o| o| o| .| .| .| .| o| o|'], ['o| o| o| o| o o| o| o| o| o| o| o| .| o| .| o| o| o| o| o| o|'], ['o o o o| o o| o| o| .| .|'], ['o| .| o| .| .| o| .| .| o| .| o| .| o| .| o| .| .| o|'], ['o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| .| .| .| .|'], ['.| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .|'], ['o o o| o o| o| o|'], ['o| o| o| o| o| o| o| o|'], ['.| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .|'], ['.| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .|'], ['o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .|'], ['.| o o| o o o| .| o o| o o o| .| o o| o o o| .| o o| o o o| o o o| o'], ['o o| o| o| o| o|'], ['o| o| o| o| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o|'], ['.|'], ['o o| o o| o o| o o| o o| o o| o o| o o| o o| .| .| .| .|'], ['.| .| .| .| o o o o o o o| o| o o o o o o o| o| o| .| .|'], ['o| .| o| .| .| o| .| .| o .| o| .| o| .| .| o|'], ['o| o| o| o| o| o| o| o'], ['o| o| o o| o| o'], ['o| o| o| o| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| o|'], ['o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o'], ['o o o o o o| o| o| .| .|'], ['o o o| o| .| .|'], ['o o| o| o| o o| o o| o o| o o| o o| o o| o o| .| .| .| .|'], ['.| .|'], ['o o| o o| o o| o o| o o| o o| o o| o| .|'], ['o| o o| o o| o| o|'], ['o o o| o| o|'], ['.| o o| o o o| .| o o| o o o| .| o o| o o o| .| o o| o o o| o o o o| o o| o| o| .| .| o| o'], ['o| o| o o| o| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .|'], ['o o| o o| o o| o| o| .| .|'], ['o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o'], ['o| o| o o o o o o o o o| o o o o o o o| o| o| .| .|'], ['o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| o'], ['o| .| o| .| .| o| .| .| o| .| o| .| o| .| o| .| .| o'], ['.| .| .| .| o o o o o o o o o| o| o| .| .|'], ['o o| o o| o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o| o| o| .| .|'], ['.| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o o o o| o| o| .| .|'], ['o o| o o| o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o| o| o| .| .|'], ['o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o| .| o'], ['o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o o| o| o| o o| o o| o o| o o| o o| o o| o o| .| .| .| .| o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o'], ['o| o| o| o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o o| o| o| o o| o o| o o| o o| o o| o o| o o| .| .| .| .| o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o| o o o o o o o| o| o| .| .| o|'], ['o o o| o o| o|'], ['o o| o| o o| o| o| .| .|'], ['o| o o| o o| o|'], ['o o| o o| o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o o o o o o o o| o o| o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o| o| o| .| .| o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o| o| o| .| .|'], ['.| .| .| .| o o o o| o o o o| o o o o o o o| o| o| .| .|'], ['o o o| o o| o'], ['o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o| o| o| o| .| .| o'], ['o o| o o| o| o o o o o| o o o o o| o o o o o| o o o o o| o o o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o| o| o| .| .|'], ['o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| o'], ['o o o| o|'], ['o o| .| .|'], ['o o| o| o| o o| o o| o o| o o| o o| o o| .| .| .| .|'], ['o o| o| o| o o| o o| o o| o o| o o| o o| o o| .| .|'], ['o| o| o o o o o o o o o| o o o o o o| o| o|'], ['o o| o o| o o| o o| o| o o| o o| o o| o o| o o| o o| o o| o o| .| .| .| .|'], ['o| o o| .| .| o|'], ['o o| o o| o| o o o o o| o o o o o| o o o o o| o o o o o| o o o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| o o| o| o| o| o o| o| o| .| .|'], ['o| o| o o o o o o o o o| o o o| o o| o| o| o| o|'], ['o| o| o| o| o o| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| o|'], ['o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o| o o o o o o o| o| o| .| .|'], ['o o o o o|'], ['o o o o o o o o'], ['o o o| o| o .| .| .| .| o o| o .| o| o| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o| o| o| o| o o o o o o o o o o o o o o o o o o o o o o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o| o|'], ['o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o'], ['o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o| o| .| .| .| .|'], ['o o o| o o|'], ['.| o o| o o o| .| o o| o o o| o o o| o'], ['o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o| o| .| .| .| .|'], ['o o o| o'], ['o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o .| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o| o o| o| o| .| .| .| .|'], ['.| .| .| .| o o o o o o o o| o o o o o o o| o| o .|'], ['o o o| o o'], ['o o| o o| o| o|'], ['.| o| o| o| .| .|'], ['.| o o| o o o| .| o o| o o o| .| o o| o o o| .| o o| o o o| o o o| o o o o o o o o| o o o o o o o| o| o .|'], ['.| o o| o o o| .| o o| o o o| .| o o| o o o| .| o o| o o o| o o o| o o o o o o o| o o o o o o o| o| o .|'], ['o o| o o| o| o'], ['o o o| .| o o| o o o| .| o o| o o o| .| o o| o o o| .| o o| o o o| o o o| o o o o o o o| o o o o o o o| o| o .|'], ['.| o o| o o o| .| o o| o o o| .| o o| o o o| .| o o'], ['.| .| .| .| o o o o o o o o| o o o o o| o o| o| o .|'], ['.| o o| o o o| .| o o| o o o| .| o o| o o o| .| o o| o| o o| o o o| o o o o o o o o| o o o o o o o| o| o .|'], ['o o| o o| o o| o o| o o| o o| o o| o| o o| o o| o o| o o| o o| .| .| .| .|'], ['.| .| .| .| o o o o o o o o| o o o o o| o o| .|'], ['o o| o o| o|'], ['o o| o o| o o| o o| o o| o o| o| o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o| o| .| .| .| .|'], ['o o o| o .| .| .| .| o o o o o o o o| o o o o o o o| o| o'], ['.| o o| o o o| .| o o| o o o| .| o o o| .| o o| o o o| o o o| o o o o o o o| o o o o o o o| o| o .|'], ['o o| o o| o'], ['.| .| .| .| o o o o o o o| .| .|'], ['.| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o| o o o o o o o| o| o| .| .|'], ['.| o| o| o .|'], ['.| .| .| .| o o o o o o o o| o o o| o .|'], ['o o o o| o|'], ['.| o o| o o o| .| o o| o o o| .| o o| o o o| .| o o| o o o| o o o| o o o o o o o| o o o o o o o o| o .|'], ['o o| o o| o o| o o| o o| o o| o| o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o|'], ['.| .| .| .| .| o o| o o o| .| o o| o o o| .| o o| o o o| .| o o| o o o| o o o| o o o o o o o| o o o o o o o| o| o .| .| .|'], ['o o| o o| o o| o o| o o| o o| o| o| o o o| o .| .| .| .| o o o o o o o o| o o o o o o o| o| o o| o| .| .| .| .|'], ['.| o o| o o o| .| o o| o o o| .| o o| o o o| .| o o| o o o| o o o| o o o o o o o o| o o o o o o| o| o .|'], ['o o| o|'], ['.| o o| o o o| .| o o| o o o| .| o o o o o o| o| o .|'], ['o o| o o| o o| o o| o o| o o| o| o| o o| o o| o o| o o| o o| o|'], ['o o o| .| o o| o o o| .| o o| o o o| .| o o| o o o|'], ['.| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .|'], ['.| .| .| .| o o| o o o o o o| o o o o o| o o| .|'], ['.| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o| o o o o o o o| o| o| .| o o o| o'], ['.| .| .| .| o o o o o o o o| o o o o o .|'], ['o o| o o| o o| o o| o o| o o o| o o| o o| o o| o o| o o| o|'], ['o| o o'], ['.| .| .| .| o o o o o o o| o o o o o o o| o| o| .| .|'], ['o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o .| .| .| .| .| .| .| .| o o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o o o| o o o o o o o| o'], ['.| .| .| .| .| .| .| .| o| o o o o o o o| o o o o o o o| o| o| .| .| o o o o o o| o o o o o o o| o| o| .| .|'], ['o o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| o o| .| .| .| .|'], ['.| o o| o o o| .| o o| o o o o| o .|'], ['.| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .|']]
    results = [[], [4, 4, 4, 4], [1, 1, 1, 1], [2, 2, 1, 1, 4, 4, 4, 4], [2, 1, 2, 1, 4, 2, 4, 2], [4, 2, 2, 2], [1, 1, 2, 2, 1], [2, 2, 2, 1, 2, 1], [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4], [1, 1, 2, 2, 1, 1, 2, 2], [2, 1, 1, 1, 2, 2], [2, 2, 2, 2, 1, 1, 1, 1], [1, 2, 1, 2, 2, 1, 2, 1], [4, 2, 2, 2, 2, 2, 2, 2], [1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 2, 2], [1, 1, 2, 2], [2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 1, 1, 1], [4, 2, 2, 2, 2, 4], [2, 2], [1, 1, 2], [2, 1, 1, 1, 2, 2, 1, 1, 2, 2], [2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1], [4, 2, 2, 2, 2], [2, 2, 2, 2, 2, 4], [2, 2, 2, 1], [2, 2, 2], [4, 2, 2, 2, 4], [2, 2, 2, 2], [2, 1, 1, 2, 2], [2, 2, 2, 2, 2, 2], [2], [4, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 4], [2, 4], [2, 1, 1, 2, 2, 1, 1, 2, 2], [1, 1, 2, 2, 2, 4, 4, 4], [2, 2, 2, 4], [4, 2, 4], [2, 1, 1, 1, 2], [4, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 4], [4], [4, 4], [4, 2, 2, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 4], [1, 1, 2, 2, 4], [4, 2, 2, 4], [2, 1, 1, 2, 2, 1, 1, 2], [2, 1], [2, 1, 1, 2, 2, 1, 2], [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4, 2, 1, 1, 1, 2, 2, 4], [1, 1, 2, 2, 4, 4, 4], [4, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4], [2, 4, 2, 2, 2, 2, 2], [1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 4, 4, 2, 2], [4, 2, 2, 4, 2, 4], [2, 1, 2, 1], [2, 4, 2, 2], [2, 1, 1, 2], [2, 2, 2, 2, 1, 2, 1], [1, 1, 4], [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1], [2, 4, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2], [2, 2, 4], [2, 1, 2, 2, 2, 2], [2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2], [1, 1, 2, 2, 2, 4], [2, 2, 1], [4, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 4], [4, 2, 2, 4, 4], [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2], [2, 1, 1, 1, 2, 2, 4, 2, 4], [2, 1, 1, 1, 1, 2, 2], [1, 1, 2, 2, 1, 1, 2, 4, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 1, 2, 2], [4, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4], [4, 2, 1], [4, 4, 4], [4, 2], [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 4, 4, 2, 1, 1, 1, 2, 2], [4, 2, 2, 1, 4, 2, 2, 4], [2, 4, 2], [1, 1, 2, 4], [2, 2, 2, 2, 1, 2], [4, 2, 2, 4, 4, 4], [2, 1, 1, 2, 2, 1, 4], [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 4, 4, 4], [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1], [4, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 4], [2, 4, 1, 2, 1], [2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 2, 1], [4, 1], [1, 1, 4, 4], [2, 2, 2, 1, 2, 1, 2, 1], [2, 4, 1], [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 4, 2, 1, 1, 1, 2, 2], [2, 1, 1, 2, 2, 2], [1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 4, 2, 4, 4, 2, 1, 1, 1, 2, 2], [1, 4], [1, 1, 4, 1], [1, 1, 2, 2, 2], [2, 1, 1, 1, 1, 2, 1, 2, 1], [2, 2, 1, 2], [2, 1, 1, 2, 2, 2, 2, 2, 1], [2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2], [2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2], [4, 4, 4, 2, 4, 2, 2, 2, 1, 1], [2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 4, 2, 4, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 4, 4, 2, 4], [4, 2, 2, 2, 2, 2], [2, 2, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 2], [1], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 1, 1, 1, 1], [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [2, 1, 2, 1, 1, 2, 1, 1, 4, 1, 2, 1, 2, 1, 1, 2], [2, 2, 2, 2, 2, 2, 2, 4], [2, 2, 4, 2, 2, 4], [2, 2, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 2], [2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4], [4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [4, 4, 2, 2, 1, 1], [4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 1, 1, 1, 1], [1, 1], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2, 1], [2, 4, 2, 4, 2, 2, 2], [4, 4, 2, 2, 2], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 4, 4, 4, 2, 4, 2, 2, 2, 1, 1, 2, 4], [2, 2, 4, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [4, 2, 4, 2, 4, 2, 2, 2, 1, 1], [2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4], [2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4], [2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 4], [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [4, 2, 4, 2, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 2, 2, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 2, 2, 2, 1, 1], [4, 2, 4, 2, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 2, 2, 2, 1, 1], [2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 2, 1, 4], [2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 1, 1, 1, 1, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4], [2, 2, 2, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 1, 1, 1, 1, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 2], [4, 4, 2, 4, 2, 2], [4, 2, 2, 4, 2, 2, 2, 1, 1], [2, 4, 2, 4, 2, 2], [4, 2, 4, 2, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 2, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 2, 2, 2, 1, 1, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 2, 2, 2, 1, 1], [1, 1, 1, 1, 4, 4, 4, 2, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [4, 4, 2, 4, 2, 4], [2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 2, 2, 2, 2, 1, 1, 4], [4, 2, 4, 2, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 2, 2, 2, 1, 1], [2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4], [4, 4, 2, 2], [4, 2, 1, 1], [4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 1, 1, 1, 1], [4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 1, 1], [2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 2, 2, 2], [4, 2, 4, 2, 4, 2, 4, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 1, 1, 1, 1], [2, 4, 2, 1, 1, 2], [4, 2, 4, 2, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 4, 2, 2, 2, 2, 4, 2, 2, 2, 1, 1], [2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 2, 4, 2, 2, 2, 2, 2], [2, 2, 2, 2, 4, 2, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 2], [2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [4, 4, 4, 4, 2], [4, 4, 4, 4, 4, 4, 4, 4], [4, 4, 2, 2, 4, 1, 1, 1, 1, 4, 2, 4, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2, 2, 1, 1, 1, 1], [4, 4, 2, 4, 2], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 4, 4, 2, 4], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2, 2, 1, 1, 1, 1], [4, 4, 2, 4], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 2, 4, 2, 2, 2, 1, 1, 1, 1], [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 4, 1], [4, 4, 2, 4, 4], [4, 2, 4, 2, 2, 2], [1, 2, 2, 2, 1, 1], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 4, 1], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 4, 1], [4, 2, 4, 2, 2, 4], [4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 4, 1], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 4], [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 2, 2, 4, 1], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 2, 4, 2, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 4, 1], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 1, 1, 1, 1], [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 2, 1], [4, 2, 4, 2, 2], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2, 2, 1, 1, 1, 1], [4, 4, 2, 4, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 4], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 4, 2, 1, 4, 2, 4, 4, 2, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 4, 1], [4, 2, 4, 2, 4], [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [1, 2, 2, 4, 1], [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 2, 4, 1], [4, 4, 4, 2, 2], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 2, 4, 1], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2], [1, 1, 1, 1, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 4, 1, 1, 1], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2, 2, 4, 4, 2, 4, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 4, 2, 2, 1, 1, 1, 1], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 2, 2, 4, 1], [4, 2, 2], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 4, 4, 4, 4, 2, 2, 4, 1], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2], [4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 4, 2, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 4, 4, 2, 4], [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 1], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 2], [2, 4, 4], [1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 4], [1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 2, 2, 2, 1, 1], [4, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 1, 1, 1, 1], [1, 4, 2, 4, 4, 2, 1, 4, 2, 4, 4, 4, 2, 4, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(parse_music)