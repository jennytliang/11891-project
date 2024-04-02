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
    # for x in range(1,len(game)):
    #     for y in range(1,len(guess)):
    #         if game[x] == guess[y]:
    #             guess.remove(guess[y])
    #
    #         elif game[x] < guess[y]:
    #             n=abs(game[x]-guess[y])
    #             if n>=guess[y]:
    #                 guess.remove(guess[y])
    #
    #                 guess.append(0)
    #
    #         elif game[x] > guess[y]:
    #             n=abs(game[x] - guess[y])
    #             if n >= game[x]:
    #                 guess.remove(guess[y])
    #                 guess.append(abs(game[x] - guess[y]))
    #             else:
    #                 guess.remove(guess[y])
    #                 guess.append(0)
    #
    #
    # return guess
    # import numpy
    # game = numpy.array(game)
    # guess = numpy.array(guess)
    # return numpy.abs(game - guess)

    return numpy.abs(game - guess)