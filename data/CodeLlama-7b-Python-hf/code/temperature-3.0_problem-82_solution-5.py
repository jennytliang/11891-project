def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    is_prime = True

    # check for 0 length strings
    if len(string) == 0:
        is_prime = False

    # check for 1 length strings
    elif len(string) == 1:
        is_prime = False

    # now we check for strings of 2 characters and longer
    else:
        # first check if the first and last character are equal to each other
        if string[0] == string[len(string)-1]:

            # now check to see if the length of the string divides evenly by 2
            if len(string) % 2 == 0:

                # now we check for odd number of characters
                for i in range(1, len(string)-1, 2):
                    if string[i] != string[i+1]:
                        is_prime = False

        # now we check for strings that start with the same character
        # and end with different characters
        elif string[0] == string[len(string)-1]:

            # now check to see if the length of the string divides evenly by 2
            if len(string) % 2 == 0:

                # now we check for odd number of characters
                for i in range(1, len(string)-1, 2):
                    if string[i] != string[i+1]:
                        is_prime = False

    return is_prime