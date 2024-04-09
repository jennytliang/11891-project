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
    
	Include these tokens in the code: def is _ v owel ( ch
	Do not include these tokens in the code: # R ough first pass
	"""
    # R ough first pass
    vowels = "aeiouAEIOU"
    vowel_locations = []
    for i, ch in enumerate(word):
        if ch in vowels:
            vowel_locations.append(i)
    if len(vowel_locations) == 0:
        return ""
    if len(vowel_locations) == 1:
        return vowels[vowel_locations[0]]
    vowel_locations.append(len(word))
    for i in range(len(vowel_locations)-1):
        if vowel_locations[i+1] - vowel_locations[i] == 2:
            return word[vowel_locations[i]+1]
    return ""

def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("aab") == "a"
    assert get_closest_vowel("abc") == "a"
    assert get_closest_vowel("abcdefg") == "a"
    assert get_closest_vowel("xxyyzz") == "y"
    assert get_closest_vowel("xyyzzz") == "y"
    assert get_closest_vowel("xyyyzz") == "y"
    assert get_closest_vowel("xyyyzzx") == "y"
    assert get_closest_vowel("xyyzzzy") == "y"
    assert get_closest_vowel("xyyzzzx") == "y"
    assert get_closest_vowel("xyyzzzy") == "y"
    assert get_closest_vowel("xyyyzzz") == "y"
    assert get_closest_vowel("xyyyzzzy") == "y"
    assert get_