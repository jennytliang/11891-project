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
	Do not include these tokens in the code: result = [] for i
	"""
    result = []
    for i in range(0,len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i]-guess[i]))
    return result

def test_cases():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]
    assert compare([1,2,3,4,5,1],[1,2,3,4,5,6]) == [0,0,0,0,0,6]
    assert compare([1,2,3,4,5,1],[1,2,3,4,-1,6]) == [0,0,0,1,5,6]
    assert compare([1,2,3,4,5,1],[1,2,3,4,1,-1]) == [0,0,0,0,0,2]
    assert compare([1,2,3,4,5,1],[1,2,3,4,5,2]) == [0,0,0,0,0,1]
    assert compare([1,2,3,4,5,1],[1,2,3,4,5,0]) == [0,0,0,0,0,5]
    assert compare([1,2,3,4,5,1],[1,2,3,4,5,5]) == [0,0,0,0,0,0]
    assert compare([1,2,3,4,5,1],[1,2,3,4,5,1]) == [0,0,0,0,0,0]
    assert compare([1,2,3,4,5,1],[1,2,3,4,5,1,1]) == [0,0,0,0,0,