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
    word = word.upper()
    vowels = "AEIOU"

    # Check the last character
    i = len(word) - 1
    while word[i] not in vowels and i > 0:
        i -= 1
    if word[i] in vowels:
        return word[i]

    # Check the first character
    i = 1
    while word[i] not in vowels and i < len(word) - 1:
        i += 1
    if word[i] in vowels:
        return word[i]

    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("abab") == ""
    assert get_closest_vowel("ababab") == ""
    assert get_closest_vowel("ababababab") == ""
    assert get_closest_vowel("abababababab") == ""
    assert get_closest_vowel("ababababababab") == ""
    assert get_closest_vowel("abababababababab") == ""
    assert get_closest_vowel("ababababababababab") == ""
    assert get_closest_vowel("abababababababababab") == ""
    assert get_closest_vowel("ababababababababababab") == ""
    assert get_closest_vowel("abababababababababababab") == ""
    assert get_closest_vowel("ababababababababababababab") == ""
    assert get_closest_