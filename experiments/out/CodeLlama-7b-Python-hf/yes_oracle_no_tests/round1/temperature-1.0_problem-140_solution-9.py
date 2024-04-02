def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans = text for i in range (
	"""
    
	#create the empty answer ans
    ans = ""
    
    #for every character in text, add it to ans
    #without copying consecutive space chars
    for i in range(len(text)):
        #if its not the last char, and 
        #the char is not space, it needs to be processed
        #and the char after it is not space as well
        if i + 1 < len(text) and text[i] != ' ':
            ans += text[i]
        #if its not the last char, and
        #the char is space, but the char after it is space, 
        #and I dont have 2 consecutive spaces
        elif i + 1 < len(text) and text[i] == ' ' and text[i + 1] == ' ':
            ans += "-"
        #if its the last char, and
        #the char is space, and the
        #the char before it is not space
        #I have 2 consecutive spaces
        elif i + 1 == len(text) and text[i] == ' ' and text[i - 1] != ' ':
            ans += "_"
        #its the last char and it
        #is not a space, or its the first char and it is not
        #a space
        else:
            ans += text[i]
            #if text[i - 1] == ' ' and text[i] == ' ':
        
    
    
    return ans
    
def test_string(string):
  print("======= Input =======")
  print(string)
  print("======= Output =======")
  print(fix_spaces(string))

test_string(" Example 2 ")
# _Example_2
