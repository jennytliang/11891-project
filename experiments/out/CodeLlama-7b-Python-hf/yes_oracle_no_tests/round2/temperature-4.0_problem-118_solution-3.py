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
    
	Include these tokens in the code: def is _ v owel
	Do not include these tokens in the code: if len
	"""
    if not word:
        return ""
    
    vowels = "aeiouAEIOU"
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            if word[i-1].isupper():
                return word[i]
            if word[i-1].islower():
                if i == 1:
                    return word[i]
                if i > 1 and word[i-2].isupper():
                    return word[i]
                if i > 1 and word[i-2].islower():
                    return word[i]
    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("honey") == "o"
    assert get_closest_vowel("blue") == "o"
    assert get_closest_vowel("love") == "o"
    assert get_closest_vowel("eve") == "o"
    assert get_closest_vowel("HONEY") == "O"
    assert get_closest_vowel("LOVE") == "O"
    assert get_closest_vowel("EV") == "O"
    assert get_closest_vowel("E") == ""
    assert get_closest_vowel("B") == ""
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("yogurt123") == "u"
    assert get_closest_vowel("yogurt12345") == "u"
    assert get_closest_vowel("yogurt123456") == ""
    assert get_closest_vowel("123456") == ""
    assert get_closest_vowel("123456789") == ""
    assert get_closest_vowel("123456789