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
    l = len(word)
    if l < 3:
        return ""
    for i in range(l - 2, -1, -1):
        if word[i] in vowels:
            if word[i + 1] not in vowels and word[i + 2] in vowels:
                return word[i]
    return ""


def test_get_closest_vowel():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("abcd") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("c") == ""
    assert get_closest_vowel("d") == ""
    assert get_closest_vowel("e") == ""
    assert get_closest_vowel("f") == ""
    assert get_closest_vowel("g") == ""
    assert get_closest_vowel("h") == ""
    assert get_closest_vowel("i") == ""
    assert get_closest_vowel("j") == ""
    assert get_closest_vowel("k") == ""
    assert get_closest_vowel("l") == ""
    assert get_closest_vowel("m") == ""
    assert get_closest_vowel("n") == ""
    assert get_closest_vowel("o") == ""
    assert get_closest_vowel("p") == ""
    assert get_closest_vowel("q") == ""
    assert get_closest_vowel("r") == ""
    assert get_closest_vowel("s") == ""
    assert get_closest_vowel("t") == ""
    assert get