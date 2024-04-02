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
    
	Include these tokens in the code: is
	Do not include these tokens in the code: get _ clos est
	"""

  
    # find the index of the first vowel and the last vowel
    first_vowel = None
    last_vowel = None
    for i in range(len(word)):
        if word[i] in "aeiou":
            if first_vowel is None:
                first_vowel = i
            last_vowel = i
    
    # if there is no vowel in the word, return ""
    if first_vowel is None or last_vowel is None:
        return ""
    
    # find the index of the closest vowel
    closest_vowel = None
    for i in range(first_vowel, last_vowel):
        if word[i] in "aeiou":
            closest_vowel = i
            break
    
    # if there is no closest vowel, return ""
    if closest_vowel is None:
        return ""
    
    # return the closest vowel
    return word[closest_vowel]


def main():
    print("Example:")
    print(get_closest_vowel("yogurt"))
    print(get_closest_vowel("FULL"))
    print(get_closest_vowel("quick"))
    print(get_closest_vowel("ab"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("o") == ""
    assert get_closest_vowel("e") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("q") == ""
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == "__main__":
    main()
