def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if a == b : return True
	"""
 def check(word,sub):
        if len(word) == 0:
            return False
        if len(word)==len(sub) and word[0]==sub[0]:
            return True
        if sub in word:
            return True
        subs=word[1:]+word[0]
        return check(word[1:]+word[0],sub)

    return check(a.lower(),b.lower())   
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cycpattern_check("hello", "ell") == True, "helo toello"
    assert cycpattern_check("hello", "ehllo") ==  False, "ehllo oello"
    assert cycpattern_check("I like cycling", "cycling") ==  True, "I like cyclingo"
    assert cycpattern_check("We start coding at 6:00 pm", "We start coding") ==  False, "We start coding a 6:00pm"
