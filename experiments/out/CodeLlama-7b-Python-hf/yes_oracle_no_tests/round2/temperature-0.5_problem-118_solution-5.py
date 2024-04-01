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
    vowels = "aeiou"
    for i in range(len(word)-1, 0, -1):
        if is_vowel(word[i]):
            for j in range(i-1, 0, -1):
                if not is_vowel(word[j]):
                    return word[j]
    return ""


def is_vowel(ch):
    return ch in "aeiou"


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("hiss") == "i"
    assert get_closest_vowel("gnaw") == "a"
    assert get_closest_vowel("gnash") == "a"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("gear") == "a"
    assert get_closest_vowel("eat") == "a"
    assert get_closest_vowel("quiz") == "i"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("bead") == "a"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("hut") == "u"
    assert get_closest_vowel("hut") == "u"
    assert get_clos