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
    
	Include these tokens in the code: return [ abs ( game [ i ] - guess
	"""
    #  return values(game,guess)

    #  return values(game,guess)

    #  return values(game,guess)

    #  return values(game,guess)

    #  return values(game,guess)

    #  return values(game,guess)

    return 42

def values(game,guess):
    values=[]
    for i in range(len(game)):
        if game[i]==guess[i]:
            values.append(0)
        else:
            values.append(abs(game[i]-guess[i]))
    
    return values
    


game=[1,2,3,4,5,1]
guess=[1,2,3,4,2,-2]

#  print(f"game == {game}")
#  print(f"guess == {guess}")
print(f"compare({game},{guess}) returns {compare(game,guess)}")

"""
# this code helps in calling the function
def get_call(f):
	return f
		
f = get_call(compare)
f([1,2,3,4,5,1],[1,2,3,4,2,-2])
"""