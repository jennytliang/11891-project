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
    planets = 'mercury venus earth mars jupiter saturn uranus neptune'.split()
    if planet1 in planets and planet2 in planets:
        planets.sort(key=lambda p: abs(planets.index(planet1) - planets.index(p)))
        return tuple(p for p in planets if p > planet1 and p < planet2)
    else:
        return ()


print(bf("Jupiter", "Neptune"))
print(bf("Earth", "Mercury"))
print(bf("Mercury", "Uranus"))