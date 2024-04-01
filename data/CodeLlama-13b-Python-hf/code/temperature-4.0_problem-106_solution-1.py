def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """


    result_list = [None] * n  # Create an array with all None
    sum_from_one =1  # Init sum for odd

    # Use 3 loops, this is the fastest (O(n)- linear) with constant space O(n) because you need to store 2 numbers at any given moment
    for i in range(n):
        if i%2== 0:
            j=1
            fac =1  # Init factorial to store in index
            for j in range(i+1):
                fac=fac*j # Factorial calculation with product
                print(fac)

            # Set value in even index
            result_list[i]=fac # Set value at index i = factorial

            print("Even {} {}".format(i,fac))  # Check if it's ok
            print("Result List: {}".format(result_list))  # Check if it's ok
            fac=1

            # Set value at odd index
            j=1
            while j*j <= i:
                print("Value i: {} Value j {} and sum from one: {}". format(i, j, sum_from_one))  # This is for development
                if j * j <= i:
                    # Get index where you have to add and add to the value there
                    index_to_i = i-j + 1 # this is not i-1 because j goes to square root of n. 1-4 or 1 -7 or so. And you want to update the j-1
                    # if index 0,1,3,4 are in odd index, update the value. if are even, keep the same value or add i
                    if result_list[index_to_i]!= None: # Check if is not none, to make sure if you don't update and just sum one
                        if result_list[index_to_i]+sum_from_one<=fac: # Update to the minimum of the value you have +1, j or factorial
                            result_list[index_to_i]=result_list[index_to_i]+sum_from_one # Update in odd
                j+=1  # Even update to 1 again
            j=1
            print("Result List: {}". format(result_list))  # This is to show you how values are being updated, after a while in odd
            sum_from_one+=1 # This step will be skipped because j will be a square and you will need another j*j step to increment, which will make it even so you use sum from one to add it
        else:  # odd
            while j*j<=i: # Here you just add the first odd values

                # This is how you update when is a square. You just add the first number. If you have more, that are the same because you have no value so you just copy them
                # Get index for the current odd


                j_1 = i-j +1  # Get position to add i. 5-3 so it would be in the second position of result list. This is not i -1 because the last one is not being considered
                print("Position 1: {}".format(j_1))
                print("Index to update {} Odd Value {} index to update value {}".format(j_1,i,result_list[j_1]))
                if j<i/2:  # check if you have a previous value or if it is a square number
                    max_value = result_list[j_1] # this is the first value you encounter which is factorial. Even numbers
                else: # If are a square, all other values below are the same or plus 1 than that you store. So in this value you store the next i
                    break  # Break because you reached the limit, you store i
                if j<i: # if i ==5, you will update all values below so you have to update all before the half. If i==3 all values before 2
                   j_2 = i-j + 2 # This will update only all numbers below the j. I-3+2 for j=3 , i-2+2, to make sure it goes below that index. So i-5+3 is 3-5 = 2+3 , so you update above 3 and before 4 and you check the value in this index. And do it for all values below that. If not, it will update just index 5 and update all numbers below
                   print(j_1, j_2)
                   if i%j_2!=0: # Check if the index to update has a value, that is if it is the first number below or the square number you're checking now. # If j=1, this will be i%1==0, 1!=0 so you enter the condition
                      print("Adding value {}, Position 2: {}, Odd value: {} Index to check: {} index to update index: {} previous index: {}". format(i,i, j_2,j_2,j_2, result_list[j])) # This is just a check on how many values you're storing and which values
                       # If i = 6, then i will be odd, so will update.
                       # It will update with 10 to 4+1, 5+1, 4+1 and add 6 to update previous values that are below that are not in previous if condition.
                   else: # This will occur if you have odd numbers under it like 20
                      print("No updating in this case") # it will do nothing because that update will store values in the index
                        # 2^2=16, 2^3=8 so update all above 2. 5=3 (square root), 2*2 = 4. 6-4
                   print("I {}, Index to check 2: {} Index to up {} previous value {} Result list before: {}". format(i,j_2, j_1, result_list[j], result_list))   # Make sure in square you check all the ones below and add i to all index that you want
                   if result_list[j_2] <= (i+1) * (j_2+1) // 2 + 1: # If the value of j_2, is less than what is going to be stored update. if index for 4, 2<=4+1. if index 8 4<=1+8
                       j_1 = j_2
                # Update values in odd numbers when you have numbers below the square. So this updates the odd. If are odd, you store i at the index. Then update the following odd numbers.
                # This is because the odd numbers above are not in this loop. So you just take their values and increment them by one and you add it
                if j*j<=j_1:# You just check that you do not update a new i when the value is already in index
                    print("Index to update {}, previous index {} Index 1 before update {} value i:{} Index 2 to check {} value index to check {}". format(j_1, result_list[j_1],result_list[i+1], result_list[i+1],j,result_list[j]))
                        if max_value!=None:   # Check if we have a value that represents the index below. The first one has no previous so we need the second one. If are square, it will not change the value so check this
                            result_list[j_1]=max_value  # Just assign the value to the index you have
                print("Checking if it is square")  # This is just for development to show you which one is square or which one not and when you store values for odd


                j+=1 # Increment one number just to make sure you increment

        if i==n-1: # Check if is last value and if is odd to update the number
                if j<=n-1: # if is above that value, then break
                    j=j-1 # Update one more number up and then add it. Because this is an even list and you just can't put in odd index. This is the last one and the one before last if i=4, i=3 for j. So you add last one
        # Here you add the values so that you keep them

        print(result_list) # Just for development to check the results, this should be above and not in the end. If not it will just show that values are not updated yet
        print("Check values for odd {} Values of index {} Odd value {} Index to update {} previous max Value {} List before {} Results {}".format(j,i, i,j, result_list[i