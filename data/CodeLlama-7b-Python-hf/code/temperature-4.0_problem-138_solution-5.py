def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_of_numbers_even_to_check = 0
    counter = 4
    for num in range (0,counter):
        for j in range(0, counter):
            if sum_of_numbers_even_to_check  + (num* 2**num)/ 2 ** (counter+1)  < n  :

                if sum_of_numbers_even_to_check +  (j* 2 ** num) == n  :
                    return 1

            if sum_of_numbers_even_to_check < n  :
                if num* 2 ** num <= n  :
                    pass

