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
    vowel_index = -1
    for i in range(len(word)):
        if is_vowel(word[i]):
            vowel_index = i
            break
    if vowel_index == -1:
        return ""
    for i in range(vowel_index, len(word)):
        if is_consonant(word[i]):
            for j in range(i + 1, len(word)):
                if is_vowel(word[j]):
                    return word[j]
    return ""

def is_vowel(ch):
    return ch in "aeiou"

def is_consonant(ch):
    return ch not in "aeiou"

if __name__ == '__main__':
    print("Example:")
    print(get_closest_vowel("yogurt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
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
    assert get_closest_vowel("m")