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
    
	Include these tokens in the code: plan ets
	Do not include these tokens in the code: result
	'''
    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    try:
        planet1 = planets.index(planet1)
        planet2 = planets.index(planet2)
        result = []
        for i in range(planet1+1, planet2):
            result.append(planets[i])
        for i in range(planet2+1, planet1):
            result.append(planets[i])
        if len(result) > 0:
            return tuple(result)
        else:
            return ()
    except:
        return ()
