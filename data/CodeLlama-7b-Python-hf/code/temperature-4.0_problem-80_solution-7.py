def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    happy = False
    string = list(s)
        
    # Check a minimum length
    # In case one of the condition fail for minimum length then, no point of checking.
    # If it pass for minimum value, we would try to find if it contains repeating three consecutive characters. 
    if len(s) >= 3:
                
        # Initialise a count variable. If all three letters are not matching then, count is set to 1.                  
        no_repeating_counter = 1
        # Count the consecutive three letters, if all are not matching then, count reset to 0.       
        no_of_three_same_char_count = 0           

        # 1st and last character is taken to compare and find the next two elements.
        for x in string[:-1]:

            # 3 consecutive letters is taken to match.
            i,j = x,string[-1]
            k = j

            temp_list = s.split(k)
            next_two_ch = [temp_list[0][-2],temp_list[0][-1]]
            print("next_ch",x)
            print(temp_list,s.split(k)[0])
            # 1st three letters matched then, add count. Otherwise, make counter = 1.                     
            if i == next_two_ch[1] and next_two_ch[1] == string[0]:
                next_three_char = [i,string[0],[string[0],s.split(x)[0][-2][-1],s.split(x)[0][-1]]]
                #print("next3ch",i,temp_list,s.split(i))
                print("is_haptic",next_three_char,temp_list)
                
                continue

            elif str(i) == x or x != k:            
                
                # If count != 0 this means, there is a repeating occurrence of three consecutive characters in the given string.
                # As it is found once at the beginning then we stop checking the string for the same occurrence.
                            # A string is unhappy if it found the same repeating character three consecutive values.                
                if next_three_char[0] != [s[0],s[0],x]: 
                    # Checking count to find if three consecutive letters are all different than 1. Increment by one.            
                    count = 1
                    for l in next_three_char[1:]:            
                        
                        if len(l)==2:                
                            temp_list = s.split("".join(l))

                            if len(temp_list) == 1:                
                                break
                            