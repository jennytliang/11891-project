def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    
	Include these tokens in the code: ==
	Do not include these tokens in the code: !=
	"""

    third = [l[i] for i in range(len(l)) if 0 == i % 3]
    return [i for i in sorted(third)] + sort_third([l[i] for i in range(len(l)) if 0 != i % 3])

def count_vowels(string: str) -> int:
    """This function takes a string and counts the number of occurrences of lowercase vowels in that string.
    >>> count_vowels('hello')
    2
    >>> count_vowels('abc')
    0
    """

    string = string.lower()
    return sum([1 for char in string if char in ['a', 'e', 'i', 'o', 'u']])

def merge_files(first_name: str, second_name: str, out_name: str):
    """This function takes the names of two files first_name and second_name and outputs a single file containing all of the lines of the two input files preserving their original ordering, followed by any lines which only appear in one of the two files. It outputs the result to the file out_name.
    >>> merge_files('test_data/data_one.csv', 'test_data/data_two.csv', 'merged.csv')
    """

    from globals import PRETTY_PRIMER_DATABASE_DIR

    lines_first = open(PRETTY_PRIMER_DATASETS_DIR / first_name, 'r').readlines()
    lines_second = open(PRETTY_PRIMER_DATASETS_DIR / second_name, 'r').readlines()

    # merge the two
    for line in lines_first:
        if line in lines_second:
            lines_second.pop(lines_second.index(line))
        else:
            print("WARNING: LINE FOUND ONLY IN FIRST FILE: ", line)
    # remaining lines are exclusive to second file
    lines_first += lines_second

    # write to second file
    with open(PRETTY_PRIMER_DATASETS_DIR / out_name, 'w') as out_file:
        for line in lines_first