def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # return 0 if the string does not even have a single character
    if len(string) <= 0:
        return 0

    lower_case_letters = 'qwertyuiopasdfghjklzxcvbnm'  # all lower-case alphabet

    # create a lookup table of which characters are encountered so that we do not keep re-counting the same character
    distinct_letters = [False] * len(lower_case_letters)

    # update the characters that are seen
    for character in string:
        if (character.lower() in lower_case_letters):
            distinct_letters[lower_case_letters.index(character.lower())] = True

    # check how many distinct characters are seen
    seen_count = sum(distinct_letters)
    return int(seen_count)


