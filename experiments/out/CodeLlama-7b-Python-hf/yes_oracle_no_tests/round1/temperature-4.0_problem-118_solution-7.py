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
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(word) < 3: return ""
    
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels and word[i - 1].isalpha() and word[i + 1].isalpha():
            return word[i]
    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("ABC") == ""
    assert get_closest_vowel("banana") == "a"
    assert get_closest_vowel("abcdefgh") == ""
    assert get_closest_vowel("qweRtyUIOPnlkjhgfdsazxcv") == "a"
    assert get_closest_vowel("qwErtyUIOPnlkjhgfdsazxcv") == "a"
    assert get_closest_vowel("qwertyuinlkjhgfdsazxcv") == ""
