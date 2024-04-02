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
    i = 0
    while i < len(word):
        if is_vowel(word[i]):
            return word[i]
        i += 1
    return ""


def is_vowel(ch):
    return ch in "AEIOUaeiou"


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("ABC") == ""
    assert get_closest_vowel("xy") == ""
    assert get_closest_vowel("xyu") == "u"
    assert get_closest_vowel("xyZ") == ""
    assert get_closest_vowel("abcXYZ") == ""
    assert get_closest_vowel("abcUVWXYZ") == "U"
    assert get_closest_vowel("abcUVWXYzy") == "y"
    assert get_closest_vowel("abcUVWXYzyu") == "u"
    assert get_closest_vowel("abcUVWXYzyuio") == "u"
    assert get_closest_vowel("abcUVWXYzyuio1") == ""
    assert get_closest_vowel("abcUVWXYzyuio123") == ""


if __name__ == '__main__':
    test_function()
