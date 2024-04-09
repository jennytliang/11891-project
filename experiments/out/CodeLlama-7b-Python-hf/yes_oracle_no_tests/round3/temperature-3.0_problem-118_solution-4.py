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
    pass

if __name__ == '__main__':
    print("Example:")
    print(get_closest_vowel("yogurt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("q") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("x") == ""
    assert get_closest_vowel("z") == ""
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("yogUrt") == "U"
    assert get_closest_vowel("yogurtX") == "u"
    assert get_closest_vowel("yogurtZ") == "u"
    assert get_closest_vowel("yogurtZX") == "u"
    assert get_closest_vowel("yogurtZXY") == "u"
    assert get_closest_vowel("yogurtXYZ") == "u"
    assert get_closest_vowel("yogurtXZY") == "u"
    assert get_closest_vowel("yogurtXyZ") == "u"
    assert get_closest_vowel("yogurtXyZy") == "y"
    assert get_closest_vowel("yogurtXyZY") == "y"
    assert get_closest_vowel("XyZY") == "y"
    assert get_closest_vowel("XyZYx") == "y"
    assert get_closest_vowel("XyZYX") == "y"
    assert get_closest_vowel("XyZYXa") == "y"
    assert get_closest_vowel("X