def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    
    # My first attempt: loop over the nested lists, and using the "abs" method on the elements of the two sublists, create a list containing absolute values. Then run the "map" (or maybe "filter"?) function and pass it both sublists and the value we want returned in the respective positions in the final list
    #def my_compare(guess_lst,score)
    

    correct_guesses = [] # A list of zeros
    wrong_guess = []
    list1 = [guess_lst,] # I create an empty list, and after the loop put in the final list of zero values
    # list2 = [[score,]] - same as above

    for i in range(len(guess_lst)): 
    "I use range as it seems like a quick and not too expensive solution. But for large lists this is not ideal"


        # I then say i=0. So I would compare the first elements of each list. And if they are the same append to my_list1, add the value of 0.  If the values aren't the same, subtract the smaller from the bigger and use this as a guide to how far I was off with the value given in the guess as a positive integer

        if i == 0:# This is where i should set the first condition, that i should not be the first value, as we would have already done the above logic
            
            if guess_lst == []:#I should not be creating the first entry of the zero lists if the original lists have length zero, it would be wrong
            
               list1.append([0,])   ### This might be the right way to approach it 

        else:


            correct = abs(score[i-1]- guess_lst[i-1])  # This is where I am subtracting the number to the left in list1 to check the correct position.
            incorrect =[correct]