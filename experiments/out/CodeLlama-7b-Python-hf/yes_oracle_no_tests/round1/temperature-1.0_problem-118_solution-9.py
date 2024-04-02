def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    
	Include these tokens in the code: def is _ v owel ( ch : str )
	"""
    # First find the index of the last consonant
    last_consonant = len(word) - 1
    while word[last_consonant].isalpha() and word[last_consonant].islower():
        last_consonant -= 1

    # Then find the index of the first consonant
    first_consonant = 0
    while word[first_consonant].isalpha() and word[first_consonant].islower():
        first_consonant += 1

    # If there are no consonants, return an empty string
    if first_consonant == last_consonant:
        return ""

    # Find the index of the closest vowel
    for i in range(last_consonant, first_consonant, -1):
        if word[i].isalpha() and word[i].isupper():
            return word[i]

    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("ABCDEFGH") == ""
    assert get_closest_vowel("ABCDEFGHijklm") == "j"
    assert get_closest_vowel("ABCDEFGHijklmn") == ""
    assert get_closest_vowel("ABCDEFGHijklmno") == ""
    assert get_closest_vowel("abcdefgh") == ""
    assert get_closest_vowel("abcdefghijklm") == "j"
    assert get_closest_vowel("abcdefghijklmn") == ""
    assert get_closest_vowel("abcdefghijklmno") == ""
