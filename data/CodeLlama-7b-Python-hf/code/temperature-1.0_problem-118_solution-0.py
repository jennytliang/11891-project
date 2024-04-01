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
    """
    vowels = "aeiouAEIOU"
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            for j in range(i-1, -1, -1):
                if word[j] not in vowels:
                    for k in range(j-1, -1, -1):
                        if word[k] in vowels:
                            return word[k]
    return ""