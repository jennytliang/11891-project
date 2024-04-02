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
    vowels = "aeiouAEIOU"
    for i in range(len(word)-1,0,-1):
        if word[i] in vowels and word[i-1] in vowels:
            return word[i]
    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("hoop") == "o"
    assert get_closest_vowel("crying") == "i"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("xyyzz") == "y"
    assert get_closest_vowel("xyzab") == ""
    assert get_closest_vowel("xyy") == ""
    assert get_closest_vowel("aaa") == ""
    assert get_closest_vowel("aabb") == ""
    assert get_closest_vowel("aaaabbb") == ""
    assert get_closest_vowel("aaabbb") == "a"
    assert get_closest_vowel("aaabbbccc") == "a"
    assert get_closest_vowel("aaabbbcccddd") == "a"
    assert get_closest_vowel("aaabbbcccddde") == "a"
    assert get_closest_vowel("aaabbbcccdddee") == "a"
    assert get_closest_vowel("aaabbbcccdddeee") == "a"
    assert get_closest_vowel("aaabbbcccdddeeee") == "a"
    assert get_closest_vowel("aaabbbcccdddeeeee") == "e"
    assert get_closest_vowel("aaabbbcccdddeeeeee") == "e"
    assert get_closest_vowel("aaabbbcccdddeeeeeee")