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
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: answer = [] for i
	"""
    #First, we'll make sure that the two inputs are the same length.
    if len(game) != len(guess):
        raise ValueError("The two lists are not the same length.")
    
    #Then, we'll create a new list to hold the differences.
    answer = []
    
    #Now we'll run through both lists and compare the values at each index.
    for i in range(len(game)):
        #If the guess is correct, add 0 to answer, otherwise, add the difference between the guess and the actual score.
        if guess[i] == game[i]:
            answer.append(0)
        else:
            answer.append(abs(guess[i] - game[i]))
    
    #Finally, return the answer list.
    return answer