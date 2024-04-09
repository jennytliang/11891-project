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
	Do not include these tokens in the code: # find the index
	"""
    # Find the index of the first consonant from the right side
    for i in range(len(word)-1, -1, -1):
        if word[i].isalpha() and word[i].isupper():
            break
    else:
        return ""

    if i == len(word)-1:
        return ""
    
    # Find the index of the first vowel from the right side
    for j in range(i+1, len(word)):
        if word[j].isalpha() and word[j].islower():
            break
    else:
        return ""
    
    # Find the index of the first consonant from the left side
    for k in range(i-1, -1, -1):
        if word[k].isalpha() and word[k].isupper():
            break
    else:
        return ""
    
    # Find the index of the first vowel from the left side
    for l in range(k-1, -1, -1):
        if word[l].isalpha() and word[l].islower():
            break
    else:
        return ""
    
    if k < l:
        return ""
    
    return word[j]


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("Q") == ""
    assert get_closest_vowel("QUICK") == "I"
    assert get_closest_vowel("QUICK!") == "I"
    assert get_closest_vowel("acorn") == "a"
    assert get_closest_vowel("x") == ""
    assert get_closest_vowel("XYZ") == "Y"

if __name__ == '__main__':
    test_