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
    
	Do not include these tokens in the code: i = 3
	"""
    
    # if the string is less than 3 chars, it's not happy
    if len(s) < 3:
        return False

    # get the first 3 chars
    first_3 = s[0:3]

    # check if the first 3 chars are all distinct
    if len(set(first_3)) == 3:
        # the first 3 chars are all distinct, so we can check the next 3 chars
        next_3 = s[1:4]

        # check if the next 3 chars are all distinct
        if len(set(next_3)) == 3:
            # the next 3 chars are all distinct, so we can check the next 3 chars
            next_3 = s[2:5]

            # check if the next 3 chars are all distinct
            if len(set(next_3)) == 3:
                # the next 3 chars are all distinct, so we can check the next 3 chars
                next_3 = s[3:6]

                # check if the next 3 chars are all distinct
                if len(set(next_3)) == 3:
                    # the next 3 chars are all distinct, so we can check the next 3 chars
                    next_3 = s[4:7]

                    # check if the next 3 chars are all distinct
                    if len(set(next_3)) == 3:
                        # the next 3 chars are all distinct, so we can check the next 3 chars
                        next_3 = s[5:8]

                        # check if the next 3 chars are all distinct
                        if len(set(next_3)) == 3:
                            # the next 3 chars are all distinct, so we can check the next 3 chars
                            next_3 = s[6:9]

                            # check if the next 3 chars are all distinct
                            if len(set(next_3)) == 3:
                                # the next 3 chars are all distinct, so we can check the next 3 chars
                                next_3 = s[