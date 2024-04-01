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
    vowels = ["a", "e", "i", "o", "u"]
    vowel_positions = [i for i, letter in enumerate(word) if letter in vowels]
    vowel_count = len(vowel_positions)

    # Check if there are 2 or more vowels and check if the right side starts with a vowel
    if vowel_count >= 2 and word[-1] in vowels:
        return word[vowel_positions[-1]]
    
    if word[-1] in vowels or word[0] in vowels:
        return ""

    # If there are vowels but the right side has no vowels
    if vowel_count >= 2:
        return word[vowel_positions[-1]]

    # Find closest vowel from right side
    for position in range(len(word)-1, -1, -1):
        letter = word[position]
        if letter in vowels:
            return letter
    
    return ""



def main():
    print("Pass" if (get_closest_vowel("foobar") == "o") else "Fail") 
    print("Pass" if (get_closest_vowel("quick") == "") else "Fail") 
    print("Pass" if (get_closest_vowel("FuN") == "U") else "Fail") 


main()