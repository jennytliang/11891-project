def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    
	Include these tokens in the code: plan ets = ["
	Do not include these tokens in the code: if planet 1 == "
	'''
    print(planet1, planet2)
    result = ()
    planetList = ["Mercury", "Venus", "Earth", "Mars",
                  "Jupiter", "Saturn", "Uranus", "Neptune"]
    p = len(planetList) - 1
    while len(result) == 0:
        if planet1 in planetList:
            for i in range(len(planetList)):
                if planetList[i] > planet1 and planetList[i] < planet2:
                    result = result + tuple((planetList[i],))
                    if planetList[i] == planet2:
                        break
        elif planet2 in planetList:
            for i in range(len(planetList)):
                if planetList[i] < planet1 and planetList[i] > planet2:
                    result = result + tuple((planetList[i],))
                    if planetList[i] == planet1:
                        break
        else:
            planetList.append(planet1)
            planetList.append(planet2)
            result = ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

    print(result)


bf("Jupiter", "Neptune")
# bf("Earth", "Mercury")
# bf("Mercury", "Uranus")
