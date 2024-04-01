def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    
	Include these tokens in the code: s = sum ( map ( lambda x : int
	Do not include these tokens in the code: # your code here
	"""

    # 1. Converting the decimal number into binary:
    binary_number = bin(N)

    # 2. Splitting the binary number into a list of binary digits:
    binary_number_list = list(binary_number)

    # 3. Removing the '0b' from the list:
    binary_number_list.remove('0b')

    # 4. Removing the last digit of the binary number:
    binary_number_list.pop()

    # 5. Converting the list of binary digits into a string:
    binary_number_string = ''.join(binary_number_list)

    # 6. Converting the string into a list of binary digits:
    binary_number_string_list = list(binary_number_string)

    # 7. Adding the digits in the list:
    sum_of_digits = 0
    for digit in binary_number_string_list:
        sum_of_digits += int(digit)

    # 8. Converting the sum of digits into a string:
    sum_of_digits_string = str(sum_of_digits)

    # 9. Returning the result:
    return sum_of_digits_string


# 10. Testing the function:
print(solve(1000))
print(solve(150))
print(solve(147))

# 11. Checking the function:
# assert solve(1000) == "1"
# assert solve(150) == "110"
# assert solve(147) == "1100"

# 12. Checking the function:
# print(solve(1000))
# print(solve(150))
# print(solve(147))
