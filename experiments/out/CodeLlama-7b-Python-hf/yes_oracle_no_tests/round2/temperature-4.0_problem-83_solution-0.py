def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: n < 0 : return 0
	"""

  # 1. Take the input and check if it is a positive integer
    if n < 0:
        return 0

  # 2. Create a list to store the results
    results = []

  # 3. Create a for loop that will run for the number of digits in n
    for i in range(len(str(n))):
        if i == 0:
            results.append(str(n))
        else:
            results.append(str(n)[i:])

  # 4. Create a for loop that will run through the results list
    count = 0
    for i in results:
        if i[0] == '1':
            count += 1
        if i[-1] == '1':
            count += 1

  # 5. Return the count
    return count