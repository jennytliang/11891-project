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
    vowel_index = -1
    i = len(word) - 1
    while i > 0:
        if word[i] in vowels:
            vowel_index = i
            break
        i -= 1
    if vowel_index == -1:
        return ""
    i -= 1
    while i > 0:
        if word[i] not in vowels:
            return word[vowel_index]
        i -= 1
    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("happy") == "a"
    assert get_closest_vowel("apple") == "e"
    assert get_closest_vowel("happy birthday!") == "a"
    assert get_closest_vowel("python") == ""
    assert get_closest_vowel("qwertyuiop") == ""
    assert get_closest_vowel("aaaa") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("z") == ""

if __name__ == '__main__':
    test_function()
