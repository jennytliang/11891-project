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
	Do not include these tokens in the code: v ow els = [" a ",
	"""
    vowels = "aeiou"
    # your code here
    if len(word) < 3:
        return ""

    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            if word[i-1].isupper() and word[i+1].isupper():
                continue
            else:
                return word[i]

    return ""


if __name__ == '__main__':
    print(get_closest_vowel("yogurt"))
    print(get_closest_vowel("FULL"))
    print(get_closest_vowel("quick"))
    print(get_closest_vowel("ab"))
