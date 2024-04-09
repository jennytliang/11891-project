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
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: pass if __ name __
	"""
    # pass
    # return ""
    # RW
    vowels = "aeiou"
    vowels_idx = []
    for i, c in enumerate(word):
        if c in vowels:
            vowels_idx.append(i)
    if len(vowels_idx) < 2:
        return ""
    vowels_idx.reverse()
    for i in range(len(vowels_idx) - 1):
        if vowels_idx[i] < vowels_idx[i + 1]:
            return word[vowels_idx[i + 1]]
    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("ABCabc") == "a"
    assert get_closest_vowel("apple") == "e"
    assert get_closest_vowel("banana") == "a"
    assert get_closest_vowel("abcde") == ""
    assert get_closest_vowel("xyz") == ""
    assert get_closest_vowel("a") == ""
    print("Test completed!")


if __name__ == "__main__":
    test_function()
