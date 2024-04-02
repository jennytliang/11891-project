def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: ( s
	"""

    wo_sp_commas_string = ""
    wo_commas_string  = ""
    wo_commas_string2 = ""
    wo_commas_string_array = [[]]* 2
    # print(wo_commas_string_array)
    if (s != ""):
                wo_sp_commas_string = s.replace(" ","")
                wo_commas_string = wo_sp_commas_string.replace(",", " ")
                wo_commas_string2 = wo_commas_string.split()
    
    wo_commas_string_array[0] = wo_commas_string2
    
    return wo_commas_string_array