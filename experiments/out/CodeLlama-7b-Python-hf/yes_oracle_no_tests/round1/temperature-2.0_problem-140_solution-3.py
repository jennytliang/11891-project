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
	#TODO: write your code here
	
	# replace all spaces with underscores
	ans = text.replace(" ", "_")
	
	# loop through the string and find consecutive spaces
	for i in range(len(ans)):
		if ans[i] == " ":
			# if there are more than 2 consecutive spaces, replace with a -
			if ans[i+1] == " " and ans[i+2] == " ":
				ans = ans.replace("  ", "-")
	
	return ans
		
	
print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))